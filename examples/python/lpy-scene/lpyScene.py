from photonmap import libphotonmap_core
from photonmap.libphotonmap_core import *

from openalea.lpy import *
from openalea.plantgl.all import Tesselator

def watts_to_emission(w):
    """
    Converts watts to emissive power.
    :param w: the watts to convert.
    :return: the emission strength.
    """
    return w * 2.0 / 10.0

def flatten(lt: list) -> list:
    """
    Flattens a list
    Parameters
    ----------
    lt: list
        a list

    Returns
    ---------
    l: list
        the flattened list

    """
    return [item for sublist in lt for item in sublist]


def addModel(lscene, tr, tr2shmap, scene):
    ctr = 0
    for sh in lscene:
        sh.apply(tr)
        mesh = tr.result
        mesh.computeNormalList()
        indexListSize = mesh.indexListSize()
        vertex = VectorFloat([])
        normals = VectorFloat([])
        ind = []
        maxi = 0
        for i in range(0, indexListSize):
            index = mesh.indexAt(i)
            typeF = mesh.faceSize(i)
            for j in range(0, typeF):
                if index[j] > maxi:
                    maxi = index[j]
        for k in range(0, maxi + 1):
            mvector = mesh.pointAt(k)
            vertex.append(mvector[0])
            vertex.append(mvector[1])
            vertex.append(mvector[2])
        for k in range(0, maxi + 1):
            nvector = mesh.normalAt(k)
            normals.append(nvector[0])
            normals.append(nvector[1])
            normals.append(nvector[2])

        idx = flatten(mesh.indexList)
        for i in idx:
            if len(ind) > 0:
                i += len(ind)
                ctr += 1
        ind.extend(idx)
        index = VectorUint(ind)
        r = float(sh.appearance.diffuseColor().red) / 255.0
        g = float(sh.appearance.diffuseColor().green) / 255.0
        b = float(sh.appearance.diffuseColor().blue) / 255.0
        ambient_r = float(sh.appearance.ambient.red) / 255.0
        ambient_g = float(sh.appearance.ambient.green) / 255.0
        ambient_b = float(sh.appearance.ambient.blue) / 255.0
        shininess = sh.appearance.shininess
        specular_r = float(sh.appearance.specular.red) / 255.0
        specular_g = float(sh.appearance.specular.green) / 255.0
        specular_b = float(sh.appearance.specular.blue) / 255.0
        transparency = sh.appearance.transparency
        illum = 9  # to use the leaf bxdf
        scene.addFaceInfos(vertex, index, normals, Vec3(r, g, b), Vec3(specular_r, specular_g, specular_b),
                           Vec3(ambient_r, ambient_g, ambient_b), shininess, transparency, illum, 1.0,
                           0.5, 0.5, 0.8)
        for _ in mesh.indexList:
            tr2shmap[ctr] = sh.id
            ctr += 1


def createLpyScene(filename: str, t: int, tr2shmap: dict):
    lsystem = Lsystem(filename)
    lstring = lsystem.derive(lsystem.axiom, t)
    lscene = lsystem.sceneInterpretation(lstring)
    scene = libphotonmap_core.Scene()

    # Adding the model of plant
    addModel(lscene, Tesselator(), tr2shmap, scene)

    # Adding a light
    pos = Vec3(float(0), float(0), float(30))
        # print(emission)
    scene.addPointLight(pos, watts_to_emission(56000), Vec3(1,1,1))

    return scene


def compute_energy(tr2shmap, integrator):
    photonmap = integrator.getPhotonMap()
    cPhotonMap = integrator.getPhotonMapC()
    shenergy = {}
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        triId = tr2shmap.get(intersection.triId)
        if triId is not None:  # check if the element hit is an element of the plant
            if triId in shenergy:
                shenergy[triId] += 1
            else:
                shenergy[triId] = 1

    for i in range(cPhotonMap.nPhotons()):
        intersection = cPhotonMap.getIthPhoton(i)
        triId = tr2shmap.get(intersection.triId)
        if triId is not None:  # check if the element hit is an element of the plant
            if triId in shenergy:
                shenergy[triId] += 1
            else:
                shenergy[triId] = 1

    for k, v in shenergy.items():
        print("organ n°" + str(k) + " has " + str(v) + " photons on it")


if __name__ == '__main__':
    width = 512
    height = 512
    n_samples = 5
    n_photons = 10000
    n_estimation_global = 95
    n_photons_caustics_multiplier = 10
    n_estimation_caustics = 10
    final_gathering_depth = 0
    max_depth = 100

    
    aspect_ratio = 4/3
    image_width = 512
    image_height = int(image_width / aspect_ratio)
    image = Image(image_width, image_height)

    lookfrom = Vec3(5, 5, 40)
    lookat = Vec3(0, 0, 0)
    vup = Vec3(0, 0, -1)
    vfov = 25.0
    dist_to_focus = 5.0
    aperture = 0.01

    camera = Camera(
        lookfrom, lookat, vup, vfov, aspect_ratio, aperture, dist_to_focus
    )

    print("Creating Scene..")
    tr2shmap = {}
    scene = createLpyScene("./rose-simple4.lpy", 75, tr2shmap)
    scene.build()
    scene.setupTriangles()

    print("Done!")

    print("Building photonMap...")
    integrator = PhotonMapping(n_photons, n_estimation_global,
                               n_photons_caustics_multiplier, n_estimation_caustics,
                               final_gathering_depth, max_depth)

    sampler = UniformSampler()

    integrator.build(scene, sampler)
    print("Done!")

    print("Printing photonmap image...")
    visualizePhotonMap(
                integrator,
                scene,
                image,
                image_height,
                image_width,
                camera,
                n_photons,
                max_depth,
                "photonmap.ppm",
                sampler,
            )
    print("Done!")

    print("Rendering image...")
    print("Rendering image...")
    image = Image(image_width, image_height)
    Render(
            sampler,
            image,
            image_height,
            image_width,
            n_samples,
            camera,
            integrator,
            scene,
            "output-photonmapping.ppm",
        )
    compute_energy(tr2shmap, integrator)

    print("Done!")

    print("You did it !")
