#ifndef CAMERA_H
#define CAMERA_H

#include <cmath>

#include "core.hpp"
#include "scene.hpp"

/**
 * @brief Class representing the camera.
 * @class Camera
 * @author Aurelien Besnier
 */
class Camera {
public:
    /**
     * @brief ConstructorScene&
     *
     * Constructor of the Camera class.
     * @param lookfrom the position of the camera.
     * @param lookat the 3d point the camera is looking at.
     * @param vup the Up vector of the camera.
     * @param vfov the vertical fov of the camera.
     * @param aspect_ratio the aspect radio of the image to render.
     * @param aperture the aperture of the camera.
     * @param focus_dist the focus distance of the camera (depth of field).
     */
    Camera(Vec3f lookfrom, Vec3f lookat, Vec3f vup,
           float vfov, // vertical field-of-view in degrees
           float aspect_ratio, float aperture, float focus_dist) {
        float theta = deg2rad(vfov);
        float h = tan(theta / 2);
        float viewport_height = 2.0f * h;
        float viewport_width = aspect_ratio * viewport_height;

        w = normalize(lookfrom - lookat);
        u = normalize(cross(vup, w));
        v = cross(w, u);

        origin = lookfrom;
        horizontal = focus_dist * viewport_width * u;
        vertical = focus_dist * viewport_height * v;
        lower_left_corner = origin - horizontal / 2 - vertical / 2 - focus_dist * w;

        lens_radius = aperture / 2;
    }

    /**
     * @fn bool sampleRay(const Vec2f &uv, Ray &ray, float &pdf) const
     * @brief Samples a point in the image to render from the camera view point.
     * @param uv the Image pixel coordinates.
     * @param ray The reference for a ray to trace.
     * @param pdf
     * @return true if the ray intersects with the scene.
     */
	bool sampleRay(const Vec2f &uv, Ray &ray, float &pdf, const Scene& scene) const {
        Vec3f rd = lens_radius * random_in_unit_disk();
        Vec3f offset = u * rd[0] + v * rd[1];
        pdf = 1.0f;

        ray = Ray(origin + offset, lower_left_corner + uv[1] * horizontal +
                                   uv[0] * vertical - origin - offset);
        IntersectInfo info;
        return scene.intersect(ray, info); // Check if the ray intersects with the scene
    }

    /**
     * @fn bool sampleRay(const Vec2f &uv, Ray &ray, float &pdf) const
     * @brief Samples a point in the image to render from the camera view point.
     * @param uv the Image pixel coordinates.
     * @param ray The reference for a ray to trace.
     * @param pdf
     * @return true if sampling success.
     */
	bool sampleRay(const Vec2f &uv, Ray &ray, float &pdf) const {
        Vec3f rd = lens_radius * random_in_unit_disk();
        Vec3f offset = u * rd[0] + v * rd[1];
        pdf = 1.0f;

        ray = Ray(origin + offset, lower_left_corner + uv[1] * horizontal +
                                   uv[0] * vertical - origin - offset);
        return true;
    }

private:
    Vec3f origin; ///< the position of the camera
    Vec3f lower_left_corner;  ///< the lower left corner of the image from the camera point of view.
    Vec3f horizontal;
    Vec3f vertical;
    Vec3f u, v, w;
    float lens_radius; ///< the lens radius of the camera's objective.
};

#endif
