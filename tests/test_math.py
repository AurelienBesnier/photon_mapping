from openalea.photonmap.common.math import  denormalize, average_vector
from openalea.plantgl.all import Vector3

def test_denormalize():
    zero = denormalize(0.0)
    assert zero == 0

    maximum = denormalize(1.0)
    assert maximum == 255

    middle = denormalize(0.5)
    assert middle == 127


def test_average_vector():
    list_vector = [Vector3(0,0,0), Vector3(1,1,1)]

    average = average_vector(list_vector)
    assert average[0] == 0.5 and average[1] == 0.5 and average[2] == 0.5