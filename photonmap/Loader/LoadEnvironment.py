import re

from openalea.plantgl.all import *

from photonmap import (
    Vec3,
    VectorFloat,
    VectorUint,
)
from photonmap.Common.Math import *
from photonmap.Common.Outils import *

# Objectif of this module is adding environment object to the scene of Photon Mapping


def addEnvironment(
    scene,
    sh,
    w,
    materialsR: dict,
    materialsS: dict,
    materialsT: dict,
    is_only_lamp=False,
):
    """
    Adds a PlantGL Shape of the room to the Photon Mapping scene.

    Parameters
    ----------
    scene : libphotonmap_core.Scene
        The photon mapping scene used to run the simulation
    sh : Shape
        The plantGL Shape to add
    w : int
        The wavelength of the light to simulate.
    materialsR : dict
        The materials reflection dictionary
    materialsS : dict
        The materials specularity dictionary
    materialsT : dict
        The materials transmission dictionary
    is_only_lamp : bool
        If True, add only the lamps and captors, If False, add all the objects in room

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
    trans = (
        sh.appearance.transparency
        if materialsT.get(material_name) is None
        else materialsT[material_name]
    )
    refl = (
        (sh.appearance.ambient.red / 255.0)
        if materialsR.get(material_name) is None
        else materialsR[material_name]
    )
    specular = (
        (sh.appearance.specular.red / 255.0)
        if materialsS.get(material_name) is None
        else materialsS[material_name]
    )

    # print(material_name, refl, specular, trans)

    # using mat Phong
    illum = 1

    if trans > 0.0:
        # illum = 9
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
        scene.addPointLight(pos, 400, light_color)

    elif emission != Color3(0, 0, 0):
        scene.addLight(vertices, indices, normals, 4000, light_color, sh.name)

    elif is_only_lamp is False:
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
            1.0 - shininess,
        )


# add light direction to a scene of PlantGL to visualize
def addLightDirectionPgl(sc, scale_factor):
    """
    Adds a PlantGL Shape of the room to the Photon Mapping scene.

    Parameters
    ----------
    sc : Lscene
        The plantgl scene
    scale_factor : int
        The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value

    Returns
    -------
        A PlantGL Scene with the hemisphere of each surface
    """
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
            sh_dir.appearance.ambient = Color3(1, 0, 0)

            pglScene.add(sh_dir)

    return Scene([pglScene, sc])
