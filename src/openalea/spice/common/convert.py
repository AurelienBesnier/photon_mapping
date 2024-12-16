import openalea.plantgl.all as pgl
from openalea.spice.libspice_core import Scene, Vec3, VectorFloat, VectorUint
from openalea.spice.common.tools import flatten

def pgl_to_spice(scene: pgl.Scene):
    spice_scene = Scene()
    nb_shapes = len(scene)
    i = 1
    for sh in scene:
        print(f"Adding shape {i}/{nb_shapes}")
        sh.geometry.computeNormalList()
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
        trans = sh.appearance.transparency
        refl = sh.appearance.ambient.red / 255.0
        specular = sh.appearance.specular.red / 255.0

        # using mat Phong
        illum = 1

        if trans > 0.0:
            # illum = 9
            print("Transparent material: " + material_name)

        shininess = sh.appearance.shininess
        spice_scene.addFaceInfos(
            vertices,
            indices,
            normals,
            diffuse,
            ambient,
            specular,
            shininess,
            trans,
            illum,
            str(sh.id),
            1,
            refl,
            trans,
            1.0 - shininess,
        )
        i+=1

    return spice_scene