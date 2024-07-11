
from photonmap import libphotonmap_core
from openalea.plantgl.all import * 
from modules.Common.Math import *
from modules.Common.Outils import *
from photonmap import (
    Vec3,
    VectorUint,
    VectorFloat,
    PhotonMapping,
    UniformSampler,
)

#Objectif of this module is adding environment object to the scene of Photon Mapping

def add_environment(
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
        scene.addPointLight(pos, 400, light_color)

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

#add light direction to a scene of PlantGL to visualize
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