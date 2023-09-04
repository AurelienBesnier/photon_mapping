from photonmap import libphotonmap_core
from photonmap.libphotonmap_core import *

from openalea.lpy import *
from openalea.plantgl.all import Tesselator


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
            vertex.append(mvector[1])
            vertex.append(mvector[2])
            vertex.append(mvector[0])
        for k in range(0, maxi + 1):
            nvector = mesh.normalAt(k)
            normals.append(nvector[1])
            normals.append(nvector[2])
            normals.append(nvector[0])

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
        illum = 6  # to use the leaf bxdf
        scene.addFaceInfos(vertex, index, normals, Vec3(r, g, b), Vec3(specular_r, specular_g, specular_b),
                           Vec3(ambient_r, ambient_g, ambient_b), shininess, transparency, illum, 1.0,
                           0.5, 0.5)
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
    light_verts = VectorFloat([5, 50, 4,
                               -5, 50, 4,
                               5, 50, -4])
    light_normals = VectorFloat([0.0, -1.0, 0.0,
                                 0.0, -1.0, 0.0,
                                 0.0, -1.0, 0.0])
    indices = VectorUint([1, 2, 3])
    scene.addLight(light_verts, indices, light_normals, 40, Vec3(1, 1, 1))

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
    width = 256
    height = 256
    n_samples = 10
    n_photons = 10000
    n_estimation_global = 95
    n_photons_caustics_multiplier = 50
    n_estimation_caustics = 50
    final_gathering_depth = 4
    max_depth = 100

    image = libphotonmap_core.Image(width, height)
    camera = libphotonmap_core.Camera(Vec3(0, 20, -25), Vec3(0, 0, 1), 0.5 * PI)

    print("Creating Scene..")
    tr2shmap = {}
    scene = createLpyScene("rose-simple4.lpy", 75, tr2shmap)
    scene.build()
    scene.setupTriangles()

    print(len(scene.getTriangles()))
    print("Done!")

    print("Building photonMap...")
    integrator = PhotonMapping(n_photons, n_estimation_global,
                               n_photons_caustics_multiplier, n_estimation_caustics,
                               final_gathering_depth, max_depth)

    sampler = UniformSampler()

    integrator.build(scene, sampler)
    print("Done!")

    print("Printing photonmap image...")
    visualizePhotonMap(scene, image, width, height, camera, n_photons, max_depth, "photonmap.ppm")
    print("Done!")

    print("Rendering image...")
    image = Image(width, height)
    Render(sampler, image, height, width, n_samples, camera, integrator, scene, "output-photonmapping.ppm")

    compute_energy(tr2shmap, integrator)

    print("Done!")

    print("You did it !")
