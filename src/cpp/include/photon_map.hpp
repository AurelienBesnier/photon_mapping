#ifndef PHOTON_MAP_H
#define PHOTON_MAP_H

#include <queue>
#include <vector>

#include "core.hpp"

/**
 * @struct Photon
 * @brief Structure representing a Photon.
 */
struct Photon
{
        Vec3f throughput; ///< BxDF * Geometric Term / pdf
        Vec3f position;   ///< The position of the photon in the scene
        Vec3f wi;         ///<  incident direction
        unsigned int triId =
          0; ///<  id of the triangle on which the photon ended up

        // implementation of Point concept
        static constexpr int dim = 3;

        float operator[](int i) const { return position[i]; }

        /**
         * @brief Default Constructor
         */
        Photon() = default;

        /**
         * @brief Parameterized constructor.
         * @param throughput The throughput of the photon.
         * @param position The 3D position of the photon.
         * @param wi the incident direction of the photon.
         * @param triId The id of the triangle on which the photon is on.
         */
        Photon(const Vec3f& throughput,
               const Vec3f& position,
               const Vec3f& wi,
               const unsigned int triId)
          : throughput(throughput)
          , position(position)
          , wi(wi)
          , triId(triId)
        {
        }
};

// Point concept
/*template <typename T>
concept Point = requires(T& x, int i) {
  { T::dim } -> std::convertible_to<int>;  // dimension
  { x[i] } -> std::convertible_to<float>;  // element access
};
*/

/**
 * @brief Compute the squared distance between given points.
 * NOTE: assume PointT and PointU has the same dimension
 * @tparam PointT
 * @tparam PointU
 * @param p1
 * @param p2
 * @return
 */
template<typename PointT, typename PointU>
inline float
distance2(const PointT& p1, const PointU& p2)
{
        float dist2 = 0;
        for (unsigned short i = 0; i < PointT::dim; ++i) {
                dist2 += (p1[i] - p2[i]) * (p1[i] - p2[i]);
        }
        return dist2;
}

/**
 * The kdtree implementation
 * @class KdTree
 * @tparam PointT The type of point in the KdTree
 */
template<typename PointT>
class KdTree
{
      private:
        /**
         * @struct Node
         * @brief Structure representing a node of a KdTree
         */
        struct Node
        {
                int axis;          ///< separation axis(x=0, y=1, z=2)
                int idx;           ///< index of median point
                int leftChildIdx;  ///< index of left child
                int rightChildIdx; ///< index of right child

                Node()
                  : axis(-1)
                  , idx(-1)
                  , leftChildIdx(-1)
                  , rightChildIdx(-1)
                {
                }
        };

        std::vector<Node> nodes; ///< array of tree nodes
        const PointT* points;    ///< pointer to array of points
        int nPoints{};           ///< number of points

        void buildNode(int* indices, int n_points, int depth);

        using KNNQueue = std::priority_queue<std::pair<float, int>>;

        template<typename PointU>
        void searchKNearestNode(int nodeIdx,
                                PointU& queryPoint,
                                int k,
                                KNNQueue& queue) const
        {
                if (nodeIdx == -1 || nodeIdx >= nodes.size())
                        return;

                const Node& node = nodes[nodeIdx];

                // median point
                const PointT& median = points[node.idx];

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
                        searchKNearestNode(
                          node.leftChildIdx, queryPoint, k, queue);
                } else {
                        searchKNearestNode(
                          node.rightChildIdx, queryPoint, k, queue);
                }

                // at leaf node, if size of queue is smaller than k, or queue's
                // largest minimum distance overlaps sibblings region, then
                // search siblings
                const float dist_to_siblings =
                  median[node.axis] - queryPoint[node.axis];
                if (queue.top().first > dist_to_siblings * dist_to_siblings) {
                        if (isLower) {
                                searchKNearestNode(
                                  node.rightChildIdx, queryPoint, k, queue);
                        } else {
                                searchKNearestNode(
                                  node.leftChildIdx, queryPoint, k, queue);
                        }
                }
        }

      public:
        /**
         * @brief Constructor.
         */
        KdTree() = default;

        void setPoints(PointT* points, int nPoints)
        {
                this->points = points;
                this->nPoints = nPoints;
        }

        /**
         * @brief Build the KdTree
         */
        void buildTree();

        template<typename PointU>
        std::vector<int> searchKNearest(PointU& queryPoint,
                                        int k,
                                        float& maxDist2) const
        {
                KNNQueue queue;
                searchKNearestNode(0, queryPoint, k, queue);

                std::vector<int> ret(queue.size());
                maxDist2 = 0;
                for (int& i : ret) {
                        const std::pair<float, int>& p = queue.top();
                        i = p.second;
                        maxDist2 = std::max(maxDist2, p.first);
                        queue.pop();
                }

                return ret;
        }
};

/**
 * Class representing a photon map
 * @class PhotonMap
 */
class PhotonMap
{
      private:
        std::vector<Photon> photons; ///< the photons in the photonmap.
        KdTree<Photon>
          kdtree; ///< kdtree structure with the position of the photons.

      public:
        /**
         * @brief Constructor
         */
        PhotonMap() = default;

        /**
         * @brief Destructor
         */
        virtual ~PhotonMap() = default;

        /**
         * @brief Get the ith photon of the photon map
         * Retrieves the ith photon in the photons member vector.
         * @param i the index of the photon to get
         * @return the photon in question.
         */
        const Photon& getIthPhoton(int i) const;

        /**
         * @fn void setPhotons(const std::vector<Photon> &p)
         * Sets the photons class member to the given vector.
         * @param p the vector to set.
         */
        void setPhotons(const std::vector<Photon>& p);

        /**
         * @fn const size_t nPhotons() const
         * @brief returns the number of photons.
         * @return the number of photons.
         */
        const size_t nPhotons() const;

        /**
         * @fn void build()
         * @brief Builds the Photon Map.
         * Builds the Kdtree member of the PhotonMap.
         */
        void build();

        /**
         * @fn std::vector<int> queryKNearestPhotons(Vec3f &p, int k, float
         * &max_dist2) const
         * @brief Get the k nearest photons to one given photon.
         * @param p the targeted photon.
         * @param k the number of neighbors to get.
         * @param max_dist2 the maximum of distance get get the neighbors.
         * @return a vector with the indices of the nearest photons.
         */
        std::vector<int> queryKNearestPhotons(Vec3f& p,
                                              int k,
                                              float& max_dist2) const;
};

#endif
