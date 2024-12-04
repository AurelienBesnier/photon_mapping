import re

from openalea.spice import (
    Vec3,
    VectorFloat,
    VectorUint,
)
from openalea.spice.common.math import average_vector, geo_hemisphere
from openalea.spice.common.tools import flatten, wavelength2rgb
from openalea.plantgl.all import Color3, Scene

# Objectif of this module is adding environment object to the scene of Photon Mapping


def addEnvironment(
    scene,
    sh,
    w,
    materials_r: dict,
    materials_s: dict,
    materials_t: dict,
    is_only_lamp=False,
):
    """
    Adds a PlantGL Shape of the room to the Photon Mapping scene.

    Parameters
    ----------
    scene : libspice_core.Scene
        The photon mapping scene used to run the simulation
    sh : Shape
        The plantGL Shape to add
    w : int
        The wavelength of the light to simulate.
    materials_r : dict
        The materials reflection dictionary
    materials_s : dict
        The materials specularity dictionary
    materials_t : dict
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
        if materials_t.get(material_name) is None
        else materials_t[material_name]
    )
    refl = (
        (sh.appearance.ambient.red / 255.0)
        if materials_r.get(material_name) is None
        else materials_r[material_name]
    )
    specular = (
        (sh.appearance.specular.red / 255.0)
        if materials_s.get(material_name) is None
        else materials_s[material_name]
    )

    # print(material_name, refl, specular, trans)

    # using mat Phong
    illum = 1

    if trans > 0.0:
        # illum = 9
        print("Transparent material: " + material_name)

    shininess = sh.appearance.shininess
    emission = sh.appearance.emission

    light_color = wavelength2rgb(w)
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
    pgl_scene = Scene()

    for sh in sc:
        vertices = sh.geometry.pointList
        normals = sh.geometry.normalList
        if len(vertices) == 4:
            centre = average_vector(vertices)
            normal = average_vector(normals)
            normal.normalize()
            rayon = 50 * scale_factor

            sh_dir = geo_hemisphere(centre, normal, rayon)
            sh_dir.appearance.ambient = Color3(1, 0, 0)

            pgl_scene.add(sh_dir)

    return Scene([pgl_scene, sc])
