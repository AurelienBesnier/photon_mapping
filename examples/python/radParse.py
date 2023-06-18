from openalea.plantgl.all import *
from openalea.plantgl.scenegraph import *


def denormalize(f: float) -> int:
    return int(255 * f)


def read_rad(file: str):
    Viewer.start()
    with open(file, 'r') as f:
        lines = f.readlines()
        materials = {}
        shapes = {}
        sc = Scene()
        i = 0
        for _ in range(len(lines)):
            i += 1
            if i >= len(lines):
                break
            elif lines[i].startswith("#"):
                continue
            elif lines[i].startswith("void"):  # material
                li = lines[i].split(" ")
                type = li[1]
                name = li[2].strip("\n")
                if materials.get(name) is None:
                    if type == "plastic":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        spec = Color3(denormalize(float(li[3])), denormalize(float(li[3])), denormalize(float(li[3])))
                        roughness = float(li[4])
                        mat = {"name": name, "type": type, "color": color, "spec": spec, "roughness": roughness}
                        materials[name] = mat
                        i += 5
                    elif type == "metal":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        spec = Color3(denormalize(float(li[3])), denormalize(float(li[3])), denormalize(float(li[3])))
                        roughness = float(li[4])
                        mat = {"name": name, "type": type, "color": color, "spec": spec, "roughness": roughness}
                        materials[name] = mat
                        i += 5
                    elif type == "trans":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        spec = Color3(denormalize(float(li[3])), denormalize(float(li[3])), denormalize(float(li[3])))
                        roughness = float(li[4])
                        trans = float(li[5])
                        tspec = float(li[6])
                        mat = {"name": name, "type": type, "color": color, "spec": spec, "roughness": roughness, "trans": trans,
                               "tspec": tspec}
                        materials[name] = mat
                        i += 5
                    elif type == "light":
                        li = lines[i + 4].split(" ")
                        color = Color3(denormalize(float(li[0])), denormalize(float(li[1])), denormalize(float(li[2])))
                        mat = {"type": type, "color": color}
                        materials[name] = mat
                        i += 5
            else:
                keys = materials.keys()
                for k in keys:
                    if lines[i].startswith(k):
                        li = lines[i].split(" ")
                        material = li[0]
                        type = li[1]
                        name = li[2].strip("\n")
                        i += 3
                        vert = []
                        size = int(lines[i])
                        tmp = i + 1
                        nbCoords = int(size / 3)
                        if nbCoords > 2:
                            for j in range(tmp, tmp + nbCoords):
                                l = lines[j].split(" ")
                                vert.append((float(l[0]) / 100.0, float(l[1]) / 100.0, float(l[2]) / 100.0))
                                i = j
                                shapes[name] = {"vertices": vert, "type": type, "size": size, "material": material}
        for sh, val in shapes.items():
            mat_key = val["material"]
            mat = materials[mat_key]
            vert = val["vertices"]
            print(mat)
            s = Shape()
            nbCoords = int(val["size"] / 3)
            if nbCoords % 3 == 0:
                ts = TriangleSet(vert)
                i = 0
                indList = []
                while i < nbCoords:
                    ind = Index3(i, i + 1, i + 2)
                    indList.append(ind)
                    i += 3
                ts.indexList = Index3Array(indList)
                ts.computeNormalList()
                s.geometry = ts
                s.name = sh
                if mat["type"] == "light":
                    s.appearance = Material(Color3(mat["color"]))
                elif mat["type"] == "trans":
                    s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]), specular=Color3(mat["spec"]),
                                            shininess=1 - mat["roughness"], transparency=mat["trans"])
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                shininess=1 - mat["roughness"])
                    else:
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                specular=Color3(mat["spec"]), shininess=1 - mat["roughness"])
                s.appearance.name = mat["name"]
                sc.add(s)
            else:
                ts = TriangleSet(vert)
                i = 0
                indList = []
                while i < nbCoords:
                    ind = Index3(i, i + 1, i + 2)
                    ind2 = Index3(i, i + 2, i + 3)
                    indList.append(ind)
                    indList.append(ind2)
                    i += 4
                ts.indexList = Index3Array(indList)
                ts.computeNormalList()
                s.geometry = ts
                s.name = sh
                if mat["type"] == "light":
                    s.appearance = Material(Color3(mat["color"]))
                elif mat["type"] == "trans":
                    s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]), specular=Color3(mat["spec"]),
                                            shininess=1 - mat["roughness"], transparency=mat["trans"])
                else:
                    if Color3(mat["spec"]) == Color3(0, 0, 0):
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                shininess=1 - mat["roughness"])
                    else:
                        s.appearance = Material(name=mat["name"], ambient=Color3(mat["color"]),
                                                specular=Color3(mat["spec"]), shininess=1 - mat["roughness"])
                s.appearance.name = mat["name"]
                sc.add(s)
        sc.save("env.bgeom")
        sc.save("env.geom")
        sc.save("env.obj")
        print(materials)


if __name__ == "__main__":
    filename = "testChamber.rad"
    read_rad(filename)
