import re
import sys
from datetime import datetime
import random

from openalea.lpy import Lsystem
from openalea.plantgl.all import *
from photonmap.libphotonmap_core import Vec3, VectorUint, VectorFloat, PhotonMapping, UniformSampler, \
    visualizePhotonMap, Render, Camera, PI

from photonmap import libphotonmap_core


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


def denormalize(f: float) -> int:
    return int(255 * f)


def addModel(lscene, tr, tr2shmap, sc: libphotonmap_core.Scene, anchor: Vec3):
    ctr = 0
    for sh in lscene:
        sh.apply(tr)
        mesh = tr.result
        mesh.computeNormalList()
        indexListSize = mesh.indexListSize()
        vertices = VectorFloat([])
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
            vertices.append(mvector[0] / 10 + anchor[0])
            vertices.append(mvector[2] / 10 + anchor[1])
            vertices.append(mvector[1] / 10 + anchor[2])
        for k in range(0, maxi + 1):
            nvector = mesh.normalAt(k)
            normals.append(nvector[0])
            normals.append(nvector[2])
            normals.append(nvector[1])

        idx = flatten(mesh.indexList)
        for i in idx:
            if len(ind) > 0:
                i += len(ind)
                ctr += 1
        ind.extend(idx)
        indices = VectorUint(ind)
        r = float(sh.appearance.diffuseColor().red) / 255.0
        g = float(sh.appearance.diffuseColor().green) / 255.0
        b = float(sh.appearance.diffuseColor().blue) / 255.0
        diffuse = Vec3(r, g, b)
        ambient_r = float(sh.appearance.ambient.red) / 255.0
        ambient_g = float(sh.appearance.ambient.green) / 255.0
        ambient_b = float(sh.appearance.ambient.blue) / 255.0
        ambient = Vec3(ambient_r, ambient_g, ambient_b)
        shininess = sh.appearance.shininess
        specular_r = float(sh.appearance.specular.red) / 255.0
        specular_g = float(sh.appearance.specular.green) / 255.0
        specular_b = float(sh.appearance.specular.blue) / 255.0
        specular = Vec3(specular_r, specular_g, specular_b)
        transparency = sh.appearance.transparency
        illum = 9  # to use the leaf bxdf

        sc.addFaceInfos(vertices, indices, normals, diffuse, ambient, specular, shininess, transparency, illum, 1,
                        1 - transparency, transparency, 1.0 - shininess)

        for _ in mesh.indexList:
            tr2shmap[ctr] = sh.id
            ctr += 1


def addLpyFileToScene(sc: libphotonmap_core.Scene, filename: str, t: int, tr2shmap: dict, anchor: Vec3):
    lsystem = Lsystem(filename)
    lstring = lsystem.derive(lsystem.axiom, t)
    lscene = lsystem.sceneInterpretation(lstring)

    # Adding the model of plant
    addModel(lscene, Tesselator(), tr2shmap, sc, anchor)

    return sc


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


def read_rad(file: str):
    with open(file, 'r') as f:
        lines = f.readlines()
        materials = {}
        shapes = {}
        sc = Scene()
        anchor = Vec3(0, 0, 0)
        i = 0
        for _ in range(len(lines)):
            i += 1
            if i >= len(lines):
                break
            elif lines[i].startswith("#"):
                continue
            elif lines[i].startswith("void"):  # material
                li = lines[i].split(" ")
                type = li[1]
                name = li[2].strip("\n")
                # print("material name: " + str(name))
                if materials.get(name) is None:
                    if type == "plastic":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        spec = Color3(denormalize(float(li[3])), denormalize(float(li[3])), denormalize(float(li[3])))
                        roughness = float(li[4])
                        mat = {"name": name, "type": type, "color": color, "spec": spec, "roughness": roughness}
                        materials[name] = mat
                        i += 5
                    elif type == "metal":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        spec = Color3(denormalize(float(li[3])), denormalize(float(li[3])), denormalize(float(li[3])))
                        roughness = float(li[4])
                        mat = {"name": name, "type": type, "color": color, "spec": spec, "roughness": roughness}
                        materials[name] = mat
                        i += 5
                    elif type == "trans":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        spec = Color3(denormalize(float(li[3])), denormalize(float(li[3])), denormalize(float(li[3])))
                        roughness = float(li[4])
                        trans = float(li[5])
                        tspec = float(li[6])
                        mat = {"name": name, "type": type, "color": color, "spec": spec, "roughness": roughness,
                               "trans": trans, "tspec": tspec}
                        materials[name] = mat
                        i += 5
                    elif type == "light":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        mat = {"type": type, "color": color}
                        materials[name] = mat
                        i += 5
            else:
                keys = materials.keys()
                for k in keys:
                    if lines[i].startswith(k):
                        li = lines[i].split(" ")
                        material = li[0]
                        type = li[1]
                        name = li[2].strip("\n")
                        i += 3
                        vert = []
                        size = int(lines[i])
                        tmp = i + 1
                        nbCoords = int(size / 3)
                        if nbCoords > 2:
                            if "type" == "cylinder":
                                l = re.split(r"\s+|;+", lines[0])
                                l2 = re.split(r"\s+|;+", lines[1])
                                l3 = re.split(r"\s+|;+", lines[2])
                                x, y, z = float(l[0]) / 100.0, float(l[2]) / 100.0, float(l[1]) / 100.0
                                x2, y2, z2 = (float(l2[0]) / 10.0, float(l2[2]) / 100.0, float(l2[1]) / 100.0)
                                vert.append((x, y, z))
                                vert.append((x2, y2, z2))
                                for i in range(nbCoords):
                                    vert.append((x, y, z))

                                shapes[name] = {"vertices": vert, "type": type, "size": size, "material": material}
                            else:
                                for j in range(tmp, tmp + nbCoords):
                                    l = re.split(r"\s+|;+", lines[j])
                                    #print(name)
                                    vert.append((float(l[0]) / 100.0, float(l[2]) / 100.0, float(l[1]) / 100.0))
                                    i = j
                                    shapes[name] = {"vertices": vert, "type": type, "size": size, "material": material}
                        if name == "anchor":
                            print("anchor found")
                            anchor = vert[0]
                            print(anchor)
        for sh, val in shapes.items():
            mat_key = val["material"]
            mat = materials[mat_key]
            # print("material: " + str(mat))
            vert = val["vertices"]
            s = Shape()
            nbCoords = int(val["size"] / 3)
            if nbCoords % 3 == 0:
                ts = TriangleSet(vert)
                i = 0
                indList = []
                while i < nbCoords:
                    ind = Index3(i, i + 2, i + 1)
                    indList.append(ind)
                    i += 3
                ts.indexList = Index3Array(indList)
                ts.computeNormalList()
                s.geometry = ts
                s.name = sh
                if mat["type"] == "light":
                    s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                            emission=Color3(mat["color"]))

                elif mat["type"] == "trans":
                    s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                            specular=Color3(mat["spec"]),
                                            shininess=1 - mat["roughness"], transparency=mat["trans"])
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                shininess=1 - mat["roughness"])
                    else:
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                specular=Color3(mat["spec"]), shininess=1 - mat["roughness"])
                s.appearance.name = mat["name"]
                sc.add(s)
            else:
                ts = TriangleSet(vert)
                i = 0
                indList = []
                while i < nbCoords:
                    ind = Index3(i, i + 2, i + 1)
                    ind2 = Index3(i, i + 3, i + 2)
                    indList.append(ind)
                    indList.append(ind2)
                    i += 4
                ts.indexList = Index3Array(indList)
                ts.computeNormalList()
                s.geometry = ts
                s.name = sh
                if mat["type"] == "light" or s.name.startswith("ref"):
                    s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                            emission=Color3(mat["color"]))
                elif mat["type"] == "trans":
                    s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                            specular=Color3(mat["spec"]),
                                            shininess=1 - mat["roughness"], transparency=mat["trans"])
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                shininess=1 - mat["roughness"])
                    else:
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                specular=Color3(mat["spec"]), shininess=1 - mat["roughness"])
                s.appearance.name = mat["name"]
                sc.add(s)
        sc.save("env.obj")
        return sc, anchor


def watts_to_emission(w):
    return w * 2.0 / 10.0


def add_shape(scene: libphotonmap_core.Scene, sh: Shape):
    normals = VectorFloat(flatten(sh.geometry.normalList))
    indices = VectorUint(flatten(sh.geometry.indexList))
    vertices = VectorFloat(flatten(sh.geometry.pointList))
    ambient = Vec3(sh.appearance.ambient.red / 255.0, sh.appearance.ambient.green / 255.0,
                   sh.appearance.ambient.blue / 255.0)
    specular = Vec3(sh.appearance.specular.red / 255.0, sh.appearance.specular.green / 255.0,
                    sh.appearance.specular.blue / 255.0)
    diffuse = ambient
    trans = sh.appearance.transparency
    illum = 1
    shininess = sh.appearance.shininess
    emission = sh.appearance.emission
    if emission != Color3(0, 0, 0):
        pos = Vec3(vertices[0], vertices[1], vertices[2])
        # scene.addLight(vertices, indices, normals, watts_to_emission(18), ambient)
        scene.addPointLight(pos, watts_to_emission(1000), Vec3(1, 1, 1))

        scene.addFaceInfos(vertices, indices, normals, diffuse, ambient, specular, shininess,
                           trans, illum, 1, 1 - trans, trans, 1.0 - shininess)
    else:
        scene.addFaceInfos(vertices, indices, normals, diffuse, ambient, specular, shininess,
                           trans, illum, 1, 1 - trans, trans, 1.0 - shininess)


def addCaptor():
    with open("captor.obj", 'r') as f:
        print("")


def photonmap_plantglScene(sc, anchor):
    scene = libphotonmap_core.Scene()
    for sh in sc:
        add_shape(scene, sh)
    tr2shmap = {}
    # scene.addSpotLight(Vec3(12, 12, 7), watts_to_emission(18), Vec3(1, 1, 1),
    #                   Vec3(0.4, -0.4, 1), 20)
    addLpyFileToScene(scene, "rose-simple4.lpy", 150, tr2shmap, anchor)

    width = 512
    height = 512
    n_samples = 5
    n_photons = 1000
    n_estimation_global = 100
    n_photons_caustics_multiplier = 2
    n_estimation_caustics = 15
    final_gathering_depth = 0
    max_depth = 100

    image = libphotonmap_core.Image(width, height)
    camera = libphotonmap_core.Camera(Vec3(12, 12, 2), Vec3(0.4, -0.4, 1), 0.75 * PI)

    scene.build()
    scene.setupTriangles()

    print("Building photonMap...")
    integrator = PhotonMapping(n_photons, n_estimation_global,
                               n_photons_caustics_multiplier, n_estimation_caustics,
                               final_gathering_depth, max_depth)

    sampler = UniformSampler(random.randint(1, sys.maxsize))

    integrator.build(scene, sampler)
    print("Done!")

    print("Printing photonmap image...")
    visualizePhotonMap(scene, image, width, height, camera, n_photons, max_depth, "photonmap.ppm")
    print("Done!")

    print("Rendering image...")
    image = libphotonmap_core.Image(width, height)
    Render(sampler, image, height, width, n_samples, camera, integrator, scene, "output-photonmapping.ppm")

    compute_energy(tr2shmap, integrator)

    print("Done!")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


if __name__ == "__main__":
    sc, anchor = read_rad("./chambre2.rad")
    #photonmap_plantglScene(sc, anchor)
