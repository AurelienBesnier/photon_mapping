from math import cos, sin, pi
from photonmap import libphotonmap_core
from openalea.plantgl.all import * 
from photonmap import (
    Vec3,
    VectorUint,
    VectorFloat,
    PhotonMapping,
    UniformSampler,
)

#Objectif of this module is adding captors to the scene of photon mapping to the received energy 
#Data is located in this directory: ./captors

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


#add captor to a scene of PlantGL to visualize
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