from math import cos, pi, sin

from openalea.plantgl.all import Index3, Shape, TriangleSet, Vector3

# This module consist the mathematical functions using in this project


def denormalize(f: float) -> int:
    """
    Convert a value from range (0 - 1) to (0 - 255)

    Parameters
    ----------
    f: float
        The value to convert

    """

    return int(255 * f)


def spherical_to_cartesian(theta, phi, x_seg, y_seg):
    """
    Convert the quaternion of object from angle(theta, phi) to Vec3(x,y,z)

    Parameters
    ----------
    theta: float
        The angle theta
    phi: float
        The angle phi
    x_seg: int
        The number of x segment
    y_seg: int
        The number of y segment

    """

    theta = theta * pi / 2 / y_seg
    phi = phi * 2 * pi / x_seg
    return Vector3(cos(phi) * sin(theta), cos(theta), sin(phi) * sin(theta))


def cross_vector(a, b):
    """
    Calculate the cross product of two vector

    Parameters
    ----------
    a: Vec3
        The first vector
    b: Vec3
        The second vector

    """

    res = Vector3(0, 0, 0)
    res[0] = a[1] * b[2] - b[1] * a[2]
    res[1] = -a[0] * b[2] + b[0] * a[2]
    res[2] = a[0] * b[1] - b[0] * a[1]
    return res


def orthonormal_basis(n):
    """
    Calculate the axis orthogonal from the vector normal

    Parameters
    ----------
    n: Vec3
        The normal vector (first axe)

    Returns
    -------
    t: Vec3
        The second axe
    b: Vec3
        The third axe

    """
    if abs(n[1]) < 0.9:
        t = cross_vector(n, Vector3(0, 1, 0))
    else:
        t = cross_vector(n, Vector3(0, 0, -1))

    t.normalize()
    b = cross_vector(t, n)
    b.normalize()

    return t, b


def geo_hemisphere(centre, normal, rayon):
    """
    Generate the geometry of a hemisphere

    Parameters
    ----------
    centre: Vec3
        The center of sphere
    normal: Vec3
        The normal vector
    rayon: float
        The radius of sphere

    Returns
    -------
        A Shape PlantGL

    """

    vertices = []
    triangles = []
    normals = []

    x_segment = 10
    y_segment = 5

    for i in range(y_segment):
        for j in range(x_segment):
            v1 = spherical_to_cartesian(i, j, x_segment, y_segment)
            v2 = spherical_to_cartesian(i, j + 1, x_segment, y_segment)
            v3 = spherical_to_cartesian(i + 1, j, x_segment, y_segment)
            v4 = spherical_to_cartesian(i + 1, j + 1, x_segment, y_segment)
            # add vert
            v_count = len(vertices)
            vertices.append(v1)
            vertices.append(v2)
            vertices.append(v3)
            vertices.append(v4)

            # add normal:: normals et vertices sont egaux car c'est une sphere unité
            normals.append(v1)
            normals.append(v2)
            normals.append(v3)
            normals.append(v4)

            # add triangle
            triangles.append(Index3(v_count, v_count + 1, v_count + 2))
            triangles.append(Index3(v_count + 1, v_count + 2, v_count + 3))

    # apply transform
    t, b = orthonormal_basis(normal)
    for i, v in enumerate(vertices):
        v_r = Vector3(0, 0, 0)
        v_r[0] = v[0] * t[0] + v[1] * normal[0] + v[2] * b[0]
        v_r[1] = v[0] * t[1] + v[1] * normal[1] + v[2] * b[1]
        v_r[2] = v[0] * t[2] + v[1] * normal[2] + v[2] * b[2]
        vertices[i] = rayon * v_r + centre

    return Shape(TriangleSet(vertices, triangles, normals))


def average_vector(list_vectors):
    """
    Calculate the average vector of a list

    Parameters
    ----------
    list_vectors: array
        The list of vector

    """

    v_sum = Vector3(0, 0, 0)
    for v in list_vectors:
        v_sum += v

    v_sum /= len(list_vectors)

    return v_sum
