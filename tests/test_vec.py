from openalea.photonmap import Vec3


def test_vec3_create():
    u = Vec3()
    assert u[0] == 0 and u[1] == 0 and u[2] == 0
    v = Vec3(1)
    assert v[0] == 1 and v[1] == 1 and v[2] == 1


def test_vec3_add():
    u = Vec3(2)
    v = Vec3(1) + u
    assert v[0] == 3 and v[1] == 3 and v[2] == 3


def test_vec3_mul():
    v = Vec3(2) * 2
    assert v[0] == 4 and v[1] == 4 and v[2] == 4


def test_vec3_div():
    v = Vec3(2) / 2.0
    assert v[0] == 1 and v[1] == 1 and v[2] == 1
