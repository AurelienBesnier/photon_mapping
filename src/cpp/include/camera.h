#ifndef _CAMERA_H
#define _CAMERA_H
#include <cmath>

#include "core.h"

class Camera {
public:
    Camera(
            Vec3f lookfrom,
            Vec3f lookat,
            Vec3f   vup,
            float vfov, // vertical field-of-view in degrees
            float aspect_ratio,
            float aperture,
            float focus_dist
    ) {
        float theta = deg2rad(vfov);
        float h = tan(theta/2);
        float viewport_height = 2.0 * h;
        float viewport_width = aspect_ratio * viewport_height;

        w = normalize(lookfrom - lookat);
        u = normalize(cross(vup, w));
        v = cross(w, u);

        origin = lookfrom;
        horizontal = focus_dist * viewport_width * u;
        vertical = focus_dist * viewport_height * v;
        lower_left_corner = origin - horizontal/2 - vertical/2 - focus_dist*w;

        lens_radius = aperture / 2;
    }


    bool sampleRay(const Vec2f& uv, Ray& ray, float &pdf) const {
        Vec3f rd = lens_radius * random_in_unit_disk();
        Vec3f offset = u * rd[0] + v * rd[1];
        pdf = 1.0f;

        ray = Ray(
                origin + offset,
                lower_left_corner + uv[0]*horizontal + uv[1]*vertical - origin - offset
        );
        return true;
    }

private:
    Vec3f origin;
    Vec3f lower_left_corner;
    Vec3f horizontal;
    Vec3f vertical;
    Vec3f u, v, w;
    float lens_radius;
};

#endif
