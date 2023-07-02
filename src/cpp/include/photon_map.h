#ifndef _PHOTON_MAP_H
#define _PHOTON_MAP_H

#include <concepts>
#include <type_traits>
#include <numeric>
#include <queue>
#include <vector>

#include "core.h"

struct Photon {
    Vec3f throughput;  // BxDF * Geometric Term / pdf
    Vec3f position;
    Vec3f wi;  // incident direction
    unsigned int triId = 0; // id of the triangle on which the photon ended up

    // implementation of Point concept
    static constexpr int dim = 3;

    float operator[](int i) const { return position[i]; }

    Photon() = default;

    Photon(const Vec3f &throughput, const Vec3f &position, const Vec3f &wi, const unsigned int triId)
            : throughput(throughput), position(position), wi(wi), triId(triId) {}
};

// Point concept
/*template <typename T>
concept Point = requires(T& x, int i) {
  { T::dim } -> std::convertible_to<int>;  // dimension
  { x[i] } -> std::convertible_to<float>;  // element access
};
*/

// compute the squared distance between given points
// NOTE: assume PointT and PointU has the same dimension
template<typename PointT, typename PointU>
//requires Point<PointT> && Point<PointU>
inline float distance2(const PointT &p1, const PointU &p2) {
    float dist2 = 0;
    for (int i = 0; i < PointT::dim; ++i) {
        dist2 += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    }
    return dist2;
}

// implementation of kd-tree
template<typename PointT>
//requires Point<PointT>
class KdTree {
private:
    struct Node {
        int axis;           // separation axis(x=0, y=1, z=2)
        int idx;            // index of median point
        int leftChildIdx;   // index of left child
        int rightChildIdx;  // index of right child

        Node() : axis(-1), idx(-1), leftChildIdx(-1), rightChildIdx(-1) {}
    };

    std::vector<Node> nodes;  // array of tree nodes
    const PointT *points;     // pointer to array of points
    int nPoints;              // number of points

    void buildNode(int *indices, int n_points, int depth) {
        if (n_points <= 0) return;

        // choose separation axis
        const int axis = depth % 3;

        // sort indices by coordination in the separation axis.
        std::sort(indices, indices + n_points, [&](const int idx1, const int idx2) {
            return points[idx1][axis] < points[idx2][axis];
        });

        // index of middle element of indices
        const int mid = (n_points - 1) / 2;

        // add node to node array, remember index of current node(parent node)
        const int parentIdx = nodes.size();
        Node node;
        node.axis = axis;
        node.idx = indices[mid];
        nodes.push_back(node);

        // add left children to node array
        const int leftChildIdx = nodes.size();
        buildNode(indices, mid, depth + 1);

        // set index of left child on parent node
        // if size of nodes doesn't change, it means there is no left children
        if (leftChildIdx == nodes.size()) {
            nodes[parentIdx].leftChildIdx = -1;
        } else {
            nodes[parentIdx].leftChildIdx = leftChildIdx;
        }

        // add right children to node array
        const int rightChildIdx = nodes.size();
        buildNode(indices + mid + 1, n_points - mid - 1, depth + 1);

        // set index of right child on parent node
        // if size of nodes doesn't change, it means there is no right children
        if (rightChildIdx == nodes.size()) {
            nodes[parentIdx].rightChildIdx = -1;
        } else {
            nodes[parentIdx].rightChildIdx = rightChildIdx;
        }
    }

    using KNNQueue = std::priority_queue<std::pair<float, int>>;

    template<typename PointU>
    //requires Point<PointU>
    void searchKNearestNode(int nodeIdx, PointU &queryPoint, int k,
                            KNNQueue &queue) const {
        if (nodeIdx == -1 || nodeIdx >= nodes.size()) return;

        const Node &node = nodes[nodeIdx];

        // median point
        const PointT &median = points[node.idx];

        // push to queue
        const float dist2 = distance2(queryPoint, median);
        queue.emplace(dist2, node.idx);

        // if size of queue is larger than k, pop queue
        if (queue.size() > k) {
            queue.pop();
        }

        // if query point is lower than median, search left child
        // else, search right child
        const bool isLower = queryPoint[node.axis] < median[node.axis];
        if (isLower) {
            searchKNearestNode(node.leftChildIdx, queryPoint, k, queue);
        } else {
            searchKNearestNode(node.rightChildIdx, queryPoint, k, queue);
        }

        // at leaf node, if size of queue is smaller than k, or queue's largest
        // minimum distance overlaps sibblings region, then search siblings
        const float dist_to_siblings = median[node.axis] - queryPoint[node.axis];
        if (queue.top().first > dist_to_siblings * dist_to_siblings) {
            if (isLower) {
                searchKNearestNode(node.rightChildIdx, queryPoint, k, queue);
            } else {
                searchKNearestNode(node.leftChildIdx, queryPoint, k, queue);
            }
        }
    }

public:
    KdTree() = default;

    void setPoints(PointT *points, int nPoints) {
        this->points = points;
        this->nPoints = nPoints;
    }

    void buildTree() {
        // setup indices of points
        std::vector<int> indices(nPoints);
        std::iota(indices.begin(), indices.end(), 0);

        // build tree recursively
        buildNode(indices.data(), nPoints, 0);
    }

    template<typename PointU>
    //requires Point<PointU>
    std::vector<int> searchKNearest(
            PointU &queryPoint, int k, float &maxDist2)
    const {
        KNNQueue queue;
        searchKNearestNode(0, queryPoint, k, queue);

        std::vector<int> ret(queue.size());
        maxDist2 = 0;
        for (int &i: ret) {
            const auto &p = queue.top();
            i = p.second;
            maxDist2 = std::max(maxDist2, p.first);
            queue.pop();
        }

        return ret;
    }
};

class PhotonMap {
private:
    std::vector<Photon> photons;
    KdTree<Photon> kdtree;

public:
    PhotonMap() = default;

    const Photon &getIthPhoton(int i) const { return photons[i]; }
    void setPhotons(std::vector<Photon> &p) {
        this->photons = p;
    }

    const size_t nPhotons() const { return photons.size(); }

    void build() {
#ifdef __OUTPUT__
        std::cout<<"[PhotonMap] photons: "<<photons.size()<<std::endl;
#endif
        kdtree.setPoints(photons.data(), photons.size());
        kdtree.buildTree();
    }

    std::vector<int> queryKNearestPhotons(Vec3f &p, int k, float &max_dist2) const {
        return kdtree.searchKNearest(p, k, max_dist2);
    }
};

#endif
