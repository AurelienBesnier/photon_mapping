import pathlib
from openalea.photonmap.reader.read_rad_geo import read_rad

filepath = pathlib.Path(__file__).parent.resolve()

def test_read_rad():
    sc = read_rad(filepath / "testChamber.rad", scale_factor=1, invert_normals=False)
    assert sc is not None