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

class Captor:
    """
    A class which contains all the data of captor.

    Attributes
    ----------
    xSite: float
        The X coordinate of captor's position
    ySite: float
        The Y coordinate of captor's position
    zSite: float
        The Z coordinate of captor's position
    xNormal: float
        The X coordinate of captor's normal
    yNormal: float
        The Y coordinate of captor's normal
    zNormal: float
        The Z coordinate of captor's normal
    radius: float
        The radius of captor
    vertices: array
        The vertices of captor's geometry
    normals: array
        The normal vectors of each vertices in captor's geometry
    triangles: array
        The triangles of captor's geometry
   
    
    """
    def __init__(self, pos_x = 0, pos_y = 0, pos_z = 0, nor_x = 0, nor_y = 0, nor_z = 0, r = 0):
        self.xSite = pos_x
        self.ySite = pos_y
        self.zSite = pos_z
        self.xNormal = nor_x
        self.yNormal = nor_y
        self.zNormal = nor_z
        self.radius = r

        self.createGeometry()
    
    def createGeometry(self):
        """
        Create geometry of circular captor 

        Returns
        -------
        vertices: array
            The vertices of captor's geometry
        normals: array
            The normal vectors of each vertices in captor's geometry
        triangles: array
            The triangles of captor's geometry

        """
        vertices = VectorFloat()
        normals = VectorFloat()
        triangles = VectorUint()

        val = 3.14285 / 180
        deltaAngle = 10
        triangleCount = 0

        vertices.append(self.xSite)
        vertices.append(self.ySite)
        vertices.append(self.zSite)
        normals.append(self.xNormal)
        normals.append(self.yNormal)
        normals.append(self.zNormal)
        
        if self.zNormal == 1:
            x1 = self.radius * cos(0)
            y1 = self.radius * sin(0)
            z1 = 0
        else:
            x1 = self.radius * cos(0)
            y1 = 0
            z1 = self.radius * sin(0)

        vertices.append(x1 + self.xSite)
        vertices.append(y1 + self.ySite)
        vertices.append(z1 + self.zSite)
        normals.append(self.xNormal)
        normals.append(self.yNormal)
        normals.append(self.zNormal)

        i = 0
        while i < 360:
            if self.zNormal == 1:
                x2 = self.radius * cos((i + deltaAngle) * val)
                y2 = self.radius * sin((i + deltaAngle) * val)
                z2 = 0
            else:
                x2 = self.radius * cos((i + deltaAngle) * val)
                y2 = 0
                z2 = self.radius * sin((i + deltaAngle) * val)

            vertices.append(x2 + self.xSite)
            vertices.append(y2 + self.ySite)
            vertices.append(z2 + self.zSite)
            normals.append(self.xNormal)
            normals.append(self.yNormal)
            normals.append(self.zNormal)

            triangles.append(triangleCount + 1)
            triangles.append(triangleCount + 2)
            triangles.append(0)

            triangleCount += 1
            i += deltaAngle

        self.vertices = vertices
        self.normals = normals
        self.triangles = triangles
    
    def equal(self, xSite, ySite, zSite):
        """
        Check if the coordinate is equal to the position of captor

        Parameters
        ----------
        xSite: float
            The X coordinate
        ySite: float
            The Y coordinate
        zSite: float
            The Z coordinate

        Returns
        -------
            True if equal
            False if not equal

        """

        if self.xSite == xSite and self.ySite == ySite and self.zSite == zSite:
            return True
        
        return False

    def getGeometry(self):
        """
        Get geometry of captor

        Returns
        -------
        vertices: array
            The vertices of captor's geometry
        normals: array
            The normal vectors of each vertices in captor's geometry
        triangles: array
            The triangles of captor's geometry

        """

        return self.vertices, self.triangles, self.normals

def addCaptors(scene, scale_factor, captor_triangle_dict, filename):
    """
    Adds circular captors to the scene. the captors needs to be in a file

    Parameters
    ----------
    scene : libphotonmap_core.Scene
        The photon mapping scene used to run the simulation
    scale_factor : int
        The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value
    captor_triangle_dict : dict
        The dictionary of the triangles of captors
    filename : str
        The link to the file which contains the data of captors

    
    Returns
    -------
        Add all the mesh of captors to the scene and return the list of captors

    """
    lastTriangleId = scene.nFaces()
    captor_list = []
    with open(filename, "r") as f:
        next(f)
        captorId = 0
        for line in f:
            
            row = line.split(",")
            x = float(row[0]) / scale_factor
            y = float(row[1]) / scale_factor
            z = float(row[2]) / scale_factor
            r = float(row[3]) / scale_factor
            xnorm = float(row[4])
            ynorm = float(row[5])
            znorm = float(row[6])

            captor = Captor(x, y, z, xnorm, ynorm, znorm, r)
            vertices, triangles, normals = captor.getGeometry()
            scene.addCaptor(vertices, triangles, normals)

            for j in triangles:
                captor_triangle_dict[lastTriangleId + j] = captorId
            captorId += 1
            lastTriangleId = scene.nFaces()
            captor_list.append(captor)
    
    return captor_list

def findIndexOfCaptorInList(list_captor, x, y, z):
    """
    Find the index of a captor while knowing its position

    Parameters
    ----------
    list_captor : Array
        The list of the captor in the scene
    x : float
        x coordinate
    y : float
        y coordinate
    z : float
        z coordinate

    Returns
    -------
        if not found, return -1 
        if found, return the index of the captor

    """
        
    for i in range(len(list_captor)):
        if(list_captor[i].equal(x, y, z)):
            return i
    return -1

#add captor to a scene of PlantGL to visualize
def addCapteurPgl(sc, scale_factor: int, filename: str):
    """
    Add the captors to the PlantGL scene to visualize the scene

    Parameters
    ----------
    sc : Lscene
        The plantgl scene
    scale_factor : int
        The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value
    filename : float
        The link to the file which contains the data of captors

    Returns
    -------
        A PlantGL Scene with the captors

    """
        
    pglScene = Scene()

    with open(filename, "r") as f:
        next(f)
        for line in f:
            row = line.split(",")
            x = float(row[0]) / scale_factor
            y = float(row[1]) / scale_factor
            z = float(row[2]) / scale_factor
            r = float(row[3]) / scale_factor
            xnorm = float(row[4])
            ynorm = float(row[5])
            znorm = float(row[6])

            captor = Captor(x, y, z, xnorm, ynorm, znorm, r)
            vertices, triangles, normals = captor.getGeometry()

            pgl_vertices = []
            pgl_triangles = []
            pgl_normals = []

            for ind in range(0, len(vertices), 3):
                pgl_vertices.append(Vector3(vertices[ind], vertices[ind + 1], vertices[ind + 2]))
                pgl_normals.append(Vector3(normals[ind], normals[ind + 1], normals[ind + 2]))

            for ind in range(0, len(triangles), 3):
                pgl_triangles.append(Index3(triangles[ind], triangles[ind + 1], triangles[ind + 2]))

            tmpSh= Shape(TriangleSet(pgl_vertices, pgl_triangles, pgl_normals))
            tmpSh.appearance.ambient = Color3(1,0,0)
            pglScene.add(tmpSh)

    return Scene([pglScene, sc])