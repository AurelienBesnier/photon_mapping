from openalea.plantgl.all import * 
from math import cos, sin, pi

#This module consist the mathematical functions using in this project 

def denormalize(f: float) -> int:
    return int(255 * f)

def sphericalToCartesian(theta, phi, x_seg, y_seg):
    theta = theta * pi / 2 / y_seg
    phi = phi * 2 * pi / x_seg
    return Vector3(cos(phi) * sin(theta), cos(theta), sin(phi) * sin(theta))

def crossVector(a, b):
    res = Vector3(0,0,0)
    res[0] = a[1] * b[2] - b[1] * a[2]
    res[1] = - a[0] * b[2] + b[0] * a[2]
    res[2] = a[0] * b[1] - b[0] * a[1] 
    return res

def orthonormalBasis(n):
    t = Vector3(0,0,0)
    b = Vector3(0,0,0)

    if abs(n[1]) < 0.9:
        t = crossVector(n, Vector3(0, 1, 0))
    else:
        t = crossVector(n, Vector3(0, 0, -1))
    
    t.normalize()
    b = crossVector(t, n)
    b.normalize()

    return t, b 

def geoHemisphere(centre, normal, rayon):
    vertices = []
    triangles = []
    normals = []

    x_segment = 10
    y_segment = 5
   
    for i in range(y_segment):
        theta = i * pi / 2 / y_segment
        for j in range(x_segment):
            phi = j * 2 * pi / x_segment
            v1 = sphericalToCartesian(i, j, x_segment, y_segment)
            v2 = sphericalToCartesian(i, j + 1, x_segment, y_segment)
            v3 = sphericalToCartesian(i + 1, j, x_segment, y_segment)
            v4 = sphericalToCartesian(i + 1, j + 1, x_segment, y_segment)
            #add vert
            v_count = len(vertices)
            vertices.append(v1)
            vertices.append(v2)
            vertices.append(v3)
            vertices.append(v4)
            
            #add normal:: normals et vertices sont egaux car c'est une sphere unité
            normals.append(v1)
            normals.append(v2)
            normals.append(v3)
            normals.append(v4)

            #add triangle
            triangles.append(Index3(v_count, v_count + 1, v_count + 2))
            triangles.append(Index3(v_count + 1, v_count + 2, v_count + 3))

    #apply transform
    t, b = orthonormalBasis(normal)
    for i, v in enumerate(vertices):
        v_r = Vector3(0,0,0)
        v_r[0] = v[0] * t[0] + v[1] * normal[0] + v[2] * b[0]
        v_r[1] = v[0] * t[1] + v[1] * normal[1] + v[2] * b[1]
        v_r[2] = v[0] * t[2] + v[1] * normal[2] + v[2] * b[2]
        vertices[i] = rayon * v_r + centre

    return Shape(TriangleSet(vertices, triangles, normals))
    

def averageVector(listVectors):
    sum = Vector3(0,0,0)
    for v in listVectors:
        sum = sum + v
    
    sum = sum / len(listVectors)

    return sum