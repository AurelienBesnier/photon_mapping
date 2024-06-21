import bisect
from collections import OrderedDict
import gc
from math import cos, sin, pi
import os
import random
import re
import sys
import time
import pandas as pd

from openalea.plantgl.all import * 
from scipy.integrate import simpson
from scipy.spatial import Delaunay

from openalea.lpy import Lsystem
from photonmap import (
    Vec3,
    VectorUint,
    VectorFloat,
    PhotonMapping,
    UniformSampler,
)
from photonmap import libphotonmap_core
from photonmap.libphotonmap_core import (
    Render,
    visualizePhotonMap,
    visualizeCausticsPhotonMap,
    visualizeCaptorsPhotonMap,
)


def get_integral_of_band(band: range, spectrum: dict) -> float:
    """
    Returns the integral of the band as a percentage
    Parameters
    ----------
    band: range
        The section of the spectrum to get.
    spectrum: dict
        The whole spectrum of the band.

    Returns
    -------

    """
    spec_range = []
    for i in band:
        spec_range.append(spectrum[i])
    I_simps = simpson(y=spec_range, x=None, axis=-1)

    return I_simps / 100  # get as percentage


def correct_energy(shenergy: dict, correction_ratio):
    """
    Correct the energy computed during the simulation  with the integral of the chosen spectrum band.
    Parameters
    ----------
    shenergy: dict

    Returns
    -------

    """
    for k, v in shenergy.items():
        shenergy[k] = int(v * correction_ratio)


def setup_dataset_materials(w_start: int, w_end: int):
    """
    Fills the materialsR and materialsT dictionaries with information from the provided data for the materials of
    the simulation.
    Parameters
    ----------
    w_start: int
        The first wavelength of band.
    w_end: int
        The last wavelength of band.

    Returns
    -------

    """
    materialsT = {}
    materialsS = {}
    materialsR = {}

    for element in ("Plant", "Env"):  # Reflectances
        files = []
        dir_pathReflect = (
            os.path.dirname(__file__) + "/PO/" + element + "/ReflectancesMean/"
        )
        for path in os.listdir(dir_pathReflect):
            if os.path.isfile(os.path.join(dir_pathReflect, path)):
                if not path.startswith("."):
                    files.append(path)
        for file in files:
            matName = file.split(".")[0]
            contentReflect, stepReflect, startReflect = read_spectrum_file(
                os.path.join(dir_pathReflect, file)
            )
            
            refl = get_average_of_props(range(w_start, w_end, 1), contentReflect)
            
            materialsR[matName] = (
                float(refl)
                if float(refl) > 0
                else 0.0
            )

    for element in ("Plant", "Env"):  # Transmittances
        files = []
        dir_pathTransmit = (
            os.path.dirname(__file__) + "/PO/" + element + "/TransmittancesMean/"
        )
        for path in os.listdir(dir_pathTransmit):
            if os.path.isfile(os.path.join(dir_pathTransmit, path)):
                if not path.startswith("."):
                    files.append(path)
        for file in files:
            matName = file.split(".")[0]
            contentTransmit, stepTransmit, startTransmit = read_spectrum_file(
                os.path.join(dir_pathTransmit, file)
            )

            trans = get_average_of_props(range(w_start, w_end, 1), contentTransmit)
            
            materialsT[matName] = (
                float(trans)
                if float(trans) > 0
                else 0.0
            )

    #Specularities
    dir_pathSpec = (os.path.dirname(__file__) + "/PO/Specularities.xlsx")
    contentSpec = (pd.ExcelFile(dir_pathSpec)).parse(0)
    mat_names = contentSpec["Materiau"]
    mat_spec = contentSpec["Valeur estimee visuellement"]
    
    for i in range(len(mat_spec)):
        materialsS[mat_names[i]] = (
            float(mat_spec[i])
            if float(mat_spec[i]) > 0
            else 0.0
        )


    return materialsR, materialsS, materialsT


def wavelength2Rgb(w: int) -> Vec3:
    """
    Convert a wavelength between 400 - 800 nm to RGB color
    Parameters
    ----------
    w: int
        The wavelength to convert

    Returns
    -------
    RGB: Vec3
        A Vec3 structure representing an RGB color.

    """
    if 380.0 <= w < 440:
        red = -(w - 440.0) / (440.0 - 380.0)
        green = 0.0
        blue = 1.0
    elif 440.0 <= w < 490.0:
        red = 0.0
        green = (w - 440.0) / (490.0 - 440.0)
        blue = 1.0
    elif 490.0 <= w < 510.0:
        red = 0.0
        green = 1.0
        blue = -(w - 510.0) / (510.0 - 490.0)
    elif 510.0 <= w < 580.0:
        red = (w - 510.0) / (580.0 - 510.0)
        green = 1.0
        blue = 0.0
    elif 580.0 <= w < 645.0:
        red = 1.0
        green = -(w - 645.0) / (645.0 - 580.0)
        blue = 0.0
    elif 645.0 <= w < 781.0:
        red = 1.0
        green = 0.0
        blue = 0.0
    else:
        red = 0.0
        green = 0.0
        blue = 0.0

    return Vec3(red, green, blue)


def get_average_of_band(band: range, spectrum: dict) -> int:
    """
    Get the wavelength that represent the average of the count of photon send in a band of the spectrum of the light.
    Parameters
    ----------
    band: range
        The range of wavelength to compute the average of photon to send.
    spectrum: dict
        a dictionary representing the spectrum of the light with a wavelength as the key and a count of photons as the
        value.

    Returns
    -------
    wavelength: int
        The wavelength in question.
    """
    cpt: int = 0
    counts: float = 0.0
    b_dict: dict = {}
    for i in band:  # first for to get the average
        counts += spectrum[i]
        b_dict[i] = spectrum[i]
        cpt += 1
    avg = counts / cpt
    # get the closest wavelength of that average
    res_key, res_val = min(b_dict.items(), key=lambda x: abs(avg - x[1]))
    return res_key


def get_average_of_props(band: range, props: dict) -> float:
    res = 0.0
    count = 0
    for i in band:
        res += props[i]
        count += 1
    
    res /= count
    return res

def read_spectrum_file(filename: str) -> (OrderedDict, int, int):
    """
    Parse a spectrum file.
    Parameters
    ----------
    filename: str
        The file to parse.

    Returns
    -------
    content: dict
        A dictionary with wavelength as key and photon count as value.
    step: int
        the step in the dictionary between two entries.
    start: int
        the first wavelength in the file.
    """
    content = OrderedDict()
    cpt_comment = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] != '"':  # ignore comment
                ls = re.split(r"\s+|;+", line, maxsplit=1)
                content[int(ls[0])] = float(ls[1].replace(",", "."))
            else:
                cpt_comment += 1
        first_line = re.split(r"\s+|;+", lines[cpt_comment], maxsplit=1)
        second_line = re.split(r"\s+|;+", lines[cpt_comment + 1], maxsplit=1)
        step = int(second_line[0]) - int(first_line[0])
    return content, step, int(first_line[0])


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

def sphericalToCartesian(theta, phi, x_seg, y_seg):
    theta = theta * pi / 2 / y_seg
    phi = phi * 2 * pi / x_seg
    return Vector3(cos(phi) * sin(theta), cos(theta), sin(phi) * sin(theta))

def crossVector(a, b):
    res = Vector3(0,0,0)
    res[0] = a[1] * b[2] - b[1] * a[2]
    res[1] = - a[0] * b[2] + b[0] * a[2]
    res[2] = a[0] * b[1] - b[0] * a[1] 
    return res

def orthonormalBasis(n):
    t = Vector3(0,0,0)
    b = Vector3(0,0,0)

    if abs(n[1]) < 0.9:
        t = crossVector(n, Vector3(0, 1, 0))
    else:
        t = crossVector(n, Vector3(0, 0, -1))
    
    t.normalize()
    b = crossVector(t, n)
    b.normalize()

    return t, b 

def geoHemisphere(centre, normal, rayon):
    vertices = []
    triangles = []
    normals = []

    x_segment = 10
    y_segment = 5
   
    for i in range(y_segment):
        theta = i * pi / 2 / y_segment
        for j in range(x_segment):
            phi = j * 2 * pi / x_segment
            v1 = sphericalToCartesian(i, j, x_segment, y_segment)
            v2 = sphericalToCartesian(i, j + 1, x_segment, y_segment)
            v3 = sphericalToCartesian(i + 1, j, x_segment, y_segment)
            v4 = sphericalToCartesian(i + 1, j + 1, x_segment, y_segment)
            #add vert
            v_count = len(vertices)
            vertices.append(v1)
            vertices.append(v2)
            vertices.append(v3)
            vertices.append(v4)
            
            #add normal:: normals et vertices sont egaux car c'est une sphere unité
            normals.append(v1)
            normals.append(v2)
            normals.append(v3)
            normals.append(v4)

            #add triangle
            triangles.append(Index3(v_count, v_count + 1, v_count + 2))
            triangles.append(Index3(v_count + 1, v_count + 2, v_count + 3))

    #apply transform
    t, b = orthonormalBasis(normal)
    for i, v in enumerate(vertices):
        v_r = Vector3(0,0,0)
        v_r[0] = v[0] * t[0] + v[1] * normal[0] + v[2] * b[0]
        v_r[1] = v[0] * t[1] + v[1] * normal[1] + v[2] * b[1]
        v_r[2] = v[0] * t[2] + v[1] * normal[2] + v[2] * b[2]
        vertices[i] = rayon * v_r + centre

    return Shape(TriangleSet(vertices, triangles, normals))
    

def averageVector(listVectors):
    sum = Vector3(0,0,0)
    for v in listVectors:
        sum = sum + v
    
    sum = sum / len(listVectors)

    return sum




def addLightDirectionPgl(sc, scale_factor):
    pglScene = Scene()
    
    for sh in sc:
        vertices = sh.geometry.pointList
        normals = sh.geometry.normalList
        if len(vertices) == 4:
            centre = averageVector(vertices)
            normal = averageVector(normals)
            normal.normalize()
            rayon = 50 * scale_factor
          
            sh_dir = geoHemisphere(centre, normal, rayon)
            sh_dir.appearance.ambient = Color3(1,0,0)
            
            pglScene.add(sh_dir)

    return Scene([pglScene, sc])

def addCapteurPgl(sc, scale_factor: int, filename: str):
    pglScene = Scene()

    with open(filename, "r") as f:
        next(f)
        captorId = 0
        for line in f:
            row = line.split(",")
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])
            r = float(row[3])
            xnorm = float(row[4])
            ynorm = float(row[5])
            znorm = float(row[6])
            pos = [x / scale_factor, y / scale_factor, z / scale_factor]
            normal = [xnorm, ynorm, znorm]
            r = r / scale_factor
            vertices = []
            normals = []
            triangles = []

            val = 3.14285 / 180
            deltaAngle = 45

            vertices.append(Vector3(pos[0], pos[1], pos[2]))
            normals.append(Vector3(normal[0], normal[1], normal[2]))
 
            triangleCount = 0
            if znorm == 1:
                x1 = r * cos(0)
                y1 = r * sin(0)
                z1 = 0
            else:
                x1 = r * cos(0)
                y1 = 0
                z1 = r * sin(0)
            point1 = [x1 + pos[0], y1 + pos[1], z1 + pos[2]]
    
            vertices.append(Vector3(point1[0], point1[1], point1[2]))
            normals.append(Vector3(normal[0], normal[1], normal[2]))
            i = 0
            while i < 359:
                if znorm == 1:
                    x2 = r * cos((i + deltaAngle) * val)
                    y2 = r * sin((i + deltaAngle) * val)
                    z2 = 0
                else:
                    x2 = r * cos((i + deltaAngle) * val)
                    y2 = 0
                    z2 = r * sin((i + deltaAngle) * val)

                point2 = [x2 + pos[0], y2 + pos[1], z2 + pos[2]]
                vertices.append(Vector3(point2[0], point2[1], point2[2]))
                normals.append(Vector3(normal[0], normal[1], normal[2]))
                triangles.append( Index3(triangleCount + 1, triangleCount + 2, 0) )

                triangleCount += 1
                i += deltaAngle

            tmpSh= Shape(TriangleSet(vertices, triangles, normals))
            tmpSh.appearance.ambient = Color3(1,0,0)
            pglScene.add(tmpSh)

    return Scene([pglScene, sc])

def addModelPgl(lscene, tr, sc, anchor: Vec3, scale_factor, shenergy: dict):
    max_energy = shenergy[max(shenergy, key=shenergy.get)]
    ctr = 0
    pglScene = Scene()
    for sh in lscene:
        sh.apply(tr)
        mesh = tr.result
        mesh.computeNormalList()
        indexListSize = mesh.indexListSize()
        vertices = []
        maxi = 0
        for i in range(0, indexListSize):
            index = mesh.indexAt(i)
            typeF = mesh.faceSize(i)
            for j in range(0, typeF):
                if index[j] > maxi:
                    maxi = index[j]
        for k in range(0, maxi + 1):
            mvector = mesh.pointAt(k)
            vertices.append(Vector3((mvector[0] / (scale_factor / 10) + anchor[0]),
                            (mvector[1] / (scale_factor / 10) + anchor[1]),
                            (mvector[2] / (scale_factor / 10) + anchor[2])),
                            )

        idx = mesh.indexList
        
        tmpSh= Shape(TriangleSet(vertices, idx, mesh.normalList))
        #tmpSh.appearance = sh.appearance

        cur_sh_energy = 0
        if sh.id in shenergy:
            cur_sh_energy = shenergy[sh.id]

        ratio = cur_sh_energy / max_energy
        r = (int)(255 * ratio) 
        g = (int)(255 * ratio) 
        b = (int)(255 * ratio) 
        tmpSh.appearance = Material(ambient=Color3(r,g,b), diffuse=sh.appearance.diffuse)

        pglScene.add(tmpSh)


    return Scene([pglScene, sc])

def addModel(
    lscene, tr, tr2shmap, sc: libphotonmap_core.Scene, anchor: Vec3, scale_factor
):
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
            vertices.append(mvector[0] / (scale_factor / 10) + anchor[0])
            vertices.append(mvector[1] / (scale_factor / 10) + anchor[1])
            vertices.append(mvector[2] / (scale_factor / 10) + anchor[2])
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
        illum = 8  # to use the leaf bxdf

        refl = (r + g + b) / 3
        spec = (specular_r + specular_g + specular_b) / 3
        

        sc.addFaceInfos(
            vertices,
            indices,
            normals,
            diffuse,
            ambient,
            spec,
            shininess,
            transparency,
            illum,
            sh.name,
            1,
            refl,
            transparency,
            1.0 - shininess,
        )

        for _ in mesh.indexList:
            tr2shmap[ctr] = sh.id
            ctr += 1


def add_lpy_file_to_scene(
    sc: libphotonmap_core.Scene,
    filename: str,
    t: int,
    tr2shmap: dict,
    anchor: Vec3,
    scale_factor,
):
    """
    Adds the lpy mesh to the photonmapping scene.
    :param sc:
    :param filename:
    :param t:
    :param tr2shmap:
    :param anchor:
    :param scale_factor:
    :return:
    """
    lsystem = Lsystem(filename)
    #lstring = lsystem.derive(lsystem.axiom, 150)
    #lscene = lsystem.sceneInterpretation(lstring)

    # Adding the model of plant
    #addModel(lscene, Tesselator(), tr2shmap, sc, anchor, scale_factor)


def write_captor_energy(energy, w_start, w_end, n_photons, nb_exp):
    od = OrderedDict(sorted(energy.items()))
    band = str(w_start) + "-" + str(w_end)

    filename = "results/captor_result-" + str(n_photons) + "-" + str(band) + "-nm.csv"

    with open(filename, "w") as f:
        f.write("id,n_photons,elevation\n")
        for k, v in od.items():
            if k <= 119:
                elevation = 1000
            elif k <= 239:
                elevation = 1400
            else:
                elevation = 1800
            print("captor n°" + str(k) + " has " + str(v / nb_exp) + " photons on it")
            f.write(str(k) + "," + str(v / nb_exp) + "," + str(elevation) + "\n")

    print("Done!")


def captor_add_energy(captor_dict, integrator, energy):
    """
    Compute the energy on each captor in the scene.
    :param energy:
    :param captor_dict:
    :param integrator:
    :return:
    """
    photonmap = integrator.getPhotonMapCaptors()
    print(photonmap.nPhotons())
    print("writing captor energy...")
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        captorId = captor_dict.get(intersection.triId)
        if captorId is None:
            print(captorId)

        if captorId is not None:  # check if the element hit is a captor
            if captorId in energy:
                energy[captorId] += 1
            else:
                energy[captorId] = 1


def compute_energy(tr2shmap, integrator):
    """
    Computes the number of photons on each organ of the plant.
    :param tr2shmap:
    :param integrator:
    :return:
    """
    photonmap = integrator.getPhotonMapCaptors()
    shenergy = {}
    for i in range(photonmap.nPhotons()):
        intersection = photonmap.getIthPhoton(i)
        triId = tr2shmap.get(intersection.triId)
        if triId is not None:  # check if the element hit is an element of the plant
            if triId in shenergy:
                shenergy[triId] += 1
            else:
                shenergy[triId] = 1

    for k, v in shenergy.items():
        print("organ n°" + str(k) + " has " + str(v) + " photons on it")
    
    return shenergy


def cylinder_vertices(start, end, rayon):
    vert = []
    direction = end - start
    direction.normalize()
    horizontal = crossVector(direction, Vector3(0,0,1))
    
    
    v1 = end + rayon * horizontal
    v2 = start + rayon * horizontal
    v3 = start - rayon * horizontal
    v4 = end - rayon * horizontal

    vert.append((v1[0], v1[1], v1[2]))
    vert.append((v2[0], v2[1], v2[2]))
    vert.append((v3[0], v3[1], v3[2]))
    vert.append((v4[0], v4[1], v4[2]))

    return vert

def read_rad(file: str, invert_normals: bool):
    """
    Parse a radiance file (https://radsite.lbl.gov/radiance/framed.html) a make a plantGL Scene
    :param file: the rad filename
    :param invert_normals: whether to invert the normals or not.
    :return: A plantGL Scene.
    """
    with open(file, "r") as f:
        lines = f.readlines()
        materials = {}
        shapes = {}
        sc = Scene()
        anchor = Vec3(0, 0, 0)
        i = 0
        scale_factor = 1
        for _ in range(len(lines)):
            i += 1
            if i >= len(lines):
                break
            elif lines[i].startswith("#"):
                continue
            elif lines[i].startswith("scale_factor"):
                li = lines[i].split(None)
                scale_factor = float(li[1])
            elif lines[i].startswith("void"):  # material
                li = lines[i].split(None)
                type = li[1]
                name = li[2].strip("\n")
                # print("material name: " + str(name))
                if materials.get(name) is None:
                    if type == "plastic":
                        li = lines[i + 4].split(None)
                        color = Color3(
                            denormalize(float(li[0])),
                            denormalize(float(li[1])),
                            denormalize(float(li[2])),
                        )
                        spec = Color3(
                            denormalize(float(li[3])),
                            denormalize(float(li[3])),
                            denormalize(float(li[3])),
                        )
                        roughness = float(li[4])
                        mat = {
                            "name": name,
                            "type": type,
                            "color": color,
                            "spec": spec,
                            "roughness": roughness,
                        }
                        materials[name] = mat
                        i += 5
                    elif type == "metal":
                        li = lines[i + 4].split(None)
                        color = Color3(
                            denormalize(float(li[0])),
                            denormalize(float(li[1])),
                            denormalize(float(li[2])),
                        )
                        spec = Color3(
                            denormalize(float(li[3])),
                            denormalize(float(li[3])),
                            denormalize(float(li[3])),
                        )
                        roughness = float(li[4])
                        mat = {
                            "name": name,
                            "type": type,
                            "color": color,
                            "spec": spec,
                            "roughness": roughness,
                        }
                        materials[name] = mat
                        i += 5
                    elif type == "trans":
                        li = lines[i + 4].split(None)
                        color = Color3(
                            denormalize(float(li[0])),
                            denormalize(float(li[1])),
                            denormalize(float(li[2])),
                        )
                        spec = Color3(
                            denormalize(float(li[3])),
                            denormalize(float(li[3])),
                            denormalize(float(li[3])),
                        )
                        roughness = float(li[4])
                        trans = float(li[5])
                        tspec = float(li[6])
                        mat = {
                            "name": name,
                            "type": type,
                            "color": color,
                            "spec": spec,
                            "roughness": roughness,
                            "trans": trans,
                            "tspec": tspec,
                        }
                        materials[name] = mat
                        i += 5
                    elif type == "light":
                        li = lines[i + 4].split(None)
                        color = Color3(
                            denormalize(float(li[0])),
                            denormalize(float(li[1])),
                            denormalize(float(li[2])),
                        )
                        mat = {"name": name, "type": type, "color": color}
                        materials[name] = mat
                        i += 5
            else:
                keys = materials.keys()
                for k in keys:
                    if lines[i].startswith(k):
                        li = lines[i].split(None)
                        material = li[0]
                        type = li[1]
                        name = li[2].strip("\n")

                        if type == "point_light" or type == "point":
                            i += 1
                            vert = []
                            l = re.split(r"\s+|;+", lines[i])
                            vert.append(
                                (
                                    float(l[0]) / scale_factor,
                                    float(l[1]) / scale_factor,
                                    float(l[2]) / scale_factor,
                                )
                            )
                            shapes[name] = {
                                "vertices": vert,
                                "type": type,
                                "size": 1,
                                "material": material,
                            }
                        else:
                            i += 3
                            vert = []
                            size = int(lines[i])
                            tmp = i + 1
                            nbCoords = int(size / 3)
                            if type == "cylinder":
                                l = re.split(r"\s+|;+", lines[i + 1])
                                l2 = re.split(r"\s+|;+", lines[i + 2])
                                l3 = re.split(r"\s+|;+", lines[i + 3])
                                r = float(l3[0]) / scale_factor

                                x, y, z = (
                                    float(l[0]) / scale_factor,
                                    float(l[1]) / scale_factor,
                                    float(l[2]) / scale_factor,
                                )
                                x2, y2, z2 = (
                                    float(l2[0]) / scale_factor,
                                    float(l2[1]) / scale_factor,
                                    float(l2[2]) / scale_factor,
                                )

                                vert = cylinder_vertices(Vector3(x,y,z), Vector3(x2,y2,z2), 0)
                                # vert.append((x + r, y + r, z + r))
                                # vert.append((x - r, y - r, z - r))

                                # vert.append((x2 + r, y2 + r, z2 + r))
                                # vert.append((x2 - r, y2 - r, z2 - r))

                                
                                shapes[name] = {
                                    "vertices": vert,
                                    "type": type,
                                    "size": len(vert),
                                    "material": material,
                                }
                                i += 3
                            elif type == "cone":
                                l = re.split(r"\s+|;+", lines[i + 1])
                                l2 = re.split(r"\s+|;+", lines[i + 2])
                                l3 = re.split(r"\s+|;+", lines[i + 3])
                                r = float(l3[0]) / scale_factor
                                r2 = float(l3[1]) / scale_factor

                                x, y, z = (
                                    float(l[0]) / scale_factor,
                                    float(l[1]) / scale_factor,
                                    float(l[2]) / scale_factor,
                                )
                                x2, y2, z2 = (
                                    float(l2[0]) / scale_factor,
                                    float(l2[1]) / scale_factor,
                                    float(l2[2]) / scale_factor,
                                )

                                ratio = r / r2

                                pos = [x, y, z]
                                newCone = Frustum()
                                newCone.taper = 1.0 + ratio
                                newCone.height = z2 * 10 - z * 10
                                ts = Tesselator()
                                newCone.apply(ts)
                                mesh = ts.result
                                maxi = 0
                                for i in range(0, mesh.indexListSize()):
                                    index = mesh.indexAt(i)
                                    typeF = mesh.faceSize(i)
                                    for j in range(0, typeF):
                                        if index[j] > maxi:
                                            maxi = index[j]
                                for u in range(0, maxi + 1):
                                    mvector = mesh.pointAt(u)
                                    mesh.pointList[u] = (
                                        mvector[0] / 10 + pos[0],
                                        mvector[1] / 10 + pos[1],
                                        mvector[2] / 10 + pos[2],
                                    )

                                shapes[name] = {
                                    "vertices": vert,
                                    "type": type,
                                    "size": len(vert),
                                    "material": material,
                                    "mesh": mesh,
                                }
                                i += 3
                            else:
                                for j in range(tmp, tmp + nbCoords):
                                    l = re.split(r"\s+|;+", lines[j])
                                    vert.append(
                                        (
                                            float(l[0]) / scale_factor,
                                            float(l[1]) / scale_factor,
                                            float(l[2]) / scale_factor,
                                        )
                                    )
                                    i = j
                                    shapes[name] = {
                                        "vertices": vert,
                                        "type": type,
                                        "size": size,
                                        "material": material,
                                    }
                            if name == "anchor":
                                anchor = vert[1]
        for sh, val in shapes.items():
            mat_key = val["material"]
            mat = materials[mat_key]
            vert = val["vertices"]
            s = Shape()
            nbCoords = int(val["size"] / 3)
            if val.get("mesh") is not None:
                print("mesh detected")
                s.name = sh
                s.geometry = val["mesh"]
                if mat["type"] == "light":
                    s.name += str(vert[0])
                    s.appearance = Material(
                        name=name,
                        ambient=Color3(mat["color"]),
                        emission=Color3(mat["color"]),
                    )

                elif mat["type"] == "trans":
                    s.appearance = Material(
                        name=mat["name"],
                        ambient=Color3(mat["color"]),
                        specular=Color3(mat["spec"]),
                        shininess=1 - mat["roughness"],
                        transparency=mat["trans"],
                    )
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(
                            name=mat["name"],
                            ambient=Color3(mat["color"]),
                            shininess=1 - mat["roughness"],
                        )
                    else:
                        s.appearance = Material(
                            name=mat["name"],
                            ambient=Color3(mat["color"]),
                            specular=Color3(mat["spec"]),
                            shininess=1 - mat["roughness"],
                        )
                s.appearance.name = mat["name"]
                sc.add(s)

            elif nbCoords % 3 == 0:
                ts = TriangleSet(vert)
                i = 0
                indList = []
                if nbCoords == 9:
                    ind = Index3(i, i + 1, i + 2)
                    indList.append(ind)
                    ind = Index3(i, i + 2, i + 3)
                    indList.append(ind)
                    ind = Index3(i, i + 3, i + 4)
                    indList.append(ind)
                    ind = Index3(i, i + 4, i + 5)
                    indList.append(ind)
                    ind = Index3(i, i + 5, i + 6)
                    indList.append(ind)
                    ind = Index3(i, i + 6, i + 7)
                    indList.append(ind)
                    ind = Index3(i, i + 7, i + 8)
                    indList.append(ind)
                else:
                    while i < nbCoords:
                        if invert_normals:
                            ind = Index3(i, i + 2, i + 1)
                        else:
                            ind = Index3(i, i + 1, i + 2)
                        indList.append(ind)
                        i += 3
                ts.indexList = Index3Array(indList)
                ts.computeNormalList()
                s.geometry = ts
                s.name = sh
                if mat["type"] == "light":
                    s.name += str(vert[0])
                    s.appearance = Material(
                        name=name,
                        ambient=Color3(mat["color"]),
                        emission=Color3(mat["color"]),
                    )

                elif mat["type"] == "trans":
                    s.appearance = Material(
                        name=mat["name"],
                        ambient=Color3(mat["color"]),
                        specular=Color3(mat["spec"]),
                        shininess=1 - mat["roughness"],
                        transparency=mat["trans"],
                    )
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(
                            name=mat["name"],
                            ambient=Color3(mat["color"]),
                            shininess=1 - mat["roughness"],
                        )
                    else:
                        s.appearance = Material(
                            name=mat["name"],
                            ambient=Color3(mat["color"]),
                            specular=Color3(mat["spec"]),
                            shininess=1 - mat["roughness"],
                        )
                s.appearance.name = mat["name"]
                sc.add(s)
            else:
                #triangulate quad
                ts = TriangleSet(vert)
                i = 0
                indList = []
                while i < nbCoords:
                    if invert_normals:
                        ind = Index3(i, i + 2, i + 1)
                        ind2 = Index3(i, i + 3, i + 2)
                    else:
                        ind = Index3(i, i + 1, i + 2)
                        ind2 = Index3(i, i + 2, i + 3)
                    indList.append(ind)
                    indList.append(ind2)
                    i += 4
                
                ts.indexList = Index3Array(indList)
                ts.computeNormalList()
                s.geometry = ts
                s.name = sh
                if mat["type"] == "light":
                    s.appearance = Material(
                        name=mat["name"],
                        ambient=Color3(mat["color"]),
                        emission=Color3(mat["color"]),
                    )
                elif mat["type"] == "trans":
                    s.appearance = Material(
                        name=mat["name"],
                        ambient=Color3(mat["color"]),
                        specular=Color3(mat["spec"]),
                        shininess=1 - mat["roughness"],
                        transparency=mat["trans"],
                    )
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(
                            name=mat["name"],
                            ambient=Color3(mat["color"]),
                            shininess=1 - mat["roughness"],
                        )
                    else:
                        s.appearance = Material(
                            name=mat["name"],
                            ambient=Color3(mat["color"]),
                            specular=Color3(mat["spec"]),
                            shininess=1 - mat["roughness"],
                        )
                s.appearance.name = mat["name"]
                sc.add(s)
        save_name = file.split(".")[0] + ".obj"
        sc.save(save_name)
        return sc, anchor, scale_factor


def watts_to_emission(w):
    """
    Converts watts to emissive power.
    :param w: the watts to convert.
    :return: the emission strength.
    """
    return w * 2.0 / 10.0


def add_shape(
    scene: libphotonmap_core.Scene,
    sh: Shape,
    w: int,
    materialsR: dict,
    materialsS: dict,
    materialsT: dict,
):
    """
    Adds a PlantGL Shape to the Photon Mapping scene.
    :param scene: A libphotonmap_core Scene
    :param sh: The plantGL Shape to add
    :param w: The wavelength of the light to simulate.
    :param materialsR: The materials reflectance dictionary
    :param materialsT: The materials transmittance dictionary
    :return:
    """
    normals = VectorFloat(flatten(sh.geometry.normalList))
    indices = VectorUint(flatten(sh.geometry.indexList))
    vertices = VectorFloat(flatten(sh.geometry.pointList))
    ambient = Vec3(
        sh.appearance.ambient.red / 255.0,
        sh.appearance.ambient.green / 255.0,
        sh.appearance.ambient.blue / 255.0,
    )
    diffuse = ambient


    material_name = sh.appearance.name
    trans = 0.0 if materialsT.get(material_name) is None else materialsT[material_name]
    refl = 0.0 if materialsR.get(material_name) is None else materialsR[material_name]
    specular = 0.0 if materialsS.get(material_name) is None else materialsS[material_name]

    #print(material_name, refl, specular, trans)
    #trans = sh.appearance.transparency
    #refl = (sh.appearance.ambient.red / 255.0)
    #specular = (sh.appearance.specular.red / 255.0)
    
    #using mat Phong
    illum = 1

    if trans > 0.0:
        #illum = 9
        print("Transparent material: " + material_name)


    shininess = sh.appearance.shininess
    emission = sh.appearance.emission
    light_color = wavelength2Rgb(w)
    # print(str(light_color[0])+" "+str(light_color[1])+" "+str(light_color[2]))
    if len(indices) == 0:
        # regex to get the coords
        coords = re.findall(r"[-+]?\d*\.*\d+", sh.name)
        # coords[0] is the id of the light
        pos = Vec3(float(coords[0]), float(coords[1]), float(coords[2]))
        # print(emission)
        scene.addPointLight(pos, watts_to_emission(4000), light_color)

    elif emission != Color3(0, 0, 0):

        scene.addLight(vertices, indices, normals, 400, light_color, sh.name)
    else:
        scene.addFaceInfos(
            vertices,
            indices,
            normals,
            diffuse,
            ambient,
            specular,
            shininess,
            trans,
            illum,
            sh.name,
            1,
            refl,
            trans,
            1.0 - shininess
        )


def addCaptors(scene: libphotonmap_core.Scene, scale_factor: int, captor_dict: dict, filename: str):
    """
    Adds circular captors to the scene. the captors needs to be in a file
    :param filename:
    :param scene:
    :param captor_dict:
    :return:
    """
    lastTriangleId = scene.nFaces()
    with open(filename, "r") as f:
        next(f)
        captorId = 0
        for line in f:
            
            row = line.split(",")
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])
            r = float(row[3])
            xnorm = float(row[4])
            ynorm = float(row[5])
            znorm = float(row[6])
            pos = [x / scale_factor, y / scale_factor, z / scale_factor]
            normal = [xnorm, ynorm, znorm]
            r = r / scale_factor
            vertices = VectorFloat()
            normals = VectorFloat()
            triangles = VectorUint()

            val = 3.14285 / 180
            deltaAngle = 10
            vertices.append(pos[0])
            vertices.append(pos[1])
            vertices.append(pos[2])
            normals.append(normal[0])
            normals.append(normal[1])
            normals.append(normal[2])
            triangleCount = 0
            if znorm == 1:
                x1 = r * cos(0)
                y1 = r * sin(0)
                z1 = 0
            else:
                x1 = r * cos(0)
                y1 = 0
                z1 = r * sin(0)
            point1 = [x1 + pos[0], y1 + pos[1], z1 + pos[2]]
            vertices.append(point1[0])
            vertices.append(point1[1])
            vertices.append(point1[2])
            normals.append(normal[0])
            normals.append(normal[1])
            normals.append(normal[2])
            i = 0
            while i < 360:
                if znorm == 1:
                    x2 = r * cos((i + deltaAngle) * val)
                    y2 = r * sin((i + deltaAngle) * val)
                    z2 = 0
                else:
                    x2 = r * cos((i + deltaAngle) * val)
                    y2 = 0
                    z2 = r * sin((i + deltaAngle) * val)

                point2 = [x2 + pos[0], y2 + pos[1], z2 + pos[2]]
                vertices.append(point2[0])
                vertices.append(point2[1])
                vertices.append(point2[2])
                normals.append(normal[0])
                normals.append(normal[1])
                normals.append(normal[2])

                triangles.append(triangleCount + 1)
                triangles.append(triangleCount + 2)
                triangles.append(0)

                triangleCount += 1
                i += deltaAngle

            scene.addCaptor(vertices, triangles, normals)

            for j in triangles:
                captor_dict[lastTriangleId + j] = captorId
            captorId += 1
            lastTriangleId = scene.nFaces()


def photonmap_plantglScene(sc, anchor, scale_factor):
    """
    Photon maps the plantGL Scene provided
    :param sc: The plantGL Scene
    :param anchor: A 3D point to put the virtual plant on.
    :param scale_factor: The scale factor to get a meter.
    :return:
    """
    n_samples = 1
    n_photons = int(1e9)
    
    n_estimation_global = 100
    n_photons_caustics_multiplier = 50
    n_estimation_caustics = 50
    final_gathering_depth = 0 #no caustics effet
    max_depth = 50
    ray_t_near = 0.1

    aspect_ratio = 16.0 / 9.0
    image_width = 1024
    image_height = int(image_width / aspect_ratio)

    image = libphotonmap_core.Image(image_width, image_height)
    lookfrom = Vec3(1.5, 1.5, 1.5)
    lookat = Vec3(anchor[0], anchor[1], anchor[2])
    vup = Vec3(0, 0, -1)
    vfov = 50.0
    dist_to_focus = 2.0
    aperture = 0.01

    # coordinates must be in meters
    camera = libphotonmap_core.Camera(
        lookfrom, lookat, vup, vfov, aspect_ratio, aperture, dist_to_focus
    )

    # Setting up spectrum bands
    spectrum = "whole"
    spec_file = "spectrum/chambre1_spectrum"
    spec_dict, step, start = read_spectrum_file(spec_file)
    wavelengths = []
    integrals = []
    band: range
    band1: range
    band2: range
    band3: range
    bands = []
    if spectrum.lower().startswith("blue"):
        band = range(start, 500, step)
        bands.append(band)
        wavelengths.append(get_average_of_band(band, spec_dict))
        integrals.append(get_integral_of_band(band, spec_dict))
        bands.append(band)
    elif spectrum.lower().startswith("green"):
        start = bisect.bisect_right(list(spec_dict.keys()), 500)
        start = list(spec_dict.keys())[start]
        band = range(start, 600, step)
        bands.append(band)
        wavelengths.append(get_average_of_band(band, spec_dict))
        integrals.append(get_integral_of_band(band, spec_dict))
    elif spectrum.lower().startswith("red"):
        start = bisect.bisect_right(list(spec_dict.keys()), 600)
        start = list(spec_dict.keys())[start]
        band = range(start, 700, step)
        bands.append(band)
        wavelengths.append(get_average_of_band(band, spec_dict))
        integrals.append(get_integral_of_band(band, spec_dict))
    elif spectrum.lower().startswith("far red"):
        start = bisect.bisect_right(list(spec_dict.keys()), 700)
        start = list(spec_dict.keys())[start]
        band = range(start, 800, step)
        bands.append(band)
        wavelengths.append(get_average_of_band(band, spec_dict))
        integrals.append(get_integral_of_band(band, spec_dict))
    elif spectrum.lower().startswith("par"):
        start2 = bisect.bisect_right(list(spec_dict.keys()), 500)
        start3 = bisect.bisect_right(list(spec_dict.keys()), 600)
        start2 = list(spec_dict.keys())[start2]
        start3 = list(spec_dict.keys())[start3]
        band1 = range(start, 500, step)
        band2 = range(start2, 600, step)
        band3 = range(start3, 700, step)
        bands.append(band1)
        bands.append(band2)
        bands.append(band3)
        wavelengths.append(get_average_of_band(band1, spec_dict))
        wavelengths.append(get_average_of_band(band2, spec_dict))
        wavelengths.append(get_average_of_band(band3, spec_dict))
        integrals.append(get_integral_of_band(band1, spec_dict))
        integrals.append(get_integral_of_band(band2, spec_dict))
        integrals.append(get_integral_of_band(band3, spec_dict))
    else:
        #setup spectrum
        band1 = range(401, 445, step)
        band2 = range(655, 665, step)
        band3 = range(735, 800, step)

        bands.append(band1)
        bands.append(band2)
        bands.append(band3)

        wavelengths.append(get_average_of_band(band1, spec_dict))
        wavelengths.append(get_average_of_band(band2, spec_dict))
        wavelengths.append(get_average_of_band(band3, spec_dict))

        integrals.append(get_integral_of_band(band1, spec_dict))
        integrals.append(get_integral_of_band(band2, spec_dict))
        integrals.append(get_integral_of_band(band3, spec_dict))


    band_start = [400, 655, 735]
    band_end = [445, 665, 800]

    nb_exp = 1
    integral_idx = 0
    scene = libphotonmap_core.Scene()

    #for index in range(len(wavelengths)):
    for index in range(1):
        captor_energy = {}
        for exp in range(nb_exp):
            start = time.time()
            index = 1
            print("************-Experience nb " + str(exp + 1)+ "-************")
            materialsR, materialsS, materialsT = setup_dataset_materials(band_start[index], band_end[index])
            scene.clear()
            captor_dict = {}
            for sh in sc:
                add_shape(scene, sh, wavelengths[index], materialsR, materialsS, materialsT)
            tr2shmap = {}

            # print(scene.nFaces())
            # add_lpy_file_to_scene(
            #      scene, "assets/rose-simple4.lpy", 128, tr2shmap, anchor, scale_factor
            # )
            
            # lsystem = Lsystem("assets/rose-simple4.lpy")
            # lstring = lsystem.derive(lsystem.axiom, 128)
            # lscene = lsystem.sceneInterpretation(lstring)
            # # Adding the model of plant
            # addModel(lscene, Tesselator(), tr2shmap, scene, anchor, scale_factor)
            
            addCaptors(scene, scale_factor, captor_dict, "captors/captors_expe1.csv")
            #print(scene.nFaces())
            scene.tnear = ray_t_near
            scene.setupTriangles()
            scene.build()

           
            print("Building photonMap...")
            integrator = PhotonMapping(
                n_photons,
                n_estimation_global,
                n_photons_caustics_multiplier,
                n_estimation_caustics,
                final_gathering_depth,
                max_depth,
            )

            

            sampler = UniformSampler(random.randint(1, sys.maxsize))
            
            # build no kdtree if not rendering
            integrator.build(scene, sampler, False)
            # print("Done!")
            # print("Printing photonmap image...")
            # visualizePhotonMap(
            #     integrator,
            #     scene,
            #     image,
            #     image_height,
            #     image_width,
            #     camera,
            #     n_photons,
            #     max_depth,
            #     "results/photonmap-" + str(w) + "nm.ppm",
            #     sampler,
            # )
            # image.clear()
            
            # print("Printing captor photonmap image...")
            # visualizeCaptorsPhotonMap(
            #     scene,
            #     image,
            #     image_height,
            #     image_width,
            #     camera,
            #     n_photons,
            #     max_depth,
            #     "results/photonmap-captors-" + str(w) + "nm.ppm",
            #     sampler,
            #     integrator,
            # )
            # image.clear()
            #
            # image.clear()
            # # visualizeCausticsPhotonMap(
            # #     scene,
            # #     image,
            # #     image_width,
            # #     image_height,
            # #     camera,
            # #     n_photons,
            # #     max_depth,
            # #     "results/photonmap-cautics.ppm",
            # #     sampler,
            # #     integrator,
            # # )
            #
            # image.clear()
            # print("Done!")
            #
            # print("Rendering image...")
            # image = libphotonmap_core.Image(image_width, image_height)
            # Render(
            #     sampler,
            #     image,
            #     image_height,
            #     image_width,
            #     n_samples,
            #     camera,
            #     integrator,
            #     scene,
            #     "results/output-photonmapping-" + str(w) + "nm.ppm",
            # )

            # image.clear()
            captor_add_energy(captor_dict, integrator, captor_energy)
            # print("correction ratio: " + str(integrals[integral_idx]))
            # correct_energy(captor_energy, integrals[integral_idx])

            #Plant Energie
            #captor_energy = compute_energy(tr2shmap, integrator)
            #sc = addModelPgl(lscene, Tesselator(), sc, anchor, scale_factor, captor_energy)
            #Viewer.display(sc)

            print("Time taken: " + str(time.time() - start))
            # print("Done!")
        write_captor_energy(captor_energy, band_start[index], band_end[index], n_photons, nb_exp)
        integral_idx += 1


if __name__ == "__main__":

    # lsystem = Lsystem( "assets/rose-simple4.lpy")
    # lstring = lsystem.derive(lsystem.axiom, 150)
    # lscene = lsystem.sceneInterpretation(lstring)

    # sc, anchor, scale_factor = read_rad("assets/chambre2.rad", True)
    sc, anchor, scale_factor = read_rad("assets/testChamber.rad", False)
    #sc, anchor, scale_factor = read_rad("assets/chamberVide.rad", False)
    #sc, anchor, scale_factor = read_rad("assets/simple.rad", False)

    shenergy = photonmap_plantglScene(sc, anchor, scale_factor)

    #sc = addModelPgl(lscene, Tesselator(), sc, anchor, scale_factor, shenergy)
    #sc = addCapteurPgl(sc, scale_factor, "captors/captors_expe1.csv")
    #sc = addLightDirectionPgl(sc, scale_factor)
    

    

    
    


# command visualiser Environnement PlantGL
# ipython
# %gui qt
# run planglRadScene.py
