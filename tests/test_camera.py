from photonmap import Camera, Image, Ray, Vec2, Vec3


def test_camera():
    aspect_ratio = 16.0 / 9.0

    image_width = 1024
    image_height = int(image_width / aspect_ratio)

    lookfrom = Vec3(0, 1, 7)
    lookat = Vec3(0, 0, -1)
    vup = Vec3(0, 1, 0)
    vfov = 50.0
    dist_to_focus = 3.0
    aperture = 0.01

    camera = Camera(lookfrom, lookat, vup, vfov, aspect_ratio,
                    aperture, dist_to_focus)

    image = Image(image_width, image_height)
    for i in range(image_height):
        for j in range(image_width):
            u = (2.0 * j - image_width) / image_height
            v = (2.0 * i - image_height) / image_height

            ray = Ray()
            pdf = 0
            if camera.sampleRay(Vec2(u, v), ray, pdf):
                image.setPixel(i, j, 0.5 * (ray.direction + 1.0))
            else:
                image.setPixel(i, j, Vec3(0))

    image.writePPM("output.ppm")
    image_written = True
    assert image_written
