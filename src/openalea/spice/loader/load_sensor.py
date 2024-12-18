from math import cos, sin

from openalea.plantgl.all import Color3, Material, Scene, Shape, TriangleSet

from openalea.spice import VectorFloat, VectorUint, Vec3
from openalea.spice.common.tools import flatten

# Objectif of this module is adding sensors to the scene of photon mapping to the received energy


class Sensor:
    """
    A class which contains all the data of sensor.

    Attributes
    ----------
    xSite: float
        The X coordinate of sensor's position
    ySite: float
        The Y coordinate of sensor's position
    zSite: float
        The Z coordinate of sensor's position
    xNormal: float
        The X coordinate of sensor's normal
    yNormal: float
        The Y coordinate of sensor's normal
    zNormal: float
        The Z coordinate of sensor's normal
    radius: float
        The radius of sensor
    vertices: array
        The vertices of sensor's geometry
    normals: array
        The normal vectors of each vertices in sensor's geometry
    triangles: array
        The triangles of sensor's geometry


    """

    def __init__(self, shape, sensor_type, position=Vec3(0, 0, 0), scale_factor=1):
        self.zNormal = None
        self.yNormal = None
        self.xNormal = None
        self.type = sensor_type
        self.sensor_id = shape.id
        self.radius = 0
        self.xSite = position[0] / scale_factor
        self.ySite = position[1] / scale_factor
        self.zSite = position[2] / scale_factor

        if hasattr(shape.geometry, "pointList"):
            vertices = shape.geometry.pointList
            # apply scale factor
            if scale_factor is not None:
                for i in range(len(vertices)):
                    cur_vertice = vertices[i]
                    vertices[i] = (
                        (cur_vertice[0] + position[0]) / scale_factor,
                        (cur_vertice[1] + position[1]) / scale_factor,
                        (cur_vertice[2] + position[2]) / scale_factor,
                    )
            shape.geometry.computeNormalList()

        self.shape = shape

    def initSensor(self, shape, position, scale_factor, sensor_type):
        """
        Init an object of face sensor

        Returns
        -------
        shape: Shape
            The geometry and material of sensor
        position : tuple(int,int,int)
            The position of sensor
        scale_factor: int
            The size of geometries. The vertices of geometries is recalculated by dividing their coordinates by this value
        sensor_type: str
            "VirtualSensor" or "FaceSensor"
        """

        self.type = sensor_type
        self.sensor_id = shape.id
        self.xSite = position[0] / scale_factor
        self.ySite = position[1] / scale_factor
        self.zSite = position[2] / scale_factor
        self.radius = 0

        vertices = shape.geometry.pointList
        # apply scale factor
        for i in range(len(vertices)):
            cur_vertice = vertices[i]
            vertices[i] = (
                (cur_vertice[0] + position[0]) / scale_factor,
                (cur_vertice[1] + position[1]) / scale_factor,
                (cur_vertice[2] + position[2]) / scale_factor,
            )
        if shape.geometry.pointList is not None:
            shape.geometry.pointList = vertices
            shape.geometry.computeNormalList()

        self.shape = shape

        return self

    def initVirtualDiskSensor(self, nor=(0, 0, 0), r=0, sensor_id=0):
        """
        Init a object of virtual disk shape sensor

        Returns
        -------
        pos: tuple
            The position of sensor
        nor: tuple
            The normal vector of sensor
        r: float
            The radius of sensor
        sensor_id: int
            The id of sensor

        """
        self.xNormal = nor[0]
        self.yNormal = nor[1]
        self.zNormal = nor[2]
        self.radius = r
        self.sensor_id = sensor_id

        self.createVirtualDisk()

        return self

    def createVirtualDisk(self):
        """
        Create geometry of circular sensor

        Returns
        -------
        vertices: array
            The vertices of sensor's geometry
        normals: array
            The normal vectors of each vertices in sensor's geometry
        triangles: array
            The triangles of sensor's geometry

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

        sensor_shape = Shape(
            TriangleSet(vertices, triangles, normals),
            Material(
                name="Sensor",
                ambient=Color3(0),
                specular=Color3(0),
                shininess=1,
                transparency=0,
            ),
        )

        self.shape = sensor_shape

    def equal(self, xSite, ySite, zSite):
        """
        Check if the coordinate is equal to the position of sensor

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

        return self.xSite == xSite and self.ySite == ySite and self.zSite == zSite

    def getGeometry(self):
        """
        Get geometry of sensor

        Returns
        -------
        vertices: array
            The vertices of sensor's geometry
        normals: array
            The normal vectors of each vertices in sensor's geometry
        triangles: array
            The triangles of sensor's geometry

        """

        # return vertice list, indexlist
        vertices = VectorFloat(flatten(self.shape.geometry.pointList))
        normals = VectorFloat(flatten(self.shape.geometry.normalList))
        triangles = VectorUint(flatten(self.shape.geometry.indexList))
        return vertices, triangles, normals

    def getOpticalProperties(self):
        """
        Get optical properties of sensor

        Returns
        -------
        refl: float
            The reflection
        specular: float
            The specular
        trans: float
            The tranparency
        roughness: float
            The roughness

        """

        # return reflection, specular, transmission
        trans = self.shape.appearance.transparency
        refl = self.shape.appearance.ambient.red / 255.0
        specular = self.shape.appearance.specular.red / 255.0
        roughness = 1.0 - self.shape.appearance.shininess

        return refl, specular, trans, roughness


def addVirtualSensors(scene, virtual_sensor_triangle_dict, list_virtual_sensor):
    """
    Adds virtual sensors to the scene.

    Parameters
    ----------
    scene : libspice_core.Scene
        The photon mapping scene used to run the simulation
    virtual_sensor_triangle_dict : dict
        The dictionary of the triangles of sensors
    list_virtual_sensor : array
        The list of virtual sensor

    Returns
    -------
        Add all the mesh of virtual sensors to the scene

    """
    lastTriangleId = scene.nFaces()

    for i in range(len(list_virtual_sensor)):
        sensor = list_virtual_sensor[i]
        if sensor.type != "VirtualSensor":
            return

        vertices, triangles, normals = sensor.getGeometry()
        #
        scene.addVirtualSensorInfos(vertices, triangles, normals)

        #
        for j in triangles:
            virtual_sensor_triangle_dict[lastTriangleId + j] = sensor.sensor_id

        lastTriangleId = scene.nFaces()


def addFaceSensors(scene, face_sensor_triangle_dict, list_face_sensor):
    """
    Adds face sensors to the scene.

    Parameters
    ----------
    scene : libspice_core.Scene
        The photon mapping scene used to run the simulation
    face_sensor_triangle_dict : dict
        The dictionary of the triangles of sensors
    list_face_sensor : array
        The list of face sensor

    Returns
    -------
        Add all the mesh of face sensors to the scene

    """

    lastTriangleId = scene.nFaces()

    for i in range(len(list_face_sensor)):
        sensor = list_face_sensor[i]
        if sensor.type != "FaceSensor":
            return

        vertices, triangles, normals = sensor.getGeometry()
        refl, specular, trans, roughness = sensor.getOpticalProperties()
        #
        scene.addFaceSensorInfos(
            vertices,
            triangles,
            normals,
            "sensor" + str(i),
            refl,
            specular,
            trans,
            roughness,
        )
        #
        for j in triangles:
            face_sensor_triangle_dict[lastTriangleId + j] = sensor.sensor_id

        lastTriangleId = scene.nFaces()


def findIndexOfDiskSensorInList(list_sensor, x, y, z):
    """
    Find the index of a disk shape sensor while knowing its position

    Parameters
    ----------
    list_sensor : Array
        The list of the sensor in the scene
    x : float
        x coordinate
    y : float
        y coordinate
    z : float
        z coordinate

    Returns
    -------
        if not found, return -1
        if found, return the index of the sensor

    """

    for i in range(len(list_sensor)):
        if list_sensor[i].equal(x, y, z):
            return i
    return -1


# add sensor to a scene of PlantGL to visualize
def addSensorPgl(sc, list_sensor):
    """
    Add the sensors to the PlantGL scene to visualize the scene

    Parameters
    ----------
    sc : Lscene
        The plantgl scene
    list_sensor : array
        The list of sensors

    Returns
    -------
        A PlantGL Scene with the sensors

    """
    pglScene = Scene()

    for i in range(len(list_sensor)):
        sensor_sh = list_sensor[i].shape
        pglScene.add(sensor_sh)

    return Scene([pglScene, sc])
