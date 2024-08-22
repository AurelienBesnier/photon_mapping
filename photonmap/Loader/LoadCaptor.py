from math import cos, sin, pi
from photonmap.Common.Outils import *
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
    def initGeometryCaptor(self, shape, position, scale_factor, using_mat):
        """
        Init a object of captor 

        Returns
        -------
        shape: Shape
            The geometry and material of captor
        position: tuple
            The position of captor
        scale_factor: float
            The scale factor of captor
        using_mat: bool
            If False the material captor has no effect to the light, if True the way that the light interacts when it contacts the captor is same as when it contacts the other surfaces

        """
        self.type = "geometry"
        self.xSite = position[0] / scale_factor
        self.ySite = position[1] / scale_factor
        self.zSite = position[2] / scale_factor
        self.using_mat = using_mat
        self.radius = 0

        vertices = shape.geometry.pointList
        #apply scale factor
        for i in range(len(vertices)):
            cur_vertice = vertices[i]
            vertices[i] = ((cur_vertice[0] + position[0]) / scale_factor,
                            (cur_vertice[1] + position[1]) / scale_factor,
                            (cur_vertice[2] + position[2]) / scale_factor)
        
        shape.geometry.pointList = vertices
        shape.geometry.computeNormalList()

        #return vertice list, indexlist
        self.vertices = VectorFloat(flatten(shape.geometry.pointList))
        self.normals = VectorFloat(flatten(shape.geometry.normalList))
        self.triangles = VectorUint(flatten(shape.geometry.indexList))

        #return reflection, specular, transmission
        self.trans = shape.appearance.transparency
        self.refl = shape.appearance.ambient.red / 255.0
        self.specular = shape.appearance.specular.red / 255.0
        self.roughness = 1.0 - shape.appearance.shininess

        return self

    def initTransDiskCaptor(self, pos = (0,0,0), nor = (0,0,0), r = 0):
        """
        Init a object of disk shape captor 

        Returns
        -------
        pos: tuple
            The position of captor
        nor: tuple
            The normal vector of captor
        r: float
            The radius of captor

        """
        self.type = "disk"
        self.xSite = pos[0]
        self.ySite = pos[1]
        self.zSite = pos[2]
        self.xNormal = nor[0]
        self.yNormal = nor[1]
        self.zNormal = nor[2]
        self.radius = r

        #setup optical properties 
        self.using_mat = False
        self.trans = 0
        self.refl = 0
        self.specular = 0
        self.roughness = 0
        
        self.createDiskGeometry()

        return self
    
    def createDiskGeometry(self):
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

def readCaptorsFile(scale_factor, filename):
    """
    Read all the captors in a file

    Parameters
    ----------
    scale_factor : int
        The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value
    filename : str
        The link to the file which contains the data of captors

    Returns
    -------
        return the list of captors

    """
    captor_list = []
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

            captor = Captor().initTransDiskCaptor((x, y, z), (xnorm, ynorm, znorm), r)
            captor_list.append(captor)
    
    return captor_list


def addCaptors(scene, captor_triangle_dict, list_captor):
    """
    Adds circular captors to the scene. the captors needs to be in a file

    Parameters
    ----------
    scene : libphotonmap_core.Scene
        The photon mapping scene used to run the simulation
    captor_triangle_dict : dict
        The dictionary of the triangles of captors
    list_captor : array
        The list of captor

    Returns
    -------
        Add all the mesh of captors to the scene 

    """
    lastTriangleId = scene.nFaces()
    for i in range(len(list_captor)):
        captor = list_captor[i]
        vertices, triangles, normals = captor.getGeometry()
        #
        scene.addCaptor(vertices, triangles, normals, captor.using_mat, 
                            captor.refl, captor.specular, captor.trans, captor.roughness)
            
        #
        for j in triangles:
            captor_triangle_dict[lastTriangleId + j] = i

        lastTriangleId = scene.nFaces()


def findIndexOfDiskCaptorInList(list_captor, x, y, z):
    """
    Find the index of a disk shape captor while knowing its position

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