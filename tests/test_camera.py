from photonmap.libphotonmap_core import *

if __name__ == "__main__":
    width = 512
    height = 512

    camera = Camera(Vec3(0), Vec3(0, 0, -1), 0.5 * PI)

    image = Image(width, height)
    for i in range(height):
        for j in range(width):
            u = (2.0 * j - width) / height
            v = (2.0 * i - height) / height

            ray = Ray()
            pdf = 0
            if camera.sampleRay(Vec2(u, v), ray, pdf):
                image.setPixel(i, j, 0.5 * (ray.direction + 1.0))
            else:
                image.setPixel(i, j, Vec3(0))

    image.writePPM("output.ppm")
