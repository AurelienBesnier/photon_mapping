from openalea.photonmap.common.tools import wavelength2rgb, flatten

def test_flatten():
    l_test = [[1,2,3],[4]]
    assert flatten(l_test) == [1,2,3,4]

def test_wavelength2rgb():
    convert = wavelength2rgb(385.0)
    assert convert[1] == 0.0 and convert[2] == 1.0 and convert[0] != 0.0

    convert = wavelength2rgb(480.0)
    assert convert[0] == 0.0 and convert[2] == 1.0 and convert[1] != 0.0

    convert = wavelength2rgb(500.0)
    assert convert[0] == 0.0 and convert[1] == 1.0 and convert[2] != 0.0

    convert = wavelength2rgb(600.0)
    assert convert[0] == 1.0 and convert[2] == 0.0 and convert[1] != 0.0

    convert = wavelength2rgb(700.0)
    assert convert[0] == 1.0 and convert[1] == 0.0 and convert[2] == 0.0

    convert = wavelength2rgb(6546.0)
    assert convert[0] == 1.0 and convert[1] == 1.0 and convert[2] == 1.0
