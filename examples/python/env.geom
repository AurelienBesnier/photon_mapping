TriangleSet Geometry_140498566425416 { 
    PointList [ 
        <0,0,0>, 
        <0,0,1.94>, 
        <2.4,0,1.94>, 
        <2.4,0,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material cloison_Alu { 
    Ambient 158
    Diffuse 1.61392
    Shininess 1
}


Shape mur_gauche { 
    Id  1596238240
    Geometry  Geometry_140498566425416
    Appearance  cloison_Alu
}


TriangleSet Geometry_140498566427208 { 
    PointList [ 
        <0,1.84,0>, 
        <2.4,1.84,0>, 
        <2.4,1.84,1.94>, 
        <0,1.84,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material cloison_Alu { 
    Ambient 158
    Diffuse 1.61392
    Shininess 1
}


Shape mur_droit { 
    Id  1596239664
    Geometry  Geometry_140498566427208
    Appearance  cloison_Alu
}


TriangleSet Geometry_140498566427976 { 
    PointList [ 
        <0,0,0>, 
        <0,1.84,0>, 
        <0,1.84,1.94>, 
        <0,0,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material cloison_Plastique { 
    Ambient 193
    Diffuse 1.32124
    Shininess 1
}


Shape mur_arriere { 
    Id  1596240800
    Geometry  Geometry_140498566427976
    Appearance  cloison_Plastique
}


TriangleSet Geometry_140498566428776 { 
    PointList [ 
        <2.4,0,0>, 
        <2.4,0,1.94>, 
        <2.4,1.84,1.94>, 
        <2.4,1.84,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material cloison_Plastique { 
    Ambient 193
    Diffuse 1.32124
    Shininess 1
}


Shape mur_avant { 
    Id  1596241568
    Geometry  Geometry_140498566428776
    Appearance  cloison_Plastique
}


TriangleSet Geometry_140498566429576 { 
    PointList [ 
        <0.06,0.06,1.94>, 
        <0.06,0.06,2.15>, 
        <2.34,0.06,2.15>, 
        <2.34,0.06,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape mur_gauche_plafond { 
    Id  1596242368
    Geometry  Geometry_140498566429576
    Appearance  mirroir
}


TriangleSet Geometry_140498566430408 { 
    PointList [ 
        <0.06,0,1.94>, 
        <0.06,0.06,1.94>, 
        <2.34,0.06,1.94>, 
        <2.34,0,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond_mur_gauche { 
    Id  1596243232
    Geometry  Geometry_140498566430408
    Appearance  mirroir
}


TriangleSet Geometry_140498566431208 { 
    PointList [ 
        <0.06,1.78,1.94>, 
        <2.34,1.78,1.94>, 
        <2.34,1.78,2.15>, 
        <0.06,1.78,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape mur_droit_plafond { 
    Id  1596244000
    Geometry  Geometry_140498566431208
    Appearance  mirroir
}


TriangleSet Geometry_140498566432008 { 
    PointList [ 
        <0.06,1.78,1.94>, 
        <0.06,1.84,1.94>, 
        <2.34,1.84,1.94>, 
        <2.34,1.78,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond_mur_droit { 
    Id  1596244800
    Geometry  Geometry_140498566432008
    Appearance  mirroir
}


TriangleSet Geometry_140498566432808 { 
    PointList [ 
        <0.06,0.06,1.94>, 
        <0.06,1.78,1.94>, 
        <0.06,1.78,2.15>, 
        <0.06,0.06,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape mur_arriere_plafond { 
    Id  1596245600
    Geometry  Geometry_140498566432808
    Appearance  mirroir
}


TriangleSet Geometry_140498566433672 { 
    PointList [ 
        <0,0,1.94>, 
        <0,1.84,1.94>, 
        <0.06,1.84,1.94>, 
        <0.06,0,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond_mur_arriere { 
    Id  1596246528
    Geometry  Geometry_140498566433672
    Appearance  mirroir
}


TriangleSet Geometry_140498566434472 { 
    PointList [ 
        <2.34,0.06,1.94>, 
        <2.34,0.06,2.15>, 
        <2.34,1.78,2.15>, 
        <2.34,1.78,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape mur_avant_plafond { 
    Id  1596247264
    Geometry  Geometry_140498566434472
    Appearance  mirroir
}


TriangleSet Geometry_140498566435272 { 
    PointList [ 
        <2.4,0,1.94>, 
        <2.34,0,1.94>, 
        <2.34,1.84,1.94>, 
        <2.4,1.84,1.94>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond_mur_avant { 
    Id  1596248064
    Geometry  Geometry_140498566435272
    Appearance  mirroir
}


TriangleSet Geometry_140498566436072 { 
    PointList [ 
        <0.06,0.06,2.15>, 
        <0.06,1.78,2.15>, 
        <0.8,1.78,2.15>, 
        <0.8,0.06,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond1 { 
    Id  1596248864
    Geometry  Geometry_140498566436072
    Appearance  mirroir
}


TriangleSet Geometry_140498566436872 { 
    PointList [ 
        <0.8,1.36,2.15>, 
        <0.8,1.78,2.15>, 
        <1.6,1.78,2.15>, 
        <1.6,1.36,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond2 { 
    Id  1596249664
    Geometry  Geometry_140498566436872
    Appearance  mirroir
}


TriangleSet Geometry_140498566437672 { 
    PointList [ 
        <1.6,1.78,2.15>, 
        <2.34,1.78,2.15>, 
        <2.34,0.06,2.15>, 
        <1.6,0.06,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond3 { 
    Id  1596250464
    Geometry  Geometry_140498566437672
    Appearance  mirroir
}


TriangleSet Geometry_140498566438472 { 
    PointList [ 
        <0.8,0.06,2.15>, 
        <0.8,0.48,2.15>, 
        <1.6,0.48,2.15>, 
        <1.6,0.06,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mirroir { 
    Ambient Black
    Shininess 1
}


Shape plafond4 { 
    Id  1596251264
    Geometry  Geometry_140498566438472
    Appearance  mirroir
}


TriangleSet Geometry_140498566439272 { 
    PointList [ 
        <0.8,0.48,2.15>, 
        <0.8,1.36,2.15>, 
        <1.6,1.36,2.15>, 
        <1.6,0.48,2.15>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_Centre { 
    Ambient Black
    Shininess 1
}


Shape plafond_Centre { 
    Id  1596252064
    Geometry  Geometry_140498566439272
    Appearance  mat_Centre
}


TriangleSet Geometry_140498566440200 { 
    PointList [ 
        <0,0,0>, 
        <2.4,0,0>, 
        <2.4,1.84,0>, 
        <0,1.84,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material carrelage { 
    Ambient 73
    Shininess 1
}


Shape sol { 
    Id  1596253120
    Geometry  Geometry_140498566440200
    Appearance  carrelage
}


TriangleSet Geometry_140498566441000 { 
    PointList [ 
        <0,0.47,0.9>, 
        <2.04,0.47,0.9>, 
        <2.04,1.37,0.9>, 
        <0,1.37,0.9>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_table { 
    Ambient 7
    Shininess 1
}


Shape table { 
    Id  1596253792
    Geometry  Geometry_140498566441000
    Appearance  mat_table
}


TriangleSet Geometry_140498566441800 { 
    PointList [ 
        <0,0.47,0.86>, 
        <0,1.37,0.86>, 
        <2.04,1.37,0.86>, 
        <2.04,0.47,0.86>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_table { 
    Ambient 7
    Shininess 1
}


Shape table_dessous { 
    Id  1596254592
    Geometry  Geometry_140498566441800
    Appearance  mat_table
}


TriangleSet Geometry_140498566442600 { 
    PointList [ 
        <0,1.37,0.86>, 
        <0,1.37,0.9>, 
        <2.04,1.37,0.9>, 
        <2.04,1.37,0.86>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_table { 
    Ambient 7
    Shininess 1
}


Shape table_cote_droit { 
    Id  1596255392
    Geometry  Geometry_140498566442600
    Appearance  mat_table
}


TriangleSet Geometry_140498566443400 { 
    PointList [ 
        <0,0.47,0.9>, 
        <0,0.47,0.86>, 
        <2.04,0.47,0.86>, 
        <2.04,0.47,0.9>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_table { 
    Ambient 7
    Shininess 1
}


Shape table_cote_gauche { 
    Id  1596256192
    Geometry  Geometry_140498566443400
    Appearance  mat_table
}


TriangleSet Geometry_140498566444200 { 
    PointList [ 
        <2.04,0.47,0.9>, 
        <2.04,0.47,0.86>, 
        <2.04,1.37,0.86>, 
        <2.04,1.37,0.9>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_table { 
    Ambient 7
    Shininess 1
}


Shape table_cote_avant { 
    Id  1596256992
    Geometry  Geometry_140498566444200
    Appearance  mat_table
}


TriangleSet Geometry_140498566445000 { 
    PointList [ 
        <0,0.47,0.86>, 
        <0,0.47,0.9>, 
        <0,1.37,0.9>, 
        <0,1.37,0.86>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material mat_table { 
    Ambient 7
    Shininess 1
}


Shape table_cote_arriere { 
    Id  1596257792
    Geometry  Geometry_140498566445000
    Appearance  mat_table
}


TriangleSet Geometry_140498566445800 { 
    PointList [ 
        <0.75625,0.177,2.06>, 
        <0.75625,0.174195,2.05229>, 
        <0.75625,0.167092,2.04818>, 
        <0.75625,0.159011,2.0496>, 
        <0.75625,0.15373,2.05588>, 
        <0.75625,0.153716,2.06408>, 
        <0.75625,0.158978,2.07038>, 
        <0.75625,0.167054,2.07182>, 
        <0.75625,0.174171,2.06774>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CAvantZ1 { 
    Id  1596258592
    Geometry  Geometry_140498566445800
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566447160 { 
    PointList [ 
        <0.74375,0.177,2.06>, 
        <0.74375,0.174195,2.06771>, 
        <0.74375,0.167092,2.07182>, 
        <0.74375,0.159011,2.0704>, 
        <0.74375,0.15373,2.06412>, 
        <0.74375,0.153716,2.05592>, 
        <0.74375,0.158978,2.04962>, 
        <0.74375,0.167054,2.04818>, 
        <0.74375,0.174171,2.05226>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CArriereZ1 { 
    Id  1596260016
    Geometry  Geometry_140498566447160
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566448520 { 
    PointList [ 
        <0.75625,1.687,2.06>, 
        <0.75625,1.6842,2.05229>, 
        <0.75625,1.67709,2.04818>, 
        <0.75625,1.66901,2.0496>, 
        <0.75625,1.66373,2.05588>, 
        <0.75625,1.66372,2.06408>, 
        <0.75625,1.66898,2.07038>, 
        <0.75625,1.67705,2.07182>, 
        <0.75625,1.68417,2.06774>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CAvantZ2 { 
    Id  1596261376
    Geometry  Geometry_140498566448520
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566449880 { 
    PointList [ 
        <0.74375,1.687,2.06>, 
        <0.74375,1.6842,2.06771>, 
        <0.74375,1.67709,2.07182>, 
        <0.74375,1.66901,2.0704>, 
        <0.74375,1.66373,2.06412>, 
        <0.74375,1.66372,2.05592>, 
        <0.74375,1.66898,2.04962>, 
        <0.74375,1.67705,2.04818>, 
        <0.74375,1.68417,2.05226>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CArriereZ2 { 
    Id  1596262736
    Geometry  Geometry_140498566449880
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566451240 { 
    PointList [ 
        <1.65625,0.177,2.06>, 
        <1.65625,0.174195,2.05229>, 
        <1.65625,0.167092,2.04818>, 
        <1.65625,0.159011,2.0496>, 
        <1.65625,0.15373,2.05588>, 
        <1.65625,0.153716,2.06408>, 
        <1.65625,0.158978,2.07038>, 
        <1.65625,0.167054,2.07182>, 
        <1.65625,0.174171,2.06774>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CAvantZ3 { 
    Id  1596264096
    Geometry  Geometry_140498566451240
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566452600 { 
    PointList [ 
        <1.64375,0.177,2.06>, 
        <1.64375,0.174195,2.06771>, 
        <1.64375,0.167092,2.07182>, 
        <1.64375,0.159011,2.0704>, 
        <1.64375,0.15373,2.06412>, 
        <1.64375,0.153716,2.05592>, 
        <1.64375,0.158978,2.04962>, 
        <1.64375,0.167054,2.04818>, 
        <1.64375,0.174171,2.05226>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CArriereZ3 { 
    Id  1596265456
    Geometry  Geometry_140498566452600
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566453960 { 
    PointList [ 
        <1.65625,1.687,2.06>, 
        <1.65625,1.6842,2.05229>, 
        <1.65625,1.67709,2.04818>, 
        <1.65625,1.66901,2.0496>, 
        <1.65625,1.66373,2.05588>, 
        <1.65625,1.66372,2.06408>, 
        <1.65625,1.66898,2.07038>, 
        <1.65625,1.67705,2.07182>, 
        <1.65625,1.68417,2.06774>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CAvantZ4 { 
    Id  1596266816
    Geometry  Geometry_140498566453960
    Appearance  EcranTotal
}


TriangleSet Geometry_140498566455320 { 
    PointList [ 
        <1.64375,1.687,2.06>, 
        <1.64375,1.6842,2.06771>, 
        <1.64375,1.67709,2.07182>, 
        <1.64375,1.66901,2.0704>, 
        <1.64375,1.66373,2.06412>, 
        <1.64375,1.66372,2.05592>, 
        <1.64375,1.66898,2.04962>, 
        <1.64375,1.67705,2.04818>, 
        <1.64375,1.68417,2.05226>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material EcranTotal { 
    Ambient Black
    Shininess 1
}


Shape CArriereZ4 { 
    Id  1596268176
    Geometry  Geometry_140498566455320
    Appearance  EcranTotal
}


