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

# Objectif of this module is adding captors to the scene of photon mapping to the received energy


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

    def initCaptor(self, shape, position, scale_factor, captor_id, captor_type):
        """
        Init a object of face captor 

        Returns
        -------
        shape: Shape
            The geometry and material of captor
        position : tuple(int,int,int)
            The position of captor
        scale_factor: int
            The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value
        captor_id: int
            The id of captor
        captor_type: str
            "VirtualCaptor" or "FaceCaptor"
        """

        self.type = captor_type
        self.captor_id = captor_id
        self.xSite = position[0] / scale_factor
        self.ySite = position[1] / scale_factor
        self.zSite = position[2] / scale_factor
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

        self.shape = shape

        return self

    def initVirtualDiskCaptor(self, pos = (0,0,0), nor = (0,0,0), r = 0, captor_id = 0):
        """
        Init a object of virtual disk shape captor 

        Returns
        -------
        pos: tuple
            The position of captor
        nor: tuple
            The normal vector of captor
        r: float
            The radius of captor
        captor_id: int
            The id of captor

        """
        self.type = "VirtualCaptor"
        self.xSite = pos[0]
        self.ySite = pos[1]
        self.zSite = pos[2]
        self.xNormal = nor[0]
        self.yNormal = nor[1]
        self.zNormal = nor[2]
        self.radius = r
        self.captor_id = captor_id
        
        self.createVirtualDisk()

        return self
    
    def createVirtualDisk(self):
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
        vertices = []
        normals = []
        triangles = []

        val = 3.14285 / 180
        deltaAngle = 10
        triangleCount = 0

        vertices.append((self.xSite, self.ySite, self.zSite))
        normals.append((self.xNormal, self.yNormal, self.zNormal))
        
        if self.zNormal == 1:
            x1 = self.radius * cos(0)
            y1 = self.radius * sin(0)
            z1 = 0
        else:
            x1 = self.radius * cos(0)
            y1 = 0
            z1 = self.radius * sin(0)

        vertices.append((x1 + self.xSite, y1 + self.ySite, z1 + self.zSite))
        normals.append((self.xNormal, self.yNormal, self.zNormal))

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

            vertices.append((x2 + self.xSite, y2 + self.ySite, z2 + self.zSite))
            normals.append((self.xNormal, self.yNormal, self.zNormal))
            triangles.append((triangleCount + 1, triangleCount + 2, 0))

            triangleCount += 1
            i += deltaAngle

        captor_shape = Shape(TriangleSet(vertices, triangles, normals),
                             Material(
                                name="Captor",
                                ambient = Color3( 0 ),
                                specular = Color3( 0 ),
                                shininess = 1,
                                transparency = 0))

        self.shape = captor_shape
    
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
        
        #return vertice list, indexlist
        vertices = VectorFloat(flatten(self.shape.geometry.pointList))
        normals = VectorFloat(flatten(self.shape.geometry.normalList))
        triangles = VectorUint(flatten(self.shape.geometry.indexList))
        return vertices, triangles, normals
    
    def getOpticalProperties(self):
        """
        Get optical properties of captor

        Returns
        -------
        vertices: array
            The vertices of captor's geometry
        normals: array
            The normal vectors of each vertices in captor's geometry
        triangles: array
            The triangles of captor's geometry

        """
        
        #return reflection, specular, transmission
        trans = self.shape.appearance.transparency
        refl = self.shape.appearance.ambient.red / 255.0
        specular = self.shape.appearance.specular.red / 255.0
        roughness = 1.0 - self.shape.appearance.shininess

        return refl, specular, trans, roughness
    

def addVirtualCaptors(scene, virtual_captor_triangle_dict, list_virtual_captor):
    """
    Adds virtual captors to the scene. 

    Parameters
    ----------
    scene : libphotonmap_core.Scene
        The photon mapping scene used to run the simulation
    virtual_captor_triangle_dict : dict
        The dictionary of the triangles of captors
    list_virtual_captor : array
        The list of virtual captor

    Returns
    -------
        Add all the mesh of virtual captors to the scene 

    """
    lastTriangleId = scene.nFaces()
    for i in range(len(list_virtual_captor)):
        captor = list_virtual_captor[i]
        if captor.type != "VirtualCaptor":
            return
        
        vertices, triangles, normals = captor.getGeometry()
        #
        scene.addVirtualCaptorInfos(vertices, triangles, normals)
            
        #
        for j in triangles:
            virtual_captor_triangle_dict[lastTriangleId + j] = captor.captor_id

        lastTriangleId = scene.nFaces()

def addFaceCaptors(scene, face_captor_triangle_dict, list_face_captor):
    """
    Adds face captors to the scene. 

    Parameters
    ----------
    scene : libphotonmap_core.Scene
        The photon mapping scene used to run the simulation
    face_captor_triangle_dict : dict
        The dictionary of the triangles of captors
    list_face_captor : array
        The list of face captor

    Returns
    -------
        Add all the mesh of face captors to the scene 

    """
    
    lastTriangleId = scene.nFaces()
    for i in range(len(list_face_captor)):
        captor = list_face_captor[i]
        if captor.type != "FaceCaptor":
            return

        vertices, triangles, normals = captor.getGeometry()
        refl, specular, trans, roughness = captor.getOpticalProperties()
        #
        scene.addFaceCaptorInfos(vertices, triangles, normals, refl, 
                                 specular, trans, roughness)
        #
        for j in triangles:
            face_captor_triangle_dict[lastTriangleId + j] = captor.captor_id

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
        if list_captor[i].equal(x, y, z):
            return i
    return -1

#add captor to a scene of PlantGL to visualize
def addCaptorPgl(sc, list_captor):
    """
    Add the captors to the PlantGL scene to visualize the scene

    Parameters
    ----------
    sc : Lscene
        The plantgl scene
    list_captor : array
        The list of captors

    Returns
    -------
        A PlantGL Scene with the captors

    """

    pglScene = Scene()

    for i in range(len(list_captor)):
        captor_sh = list_captor[i].shape
        pglScene.add(captor_sh)
            
    return Scene([pglScene, sc])
