import pathlib
from openalea.photonmap.reader.read_properties import setup_dataset_materials

filepath = pathlib.Path(__file__).parent.resolve()

def test_setup_materials():
    path = str(filepath / "PO")
    materials_r, materials_s, materials_t = setup_dataset_materials(
        400, 500, path)

    assert materials_r and materials_s and materials_t