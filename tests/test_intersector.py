from photonmap.libphotonmap_core import *


if __name__ == "__main__":
    width = 512
    height = 512

    scene = Scene()
    scene.loadModel("cornellbox-water2.obj")
    scene.build()

    camera = Camera(Vec3(0, 1, 7), Vec3(0, 0, -1), 0.25 * PI)

    image = Image(width, height)
    for i in range(height):
        for j in range(width):
            u = (2.0 * j - width) / height
            v = (2.0 * i - height) / height

            ray = Ray()
            pdf = 0.0
            if camera.sampleRay(Vec2(u, v), ray, pdf):
                info = IntersectInfo()
            if scene.intersect(ray, info):
                image.setPixel(i, j, 0.5 * (info.surfaceInfo.shadingNormal + 1.0))
            else:
                image.setPixel(i, j, Vec3(0.0))

    image.writePPM("output.ppm")
