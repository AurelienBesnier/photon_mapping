TriangleSet Geometry_140569335435768 { 
    PointList [ 
        <0,0,0>, 
        <24,0,0>, 
        <24,18.4,0>, 
        <0,18.4,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Sol { 
    Ambient 94
    Specular 25
    Shininess 1
}


Shape dallage { 
    Id  3645794048
    Geometry  Geometry_140569335435768
    Appearance  Sol
}


TriangleSet Geometry_140569421518536 { 
    PointList [ 
        <0,0,0>, 
        <0,0,19.7>, 
        <24,0,19.7>, 
        <24,0,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurMetal { 
    Ambient 164
    Diffuse 1.55488
    Specular 76
    Shininess 1
}


Shape paroix0 { 
    Id  3731616320
    Geometry  Geometry_140569421518536
    Appearance  MurMetal
}


TriangleSet Geometry_140569419117624 { 
    PointList [ 
        <24,18.4,0>, 
        <24,18.4,19.7>, 
        <0,18.4,19.7>, 
        <0,18.4,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurMetal { 
    Ambient 164
    Diffuse 1.55488
    Specular 76
    Shininess 1
}


Shape paroix1 { 
    Id  3724589696
    Geometry  Geometry_140569419117624
    Appearance  MurMetal
}


TriangleSet Geometry_140569418462664 { 
    PointList [ 
        <0,0,0>, 
        <0,18.4,0>, 
        <0,18.4,19.7>, 
        <0,0,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurBlanc { 
    Ambient 196
    Diffuse 1.30102
    Specular 51
    Shininess 1
}


Shape paroiy0 { 
    Id  3724585888
    Geometry  Geometry_140569418462664
    Appearance  MurBlanc
}


TriangleSet Geometry_140569418484728 { 
    PointList [ 
        <24,18.4,0>, 
        <24,0,0>, 
        <24,0,19.7>, 
        <24,18.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurBlanc { 
    Ambient 196
    Diffuse 1.30102
    Specular 51
    Shininess 1
}


Shape paroiy1 { 
    Id  3724585968
    Geometry  Geometry_140569418484728
    Appearance  MurBlanc
}


TriangleSet Geometry_140569379623896 { 
    PointList [ 
        <23.75,5.7,18.8>, 
        <24.25,5.7,18.8>, 
        <24.25,12.7,18.8>, 
        <23.75,12.7,18.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape linteau { 
    Id  3729456448
    Geometry  Geometry_140569379623896
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569418645224 { 
    PointList [ 
        <23.75,12.7,18.8>, 
        <24.25,12.7,18.8>, 
        <24.25,5.7,18.8>, 
        <23.75,5.7,18.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape linteauR { 
    Id  3689960592
    Geometry  Geometry_140569418645224
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569337703800 { 
    PointList [ 
        <23.75,12.7,0>, 
        <23.75,12.7,18.8>, 
        <24.25,12.7,18.8>, 
        <24.25,12.7,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape montantG { 
    Id  3648038304
    Geometry  Geometry_140569337703800
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569337704696 { 
    PointList [ 
        <24.25,12.7,0>, 
        <24.25,12.7,18.8>, 
        <23.75,12.7,18.8>, 
        <23.75,12.7,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape montantGr { 
    Id  3648040784
    Geometry  Geometry_140569337704696
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569375442680 { 
    PointList [ 
        <23.75,5.7,0>, 
        <23.75,5.7,18.8>, 
        <24.25,5.7,18.8>, 
        <24.25,5.7,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape montantD { 
    Id  3685773520
    Geometry  Geometry_140569375442680
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569375446216 { 
    PointList [ 
        <24.25,5.7,0>, 
        <24.25,5.7,18.8>, 
        <23.75,5.7,18.8>, 
        <23.75,5.7,0>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape montantDr { 
    Id  3685782304
    Geometry  Geometry_140569375446216
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569375447160 { 
    PointList [ 
        <1.555,1.65,21.55>, 
        <3.245,1.65,21.55>, 
        <3.245,1.4154,21.772>, 
        <1.555,1.4154,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref10Narrow { 
    Id  3685783248
    Geometry  Geometry_140569375447160
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569418495528 { 
    PointList [ 
        <3.245,1.65,21.55>, 
        <1.555,1.65,21.55>, 
        <1.555,1.4154,21.772>, 
        <3.245,1.4154,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref10NarrowR { 
    Id  3728831680
    Geometry  Geometry_140569418495528
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569414612888 { 
    PointList [ 
        <3.245,1.65,21.55>, 
        <1.555,1.65,21.55>, 
        <1.555,1.93618,21.8>, 
        <3.245,1.93618,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref10Wide { 
    Id  3728865520
    Geometry  Geometry_140569414612888
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569418479016 { 
    PointList [ 
        <1.555,1.65,21.55>, 
        <3.245,1.65,21.55>, 
        <3.245,1.93618,21.8>, 
        <1.555,1.93618,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref10WideR { 
    Id  3724949680
    Geometry  Geometry_140569418479016
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569419126520 { 
    PointList [ 
        <20.655,1.8,21.55>, 
        <22.345,1.8,21.55>, 
        <22.345,1.5654,21.772>, 
        <20.655,1.5654,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref11Narrow { 
    Id  3729462608
    Geometry  Geometry_140569419126520
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569418482248 { 
    PointList [ 
        <22.345,1.8,21.55>, 
        <20.655,1.8,21.55>, 
        <20.655,1.5654,21.772>, 
        <22.345,1.5654,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref11NarrowR { 
    Id  3729463376
    Geometry  Geometry_140569418482248
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569415871016 { 
    PointList [ 
        <22.345,1.8,21.55>, 
        <20.655,1.8,21.55>, 
        <20.655,2.08618,21.8>, 
        <22.345,2.08618,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref11Wide { 
    Id  3683708592
    Geometry  Geometry_140569415871016
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569415872120 { 
    PointList [ 
        <20.655,1.8,21.55>, 
        <22.345,1.8,21.55>, 
        <22.345,2.08618,21.8>, 
        <20.655,2.08618,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref11WideR { 
    Id  3726207808
    Geometry  Geometry_140569415872120
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569415875080 { 
    PointList [ 
        <22.475,16.59,21.55>, 
        <20.785,16.59,21.55>, 
        <20.785,16.8246,21.772>, 
        <22.475,16.8246,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref12Narrow { 
    Id  3726208976
    Geometry  Geometry_140569415875080
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569415875848 { 
    PointList [ 
        <20.785,16.59,21.55>, 
        <22.475,16.59,21.55>, 
        <22.475,16.8246,21.772>, 
        <20.785,16.8246,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref12NarrowR { 
    Id  3726211936
    Geometry  Geometry_140569415875848
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569415876728 { 
    PointList [ 
        <20.785,16.59,21.55>, 
        <22.475,16.59,21.55>, 
        <22.475,16.3038,21.8>, 
        <20.785,16.3038,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref12Wide { 
    Id  3726212784
    Geometry  Geometry_140569415876728
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377609608 { 
    PointList [ 
        <22.475,16.59,21.55>, 
        <20.785,16.59,21.55>, 
        <20.785,16.3038,21.8>, 
        <22.475,16.3038,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref12WideR { 
    Id  3687945600
    Geometry  Geometry_140569377609608
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377610616 { 
    PointList [ 
        <1.555,16.66,21.55>, 
        <3.245,16.66,21.55>, 
        <3.245,16.4254,21.772>, 
        <1.555,16.4254,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref13Narrow { 
    Id  3687958240
    Geometry  Geometry_140569377610616
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377623928 { 
    PointList [ 
        <3.245,16.66,21.55>, 
        <1.555,16.66,21.55>, 
        <1.555,16.4254,21.772>, 
        <3.245,16.4254,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref13NarrowR { 
    Id  3687960080
    Geometry  Geometry_140569377623928
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377624312 { 
    PointList [ 
        <3.245,16.66,21.55>, 
        <1.555,16.66,21.55>, 
        <1.555,16.9462,21.8>, 
        <3.245,16.9462,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref13Wide { 
    Id  3687948000
    Geometry  Geometry_140569377624312
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377627016 { 
    PointList [ 
        <1.555,16.66,21.55>, 
        <3.245,16.66,21.55>, 
        <3.245,16.9462,21.8>, 
        <1.555,16.9462,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref13WideR { 
    Id  3687963104
    Geometry  Geometry_140569377627016
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377627784 { 
    PointList [ 
        <6.515,1.76,21.5041>, 
        <8.205,1.76,21.5041>, 
        <8.205,1.49041,21.682>, 
        <6.515,1.49041,21.682>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref20Narrow { 
    Id  3687963872
    Geometry  Geometry_140569377627784
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377628552 { 
    PointList [ 
        <8.205,1.76,21.5041>, 
        <6.515,1.76,21.5041>, 
        <6.515,1.49041,21.682>, 
        <8.205,1.49041,21.682>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref20NarrowR { 
    Id  3687964640
    Geometry  Geometry_140569377628552
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377629320 { 
    PointList [ 
        <8.205,1.76,21.5041>, 
        <6.515,1.76,21.5041>, 
        <6.515,1.99842,21.8>, 
        <8.205,1.99842,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref20Wide { 
    Id  3687965408
    Geometry  Geometry_140569377629320
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377630088 { 
    PointList [ 
        <6.515,1.76,21.5041>, 
        <8.205,1.76,21.5041>, 
        <8.205,1.99842,21.8>, 
        <6.515,1.99842,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref20WideR { 
    Id  3687966176
    Geometry  Geometry_140569377630088
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377630856 { 
    PointList [ 
        <15.805,1.695,21.5437>, 
        <17.495,1.695,21.5437>, 
        <17.495,1.45553,21.7605>, 
        <15.805,1.45553,21.7605>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref21Narrow { 
    Id  3687966944
    Geometry  Geometry_140569377630856
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377631624 { 
    PointList [ 
        <17.495,1.695,21.5437>, 
        <15.805,1.695,21.5437>, 
        <15.805,1.45553,21.7605>, 
        <17.495,1.45553,21.7605>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref21NarrowR { 
    Id  3687967712
    Geometry  Geometry_140569377631624
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377632904 { 
    PointList [ 
        <17.495,1.695,21.5437>, 
        <15.805,1.695,21.5437>, 
        <15.805,1.97557,21.8>, 
        <17.495,1.97557,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref21Wide { 
    Id  3687968992
    Geometry  Geometry_140569377632904
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377633672 { 
    PointList [ 
        <15.805,1.695,21.5437>, 
        <17.495,1.695,21.5437>, 
        <17.495,1.97557,21.8>, 
        <15.805,1.97557,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref21WideR { 
    Id  3687969760
    Geometry  Geometry_140569377633672
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377634440 { 
    PointList [ 
        <17.585,16.7,21.55>, 
        <15.895,16.7,21.55>, 
        <15.895,16.9346,21.772>, 
        <17.585,16.9346,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref22Narrow { 
    Id  3687970528
    Geometry  Geometry_140569377634440
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377635240 { 
    PointList [ 
        <15.895,16.7,21.55>, 
        <17.585,16.7,21.55>, 
        <17.585,16.9346,21.772>, 
        <15.895,16.9346,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref22NarrowR { 
    Id  3687971296
    Geometry  Geometry_140569377635240
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377636040 { 
    PointList [ 
        <15.895,16.7,21.55>, 
        <17.585,16.7,21.55>, 
        <17.585,16.4138,21.8>, 
        <15.895,16.4138,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref22Wide { 
    Id  3687972096
    Geometry  Geometry_140569377636040
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377636840 { 
    PointList [ 
        <17.585,16.7,21.55>, 
        <15.895,16.7,21.55>, 
        <15.895,16.4138,21.8>, 
        <17.585,16.4138,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref22WideR { 
    Id  3687972896
    Geometry  Geometry_140569377636840
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377637640 { 
    PointList [ 
        <6.475,16.72,21.492>, 
        <8.165,16.72,21.492>, 
        <8.165,16.4415,21.6556>, 
        <6.475,16.4415,21.6556>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref23Narrow { 
    Id  3687973696
    Geometry  Geometry_140569377637640
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377638440 { 
    PointList [ 
        <8.165,16.72,21.492>, 
        <6.475,16.72,21.492>, 
        <6.475,16.4415,21.6556>, 
        <8.165,16.4415,21.6556>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref23NarrowR { 
    Id  3687974496
    Geometry  Geometry_140569377638440
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377639240 { 
    PointList [ 
        <8.165,16.72,21.492>, 
        <6.475,16.72,21.492>, 
        <6.475,16.9426,21.8>, 
        <8.165,16.9426,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref23Wide { 
    Id  3687975296
    Geometry  Geometry_140569377639240
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377640040 { 
    PointList [ 
        <6.475,16.72,21.492>, 
        <8.165,16.72,21.492>, 
        <8.165,16.9426,21.8>, 
        <6.475,16.9426,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref23WideR { 
    Id  3687976096
    Geometry  Geometry_140569377640040
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377640840 { 
    PointList [ 
        <1.79,6.195,21.55>, 
        <1.79,4.505,21.55>, 
        <1.5554,4.505,21.772>, 
        <1.5554,6.195,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref40Narrow { 
    Id  3687976896
    Geometry  Geometry_140569377640840
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377641640 { 
    PointList [ 
        <1.79,4.505,21.55>, 
        <1.79,6.195,21.55>, 
        <1.5554,6.195,21.772>, 
        <1.5554,4.505,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref40NarrowR { 
    Id  3687977696
    Geometry  Geometry_140569377641640
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377642440 { 
    PointList [ 
        <1.79,4.505,21.55>, 
        <1.79,6.195,21.55>, 
        <2.07618,6.195,21.8>, 
        <2.07618,4.505,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref40Wide { 
    Id  3687978496
    Geometry  Geometry_140569377642440
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377643240 { 
    PointList [ 
        <1.79,6.195,21.55>, 
        <1.79,4.505,21.55>, 
        <2.07618,4.505,21.8>, 
        <2.07618,6.195,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref40WideR { 
    Id  3687979296
    Geometry  Geometry_140569377643240
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377644040 { 
    PointList [ 
        <22.115,4.525,21.55>, 
        <22.115,6.215,21.55>, 
        <22.3496,6.215,21.772>, 
        <22.3496,4.525,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref41Narrow { 
    Id  3687980096
    Geometry  Geometry_140569377644040
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377644840 { 
    PointList [ 
        <22.115,6.215,21.55>, 
        <22.115,4.525,21.55>, 
        <22.3496,4.525,21.772>, 
        <22.3496,6.215,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref41NarrowR { 
    Id  3687980896
    Geometry  Geometry_140569377644840
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377645640 { 
    PointList [ 
        <22.115,6.215,21.55>, 
        <22.115,4.525,21.55>, 
        <21.8288,4.525,21.8>, 
        <21.8288,6.215,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref41Wide { 
    Id  3687981696
    Geometry  Geometry_140569377645640
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377646440 { 
    PointList [ 
        <22.115,4.525,21.55>, 
        <22.115,6.215,21.55>, 
        <21.8288,6.215,21.8>, 
        <21.8288,4.525,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref41WideR { 
    Id  3687982496
    Geometry  Geometry_140569377646440
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377647240 { 
    PointList [ 
        <22.285,13.775,21.55>, 
        <22.285,12.085,21.55>, 
        <22.0504,12.085,21.772>, 
        <22.0504,13.775,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref42Narrow { 
    Id  3687983296
    Geometry  Geometry_140569377647240
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377648040 { 
    PointList [ 
        <22.285,12.085,21.55>, 
        <22.285,13.775,21.55>, 
        <22.0504,13.775,21.772>, 
        <22.0504,12.085,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref42NarrowR { 
    Id  3687984096
    Geometry  Geometry_140569377648040
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377648840 { 
    PointList [ 
        <22.285,12.085,21.55>, 
        <22.285,13.775,21.55>, 
        <22.5712,13.775,21.8>, 
        <22.5712,12.085,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref42Wide { 
    Id  3687984896
    Geometry  Geometry_140569377648840
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377649640 { 
    PointList [ 
        <22.285,13.775,21.55>, 
        <22.285,12.085,21.55>, 
        <22.5712,12.085,21.8>, 
        <22.5712,13.775,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref42WideR { 
    Id  3687985696
    Geometry  Geometry_140569377649640
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377650440 { 
    PointList [ 
        <1.63,13.815,21.55>, 
        <1.63,12.125,21.55>, 
        <1.3954,12.125,21.772>, 
        <1.3954,13.815,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref43Narrow { 
    Id  3687986496
    Geometry  Geometry_140569377650440
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377651240 { 
    PointList [ 
        <1.63,12.125,21.55>, 
        <1.63,13.815,21.55>, 
        <1.3954,13.815,21.772>, 
        <1.3954,12.125,21.772>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref43NarrowR { 
    Id  3687987296
    Geometry  Geometry_140569377651240
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377652040 { 
    PointList [ 
        <1.63,12.125,21.55>, 
        <1.63,13.815,21.55>, 
        <1.91618,13.815,21.8>, 
        <1.91618,12.125,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref43Wide { 
    Id  3687988096
    Geometry  Geometry_140569377652040
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377652840 { 
    PointList [ 
        <1.63,13.815,21.55>, 
        <1.63,12.125,21.55>, 
        <1.91618,12.125,21.8>, 
        <1.91618,13.815,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape ref43WideR { 
    Id  3687988896
    Geometry  Geometry_140569377652840
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569377653640 { 
    PointList [ 
        <2.25,1.489,21.07>, 
        <2.25,1.51497,20.9987>, 
        <2.25,1.58073,20.9607>, 
        <2.25,1.6555,20.9739>, 
        <2.25,1.70431,21.032>, 
        <2.25,1.70431,21.108>, 
        <2.25,1.6555,21.1661>, 
        <2.25,1.58073,21.1793>, 
        <2.25,1.51497,21.1413>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV { 
    Id  3687989696
    Geometry  Geometry_140569377653640
    Appearance  ecran
}


TriangleSet Geometry_140569377655000 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.50991,20.9944>, 
        <2.4,1.4824,21.07>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR0 { 
    Id  3687991120
    Geometry  Geometry_140569377655000
    Appearance  ecran
}


TriangleSet Geometry_140569377655736 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.4824,21.07>, 
        <2.4,1.50991,21.1456>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR1 { 
    Id  3687991824
    Geometry  Geometry_140569377655736
    Appearance  ecran
}


TriangleSet Geometry_140569377656472 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.50991,21.1456>, 
        <2.4,1.57958,21.1858>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR2 { 
    Id  3687992560
    Geometry  Geometry_140569377656472
    Appearance  ecran
}


TriangleSet Geometry_140569377657208 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.57958,21.1858>, 
        <2.4,1.6588,21.1718>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR3 { 
    Id  3687993296
    Geometry  Geometry_140569377657208
    Appearance  ecran
}


TriangleSet Geometry_140569377657944 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.6588,21.1718>, 
        <2.4,1.71051,21.1102>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR4 { 
    Id  3687994032
    Geometry  Geometry_140569377657944
    Appearance  ecran
}


TriangleSet Geometry_140569377632392 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.71051,21.1102>, 
        <2.4,1.71051,21.0298>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR5 { 
    Id  3687968480
    Geometry  Geometry_140569377632392
    Appearance  ecran
}


TriangleSet Geometry_140569375447928 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.71051,21.0298>, 
        <2.4,1.6588,20.9682>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR6 { 
    Id  3685784016
    Geometry  Geometry_140569375447928
    Appearance  ecran
}


TriangleSet Geometry_140569375448664 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.6588,20.9682>, 
        <2.4,1.57958,20.9542>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR7 { 
    Id  3685784752
    Geometry  Geometry_140569375448664
    Appearance  ecran
}


TriangleSet Geometry_140569375449400 { 
    PointList [ 
        <2.55,1.6,21.07>, 
        <2.4,1.57958,20.9542>, 
        <2.4,1.50991,20.9944>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AR8 { 
    Id  3685785488
    Geometry  Geometry_140569375449400
    Appearance  ecran
}


TriangleSet Geometry_140569375450136 { 
    PointList [ 
        <2.613,1.528,21.07>, 
        <2.613,1.54484,21.1163>, 
        <2.613,1.5875,21.1409>, 
        <2.613,1.636,21.1324>, 
        <2.613,1.66766,21.0946>, 
        <2.613,1.66766,21.0454>, 
        <2.613,1.636,21.0076>, 
        <2.613,1.5875,20.9991>, 
        <2.613,1.54484,21.0237>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10ARx { 
    Id  3685786224
    Geometry  Geometry_140569375450136
    Appearance  ecran
}


TriangleSet Geometry_140569375451528 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.53106,21.1279>, 
        <2.4,1.51,21.07>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV0 { 
    Id  3685787616
    Geometry  Geometry_140569375451528
    Appearance  ecran
}


TriangleSet Geometry_140569415878440 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.51,21.07>, 
        <2.4,1.53106,21.0121>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV1 { 
    Id  3726213584
    Geometry  Geometry_140569415878440
    Appearance  ecran
}


TriangleSet Geometry_140569415879176 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.53106,21.0121>, 
        <2.4,1.58437,20.9814>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV2 { 
    Id  3726215264
    Geometry  Geometry_140569415879176
    Appearance  ecran
}


TriangleSet Geometry_140569415879912 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.58437,20.9814>, 
        <2.4,1.645,20.9921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV3 { 
    Id  3726216000
    Geometry  Geometry_140569415879912
    Appearance  ecran
}


TriangleSet Geometry_140569421519240 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.645,20.9921>, 
        <2.4,1.68457,21.0392>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV4 { 
    Id  3731855328
    Geometry  Geometry_140569421519240
    Appearance  ecran
}


TriangleSet Geometry_140569421519976 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.68457,21.0392>, 
        <2.4,1.68457,21.1008>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV5 { 
    Id  3731856064
    Geometry  Geometry_140569421519976
    Appearance  ecran
}


TriangleSet Geometry_140569421520712 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.68457,21.1008>, 
        <2.4,1.645,21.1479>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV6 { 
    Id  3731856800
    Geometry  Geometry_140569421520712
    Appearance  ecran
}


TriangleSet Geometry_140569421521448 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.645,21.1479>, 
        <2.4,1.58437,21.1586>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV7 { 
    Id  3731857536
    Geometry  Geometry_140569421521448
    Appearance  ecran
}


TriangleSet Geometry_140569421522184 { 
    PointList [ 
        <2.235,1.6,21.07>, 
        <2.4,1.58437,21.1586>, 
        <2.4,1.53106,21.1279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp10AV8 { 
    Id  3731858272
    Geometry  Geometry_140569421522184
    Appearance  ecran
}


TriangleSet Geometry_140569421522920 { 
    PointList [ 
        <21.65,1.911,20.95>, 
        <21.65,1.88503,20.8787>, 
        <21.65,1.81927,20.8407>, 
        <21.65,1.7445,20.8539>, 
        <21.65,1.69569,20.912>, 
        <21.65,1.69569,20.988>, 
        <21.65,1.7445,21.0461>, 
        <21.65,1.81927,21.0593>, 
        <21.65,1.88503,21.0213>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV { 
    Id  3731859008
    Geometry  Geometry_140569421522920
    Appearance  ecran
}


TriangleSet Geometry_140569421524312 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.89009,20.8744>, 
        <21.5,1.9176,20.95>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR0 { 
    Id  3731860400
    Geometry  Geometry_140569421524312
    Appearance  ecran
}


TriangleSet Geometry_140569421525048 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.9176,20.95>, 
        <21.5,1.89009,21.0256>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR1 { 
    Id  3731861136
    Geometry  Geometry_140569421525048
    Appearance  ecran
}


TriangleSet Geometry_140569421525784 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.89009,21.0256>, 
        <21.5,1.82042,21.0658>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR2 { 
    Id  3731861872
    Geometry  Geometry_140569421525784
    Appearance  ecran
}


TriangleSet Geometry_140569421526520 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.82042,21.0658>, 
        <21.5,1.7412,21.0518>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR3 { 
    Id  3731862608
    Geometry  Geometry_140569421526520
    Appearance  ecran
}


TriangleSet Geometry_140569421527256 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.7412,21.0518>, 
        <21.5,1.68949,20.9902>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR4 { 
    Id  3731863344
    Geometry  Geometry_140569421527256
    Appearance  ecran
}


TriangleSet Geometry_140569421527992 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.68949,20.9902>, 
        <21.5,1.68949,20.9098>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR5 { 
    Id  3731864080
    Geometry  Geometry_140569421527992
    Appearance  ecran
}


TriangleSet Geometry_140569421528728 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.68949,20.9098>, 
        <21.5,1.7412,20.8482>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR6 { 
    Id  3731864816
    Geometry  Geometry_140569421528728
    Appearance  ecran
}


TriangleSet Geometry_140569421529464 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.7412,20.8482>, 
        <21.5,1.82042,20.8342>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR7 { 
    Id  3731865552
    Geometry  Geometry_140569421529464
    Appearance  ecran
}


TriangleSet Geometry_140569421530200 { 
    PointList [ 
        <21.35,1.8,20.95>, 
        <21.5,1.82042,20.8342>, 
        <21.5,1.89009,20.8744>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AR8 { 
    Id  3731866288
    Geometry  Geometry_140569421530200
    Appearance  ecran
}


TriangleSet Geometry_140569421530936 { 
    PointList [ 
        <21.287,1.872,20.95>, 
        <21.287,1.85516,20.9963>, 
        <21.287,1.8125,21.0209>, 
        <21.287,1.764,21.0124>, 
        <21.287,1.73234,20.9746>, 
        <21.287,1.73234,20.9254>, 
        <21.287,1.764,20.8876>, 
        <21.287,1.8125,20.8791>, 
        <21.287,1.85516,20.9037>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11ARx { 
    Id  3731867024
    Geometry  Geometry_140569421530936
    Appearance  ecran
}


TriangleSet Geometry_140569421532328 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.86894,21.0079>, 
        <21.5,1.89,20.95>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV0 { 
    Id  3731868416
    Geometry  Geometry_140569421532328
    Appearance  ecran
}


TriangleSet Geometry_140569421533064 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.89,20.95>, 
        <21.5,1.86894,20.8921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV1 { 
    Id  3731869152
    Geometry  Geometry_140569421533064
    Appearance  ecran
}


TriangleSet Geometry_140569421533800 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.86894,20.8921>, 
        <21.5,1.81563,20.8614>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV2 { 
    Id  3731869888
    Geometry  Geometry_140569421533800
    Appearance  ecran
}


TriangleSet Geometry_140569421534536 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.81563,20.8614>, 
        <21.5,1.755,20.8721>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV3 { 
    Id  3731870624
    Geometry  Geometry_140569421534536
    Appearance  ecran
}


TriangleSet Geometry_140569421535272 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.755,20.8721>, 
        <21.5,1.71543,20.9192>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV4 { 
    Id  3731871360
    Geometry  Geometry_140569421535272
    Appearance  ecran
}


TriangleSet Geometry_140569421536008 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.71543,20.9192>, 
        <21.5,1.71543,20.9808>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV5 { 
    Id  3731872096
    Geometry  Geometry_140569421536008
    Appearance  ecran
}


TriangleSet Geometry_140569421536744 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.71543,20.9808>, 
        <21.5,1.755,21.0279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV6 { 
    Id  3731872832
    Geometry  Geometry_140569421536744
    Appearance  ecran
}


TriangleSet Geometry_140569421537480 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.755,21.0279>, 
        <21.5,1.81563,21.0386>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV7 { 
    Id  3731873568
    Geometry  Geometry_140569421537480
    Appearance  ecran
}


TriangleSet Geometry_140569421538216 { 
    PointList [ 
        <21.665,1.8,20.95>, 
        <21.5,1.81563,21.0386>, 
        <21.5,1.86894,21.0079>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp11AV8 { 
    Id  3731874304
    Geometry  Geometry_140569421538216
    Appearance  ecran
}


TriangleSet Geometry_140569421538952 { 
    PointList [ 
        <21.78,16.801,21.05>, 
        <21.78,16.775,20.9787>, 
        <21.78,16.7093,20.9407>, 
        <21.78,16.6345,20.9539>, 
        <21.78,16.5857,21.012>, 
        <21.78,16.5857,21.088>, 
        <21.78,16.6345,21.1461>, 
        <21.78,16.7093,21.1593>, 
        <21.78,16.775,21.1213>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV { 
    Id  3731875040
    Geometry  Geometry_140569421538952
    Appearance  ecran
}


TriangleSet Geometry_140569421540344 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.7801,20.9744>, 
        <21.63,16.8076,21.05>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR0 { 
    Id  3731876432
    Geometry  Geometry_140569421540344
    Appearance  ecran
}


TriangleSet Geometry_140569418483016 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.8076,21.05>, 
        <21.63,16.7801,21.1256>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR1 { 
    Id  3728819104
    Geometry  Geometry_140569418483016
    Appearance  ecran
}


TriangleSet Geometry_140569434333288 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.7801,21.1256>, 
        <21.63,16.7104,21.1658>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR2 { 
    Id  3744669376
    Geometry  Geometry_140569434333288
    Appearance  ecran
}


TriangleSet Geometry_140569434334024 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.7104,21.1658>, 
        <21.63,16.6312,21.1518>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR3 { 
    Id  3744670112
    Geometry  Geometry_140569434334024
    Appearance  ecran
}


TriangleSet Geometry_140569434334760 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.6312,21.1518>, 
        <21.63,16.5795,21.0902>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR4 { 
    Id  3744670848
    Geometry  Geometry_140569434334760
    Appearance  ecran
}


TriangleSet Geometry_140569434335496 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.5795,21.0902>, 
        <21.63,16.5795,21.0098>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR5 { 
    Id  3744671584
    Geometry  Geometry_140569434335496
    Appearance  ecran
}


TriangleSet Geometry_140569434336232 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.5795,21.0098>, 
        <21.63,16.6312,20.9482>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR6 { 
    Id  3744672320
    Geometry  Geometry_140569434336232
    Appearance  ecran
}


TriangleSet Geometry_140569434336968 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.6312,20.9482>, 
        <21.63,16.7104,20.9342>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR7 { 
    Id  3744673056
    Geometry  Geometry_140569434336968
    Appearance  ecran
}


TriangleSet Geometry_140569434337704 { 
    PointList [ 
        <21.48,16.69,21.05>, 
        <21.63,16.7104,20.9342>, 
        <21.63,16.7801,20.9744>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AR8 { 
    Id  3744673792
    Geometry  Geometry_140569434337704
    Appearance  ecran
}


TriangleSet Geometry_140569434338440 { 
    PointList [ 
        <21.417,16.762,21.05>, 
        <21.417,16.7452,21.0963>, 
        <21.417,16.7025,21.1209>, 
        <21.417,16.654,21.1124>, 
        <21.417,16.6223,21.0746>, 
        <21.417,16.6223,21.0254>, 
        <21.417,16.654,20.9876>, 
        <21.417,16.7025,20.9791>, 
        <21.417,16.7452,21.0037>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12ARx { 
    Id  3744674528
    Geometry  Geometry_140569434338440
    Appearance  ecran
}


TriangleSet Geometry_140569434339832 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.7589,21.1079>, 
        <21.63,16.78,21.05>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV0 { 
    Id  3744675920
    Geometry  Geometry_140569434339832
    Appearance  ecran
}


TriangleSet Geometry_140569434340568 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.78,21.05>, 
        <21.63,16.7589,20.9921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV1 { 
    Id  3744676656
    Geometry  Geometry_140569434340568
    Appearance  ecran
}


TriangleSet Geometry_140569434341304 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.7589,20.9921>, 
        <21.63,16.7056,20.9614>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV2 { 
    Id  3744677392
    Geometry  Geometry_140569434341304
    Appearance  ecran
}


TriangleSet Geometry_140569434342040 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.7056,20.9614>, 
        <21.63,16.645,20.9721>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV3 { 
    Id  3744678128
    Geometry  Geometry_140569434342040
    Appearance  ecran
}


TriangleSet Geometry_140569434342776 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.645,20.9721>, 
        <21.63,16.6054,21.0192>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV4 { 
    Id  3744678864
    Geometry  Geometry_140569434342776
    Appearance  ecran
}


TriangleSet Geometry_140569434343512 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.6054,21.0192>, 
        <21.63,16.6054,21.0808>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV5 { 
    Id  3744679600
    Geometry  Geometry_140569434343512
    Appearance  ecran
}


TriangleSet Geometry_140569434344248 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.6054,21.0808>, 
        <21.63,16.645,21.1279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV6 { 
    Id  3744680336
    Geometry  Geometry_140569434344248
    Appearance  ecran
}


TriangleSet Geometry_140569434344984 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.645,21.1279>, 
        <21.63,16.7056,21.1386>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV7 { 
    Id  3744681072
    Geometry  Geometry_140569434344984
    Appearance  ecran
}


TriangleSet Geometry_140569420390248 { 
    PointList [ 
        <21.795,16.69,21.05>, 
        <21.63,16.7056,21.1386>, 
        <21.63,16.7589,21.1079>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp12AV8 { 
    Id  3730438192
    Geometry  Geometry_140569420390248
    Appearance  ecran
}


TriangleSet Geometry_140569420401224 { 
    PointList [ 
        <2.25,16.509,21.05>, 
        <2.25,16.535,20.9787>, 
        <2.25,16.6007,20.9407>, 
        <2.25,16.6755,20.9539>, 
        <2.25,16.7243,21.012>, 
        <2.25,16.7243,21.088>, 
        <2.25,16.6755,21.1461>, 
        <2.25,16.6007,21.1593>, 
        <2.25,16.535,21.1213>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV { 
    Id  3730414096
    Geometry  Geometry_140569420401224
    Appearance  ecran
}


TriangleSet Geometry_140569337174136 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.5299,20.9744>, 
        <2.4,16.5024,21.05>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR0 { 
    Id  3743788320
    Geometry  Geometry_140569337174136
    Appearance  ecran
}


TriangleSet Geometry_140569420402216 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.5024,21.05>, 
        <2.4,16.5299,21.1256>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR1 { 
    Id  3743828640
    Geometry  Geometry_140569420402216
    Appearance  ecran
}


TriangleSet Geometry_140569433541928 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.5299,21.1256>, 
        <2.4,16.5996,21.1658>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR2 { 
    Id  3743904816
    Geometry  Geometry_140569433541928
    Appearance  ecran
}


TriangleSet Geometry_140569433569352 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.5996,21.1658>, 
        <2.4,16.6788,21.1518>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR3 { 
    Id  3647490080
    Geometry  Geometry_140569433569352
    Appearance  ecran
}


TriangleSet Geometry_140569433570376 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.6788,21.1518>, 
        <2.4,16.7305,21.0902>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR4 { 
    Id  3743906112
    Geometry  Geometry_140569433570376
    Appearance  ecran
}


TriangleSet Geometry_140569433571112 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.7305,21.0902>, 
        <2.4,16.7305,21.0098>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR5 { 
    Id  3743907200
    Geometry  Geometry_140569433571112
    Appearance  ecran
}


TriangleSet Geometry_140569433571848 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.7305,21.0098>, 
        <2.4,16.6788,20.9482>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR6 { 
    Id  3743907936
    Geometry  Geometry_140569433571848
    Appearance  ecran
}


TriangleSet Geometry_140569433572632 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.6788,20.9482>, 
        <2.4,16.5996,20.9342>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR7 { 
    Id  3743908672
    Geometry  Geometry_140569433572632
    Appearance  ecran
}


TriangleSet Geometry_140569433573368 { 
    PointList [ 
        <2.55,16.62,21.05>, 
        <2.4,16.5996,20.9342>, 
        <2.4,16.5299,20.9744>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AR8 { 
    Id  3743909456
    Geometry  Geometry_140569433573368
    Appearance  ecran
}


TriangleSet Geometry_140569433574104 { 
    PointList [ 
        <2.613,16.548,21.05>, 
        <2.613,16.5648,21.0963>, 
        <2.613,16.6075,21.1209>, 
        <2.613,16.656,21.1124>, 
        <2.613,16.6877,21.0746>, 
        <2.613,16.6877,21.0254>, 
        <2.613,16.656,20.9876>, 
        <2.613,16.6075,20.9791>, 
        <2.613,16.5648,21.0037>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13ARx { 
    Id  3743910192
    Geometry  Geometry_140569433574104
    Appearance  ecran
}


TriangleSet Geometry_140569433575496 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.5511,21.1079>, 
        <2.4,16.53,21.05>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV0 { 
    Id  3743911584
    Geometry  Geometry_140569433575496
    Appearance  ecran
}


TriangleSet Geometry_140569433576232 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.53,21.05>, 
        <2.4,16.5511,20.9921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV1 { 
    Id  3743912320
    Geometry  Geometry_140569433576232
    Appearance  ecran
}


TriangleSet Geometry_140569433576968 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.5511,20.9921>, 
        <2.4,16.6044,20.9614>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV2 { 
    Id  3743913056
    Geometry  Geometry_140569433576968
    Appearance  ecran
}


TriangleSet Geometry_140569421541176 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.6044,20.9614>, 
        <2.4,16.665,20.9721>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV3 { 
    Id  3731877264
    Geometry  Geometry_140569421541176
    Appearance  ecran
}


TriangleSet Geometry_140569421541912 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.665,20.9721>, 
        <2.4,16.7046,21.0192>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV4 { 
    Id  3731878000
    Geometry  Geometry_140569421541912
    Appearance  ecran
}


TriangleSet Geometry_140569421542648 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.7046,21.0192>, 
        <2.4,16.7046,21.0808>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV5 { 
    Id  3731878736
    Geometry  Geometry_140569421542648
    Appearance  ecran
}


TriangleSet Geometry_140569421543384 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.7046,21.0808>, 
        <2.4,16.665,21.1279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV6 { 
    Id  3731879472
    Geometry  Geometry_140569421543384
    Appearance  ecran
}


TriangleSet Geometry_140569421544120 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.665,21.1279>, 
        <2.4,16.6044,21.1386>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV7 { 
    Id  3731880208
    Geometry  Geometry_140569421544120
    Appearance  ecran
}


TriangleSet Geometry_140569421544856 { 
    PointList [ 
        <2.235,16.62,21.05>, 
        <2.4,16.6044,21.1386>, 
        <2.4,16.5511,21.1079>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp13AV8 { 
    Id  3731880944
    Geometry  Geometry_140569421544856
    Appearance  ecran
}


TriangleSet Geometry_140569421545400 { 
    PointList [ 
        <7.51,1.881,21.03>, 
        <7.51,1.85269,20.9522>, 
        <7.51,1.78101,20.9108>, 
        <7.51,1.6995,20.9252>, 
        <7.51,1.6463,20.9886>, 
        <7.51,1.6463,21.0714>, 
        <7.51,1.6995,21.1348>, 
        <7.51,1.78101,21.1492>, 
        <7.51,1.85269,21.1078>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp20AV { 
    Id  3731881680
    Geometry  Geometry_140569421545400
    Appearance  ecran
}


TriangleSet Geometry_140569433578120 { 
    PointList [ 
        <7.21,1.8755,21.03>, 
        <7.21,1.84848,21.1042>, 
        <7.21,1.78006,21.1437>, 
        <7.21,1.70225,21.13>, 
        <7.21,1.65147,21.0695>, 
        <7.21,1.65147,20.9905>, 
        <7.21,1.70225,20.93>, 
        <7.21,1.78006,20.9163>, 
        <7.21,1.84848,20.9558>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp20AR { 
    Id  3743914208
    Geometry  Geometry_140569433578120
    Appearance  ecran
}


TriangleSet Geometry_140569433579512 { 
    PointList [ 
        <16.5,1.679,21.03>, 
        <16.5,1.70731,20.9522>, 
        <16.5,1.77899,20.9108>, 
        <16.5,1.8605,20.9252>, 
        <16.5,1.9137,20.9886>, 
        <16.5,1.9137,21.0714>, 
        <16.5,1.8605,21.1348>, 
        <16.5,1.77899,21.1492>, 
        <16.5,1.70731,21.1078>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp21AV { 
    Id  3743915600
    Geometry  Geometry_140569433579512
    Appearance  ecran
}


TriangleSet Geometry_140569433580904 { 
    PointList [ 
        <16.8,1.6845,21.03>, 
        <16.8,1.71152,21.1042>, 
        <16.8,1.77994,21.1437>, 
        <16.8,1.85775,21.13>, 
        <16.8,1.90853,21.0695>, 
        <16.8,1.90853,20.9905>, 
        <16.8,1.85775,20.93>, 
        <16.8,1.77994,20.9163>, 
        <16.8,1.71152,20.9558>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp21AR { 
    Id  3743916992
    Geometry  Geometry_140569433580904
    Appearance  ecran
}


TriangleSet Geometry_140569433582296 { 
    PointList [ 
        <16.59,16.449,21>, 
        <16.59,16.4773,20.9222>, 
        <16.59,16.549,20.8808>, 
        <16.59,16.6305,20.8952>, 
        <16.59,16.6837,20.9586>, 
        <16.59,16.6837,21.0414>, 
        <16.59,16.6305,21.1048>, 
        <16.59,16.549,21.1192>, 
        <16.59,16.4773,21.0778>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp22AV { 
    Id  3743918384
    Geometry  Geometry_140569433582296
    Appearance  ecran
}


TriangleSet Geometry_140569433583688 { 
    PointList [ 
        <16.89,16.4545,21>, 
        <16.89,16.4815,21.0742>, 
        <16.89,16.5499,21.1137>, 
        <16.89,16.6278,21.1>, 
        <16.89,16.6785,21.0395>, 
        <16.89,16.6785,20.9605>, 
        <16.89,16.6278,20.9>, 
        <16.89,16.5499,20.8863>, 
        <16.89,16.4815,20.9258>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp22AR { 
    Id  3743919776
    Geometry  Geometry_140569433583688
    Appearance  ecran
}


TriangleSet Geometry_140569433585080 { 
    PointList [ 
        <7.47,16.821,21.05>, 
        <7.47,16.7927,20.9722>, 
        <7.47,16.721,20.9308>, 
        <7.47,16.6395,20.9452>, 
        <7.47,16.5863,21.0086>, 
        <7.47,16.5863,21.0914>, 
        <7.47,16.6395,21.1548>, 
        <7.47,16.721,21.1692>, 
        <7.47,16.7927,21.1278>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp23AV { 
    Id  3743921168
    Geometry  Geometry_140569433585080
    Appearance  ecran
}


TriangleSet Geometry_140569433586472 { 
    PointList [ 
        <7.17,16.8155,21.05>, 
        <7.17,16.7885,21.1242>, 
        <7.17,16.7201,21.1637>, 
        <7.17,16.6423,21.15>, 
        <7.17,16.5915,21.0895>, 
        <7.17,16.5915,21.0105>, 
        <7.17,16.6423,20.95>, 
        <7.17,16.7201,20.9363>, 
        <7.17,16.7885,20.9758>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp23AR { 
    Id  3743922560
    Geometry  Geometry_140569433586472
    Appearance  ecran
}


TriangleSet Geometry_140569433587864 { 
    PointList [ 
        <3.75,5.039,21.1>, 
        <3.75,5.06497,21.0287>, 
        <3.75,5.13073,20.9907>, 
        <3.75,5.2055,21.0039>, 
        <3.75,5.25431,21.062>, 
        <3.75,5.25431,21.138>, 
        <3.75,5.2055,21.1961>, 
        <3.75,5.13073,21.2093>, 
        <3.75,5.06497,21.1713>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV { 
    Id  3743923952
    Geometry  Geometry_140569433587864
    Appearance  ecran
}


TriangleSet Geometry_140569433589256 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.05991,21.0244>, 
        <3.9,5.0324,21.1>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR0 { 
    Id  3743925344
    Geometry  Geometry_140569433589256
    Appearance  ecran
}


TriangleSet Geometry_140569433589992 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.0324,21.1>, 
        <3.9,5.05991,21.1756>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR1 { 
    Id  3743926080
    Geometry  Geometry_140569433589992
    Appearance  ecran
}


TriangleSet Geometry_140569433590728 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.05991,21.1756>, 
        <3.9,5.12958,21.2158>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR2 { 
    Id  3743926816
    Geometry  Geometry_140569433590728
    Appearance  ecran
}


TriangleSet Geometry_140569433591464 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.12958,21.2158>, 
        <3.9,5.2088,21.2018>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR3 { 
    Id  3743927552
    Geometry  Geometry_140569433591464
    Appearance  ecran
}


TriangleSet Geometry_140569433592200 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.2088,21.2018>, 
        <3.9,5.26051,21.1402>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR4 { 
    Id  3743928288
    Geometry  Geometry_140569433592200
    Appearance  ecran
}


TriangleSet Geometry_140569433592936 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.26051,21.1402>, 
        <3.9,5.26051,21.0598>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR5 { 
    Id  3743929024
    Geometry  Geometry_140569433592936
    Appearance  ecran
}


TriangleSet Geometry_140569433593672 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.26051,21.0598>, 
        <3.9,5.2088,20.9982>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR6 { 
    Id  3743929760
    Geometry  Geometry_140569433593672
    Appearance  ecran
}


TriangleSet Geometry_140569433594408 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.2088,20.9982>, 
        <3.9,5.12958,20.9842>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR7 { 
    Id  3743930496
    Geometry  Geometry_140569433594408
    Appearance  ecran
}


TriangleSet Geometry_140569433595144 { 
    PointList [ 
        <4.05,5.15,21.1>, 
        <3.9,5.12958,20.9842>, 
        <3.9,5.05991,21.0244>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AR8 { 
    Id  3743931232
    Geometry  Geometry_140569433595144
    Appearance  ecran
}


TriangleSet Geometry_140569433595880 { 
    PointList [ 
        <4.113,5.078,21.1>, 
        <4.113,5.09484,21.1463>, 
        <4.113,5.1375,21.1709>, 
        <4.113,5.186,21.1624>, 
        <4.113,5.21766,21.1246>, 
        <4.113,5.21766,21.0754>, 
        <4.113,5.186,21.0376>, 
        <4.113,5.1375,21.0291>, 
        <4.113,5.09484,21.0537>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30ARx { 
    Id  3743931968
    Geometry  Geometry_140569433595880
    Appearance  ecran
}


TriangleSet Geometry_140569433597272 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.08106,21.1579>, 
        <3.9,5.06,21.1>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV0 { 
    Id  3743933360
    Geometry  Geometry_140569433597272
    Appearance  ecran
}


TriangleSet Geometry_140569433598008 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.06,21.1>, 
        <3.9,5.08106,21.0421>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV1 { 
    Id  3743934096
    Geometry  Geometry_140569433598008
    Appearance  ecran
}


TriangleSet Geometry_140569433598744 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.08106,21.0421>, 
        <3.9,5.13437,21.0114>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV2 { 
    Id  3743934832
    Geometry  Geometry_140569433598744
    Appearance  ecran
}


TriangleSet Geometry_140569433599480 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.13437,21.0114>, 
        <3.9,5.195,21.0221>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV3 { 
    Id  3743935568
    Geometry  Geometry_140569433599480
    Appearance  ecran
}


TriangleSet Geometry_140569433600216 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.195,21.0221>, 
        <3.9,5.23457,21.0692>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV4 { 
    Id  3743936304
    Geometry  Geometry_140569433600216
    Appearance  ecran
}


TriangleSet Geometry_140569433600952 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.23457,21.0692>, 
        <3.9,5.23457,21.1308>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV5 { 
    Id  3743937040
    Geometry  Geometry_140569433600952
    Appearance  ecran
}


TriangleSet Geometry_140569433601688 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.23457,21.1308>, 
        <3.9,5.195,21.1779>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV6 { 
    Id  3743937776
    Geometry  Geometry_140569433601688
    Appearance  ecran
}


TriangleSet Geometry_140569433602424 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.195,21.1779>, 
        <3.9,5.13437,21.1886>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV7 { 
    Id  3743938512
    Geometry  Geometry_140569433602424
    Appearance  ecran
}


TriangleSet Geometry_140569433603160 { 
    PointList [ 
        <3.735,5.15,21.1>, 
        <3.9,5.13437,21.1886>, 
        <3.9,5.08106,21.1579>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp30AV8 { 
    Id  3743939248
    Geometry  Geometry_140569433603160
    Appearance  ecran
}


TriangleSet Geometry_140569433603896 { 
    PointList [ 
        <20.27,5.361,21.15>, 
        <20.27,5.33503,21.0787>, 
        <20.27,5.26927,21.0407>, 
        <20.27,5.1945,21.0539>, 
        <20.27,5.14569,21.112>, 
        <20.27,5.14569,21.188>, 
        <20.27,5.1945,21.2461>, 
        <20.27,5.26927,21.2593>, 
        <20.27,5.33503,21.2213>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV { 
    Id  3743939984
    Geometry  Geometry_140569433603896
    Appearance  ecran
}


TriangleSet Geometry_140569433605288 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.34009,21.0744>, 
        <20.12,5.3676,21.15>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR0 { 
    Id  3743941376
    Geometry  Geometry_140569433605288
    Appearance  ecran
}


TriangleSet Geometry_140569433606024 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.3676,21.15>, 
        <20.12,5.34009,21.2256>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR1 { 
    Id  3743942112
    Geometry  Geometry_140569433606024
    Appearance  ecran
}


TriangleSet Geometry_140569433606760 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.34009,21.2256>, 
        <20.12,5.27042,21.2658>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR2 { 
    Id  3743942848
    Geometry  Geometry_140569433606760
    Appearance  ecran
}


TriangleSet Geometry_140569433607496 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.27042,21.2658>, 
        <20.12,5.1912,21.2518>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR3 { 
    Id  3743943584
    Geometry  Geometry_140569433607496
    Appearance  ecran
}


TriangleSet Geometry_140569433608232 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.1912,21.2518>, 
        <20.12,5.13949,21.1902>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR4 { 
    Id  3743944320
    Geometry  Geometry_140569433608232
    Appearance  ecran
}


TriangleSet Geometry_140569433608968 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.13949,21.1902>, 
        <20.12,5.13949,21.1098>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR5 { 
    Id  3743945056
    Geometry  Geometry_140569433608968
    Appearance  ecran
}


TriangleSet Geometry_140569433609704 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.13949,21.1098>, 
        <20.12,5.1912,21.0482>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR6 { 
    Id  3743945792
    Geometry  Geometry_140569433609704
    Appearance  ecran
}


TriangleSet Geometry_140569433610440 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.1912,21.0482>, 
        <20.12,5.27042,21.0342>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR7 { 
    Id  3743946528
    Geometry  Geometry_140569433610440
    Appearance  ecran
}


TriangleSet Geometry_140569433611176 { 
    PointList [ 
        <19.97,5.25,21.15>, 
        <20.12,5.27042,21.0342>, 
        <20.12,5.34009,21.0744>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AR8 { 
    Id  3743947264
    Geometry  Geometry_140569433611176
    Appearance  ecran
}


TriangleSet Geometry_140569433611912 { 
    PointList [ 
        <19.907,5.322,21.15>, 
        <19.907,5.30516,21.1963>, 
        <19.907,5.2625,21.2209>, 
        <19.907,5.214,21.2124>, 
        <19.907,5.18234,21.1746>, 
        <19.907,5.18234,21.1254>, 
        <19.907,5.214,21.0876>, 
        <19.907,5.2625,21.0791>, 
        <19.907,5.30516,21.1037>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31ARx { 
    Id  3743948000
    Geometry  Geometry_140569433611912
    Appearance  ecran
}


TriangleSet Geometry_140569433613304 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.31894,21.2079>, 
        <20.12,5.34,21.15>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV0 { 
    Id  3743949392
    Geometry  Geometry_140569433613304
    Appearance  ecran
}


TriangleSet Geometry_140569433614040 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.34,21.15>, 
        <20.12,5.31894,21.0921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV1 { 
    Id  3743950128
    Geometry  Geometry_140569433614040
    Appearance  ecran
}


TriangleSet Geometry_140569433614776 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.31894,21.0921>, 
        <20.12,5.26563,21.0614>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV2 { 
    Id  3743950864
    Geometry  Geometry_140569433614776
    Appearance  ecran
}


TriangleSet Geometry_140569433615512 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.26563,21.0614>, 
        <20.12,5.205,21.0721>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV3 { 
    Id  3743951600
    Geometry  Geometry_140569433615512
    Appearance  ecran
}


TriangleSet Geometry_140569433616248 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.205,21.0721>, 
        <20.12,5.16543,21.1192>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV4 { 
    Id  3743952336
    Geometry  Geometry_140569433616248
    Appearance  ecran
}


TriangleSet Geometry_140569433616984 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.16543,21.1192>, 
        <20.12,5.16543,21.1808>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV5 { 
    Id  3743953072
    Geometry  Geometry_140569433616984
    Appearance  ecran
}


TriangleSet Geometry_140569433617720 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.16543,21.1808>, 
        <20.12,5.205,21.2279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV6 { 
    Id  3743953808
    Geometry  Geometry_140569433617720
    Appearance  ecran
}


TriangleSet Geometry_140569433618456 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.205,21.2279>, 
        <20.12,5.26563,21.2386>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV7 { 
    Id  3743954544
    Geometry  Geometry_140569433618456
    Appearance  ecran
}


TriangleSet Geometry_140569433619192 { 
    PointList [ 
        <20.285,5.25,21.15>, 
        <20.12,5.26563,21.2386>, 
        <20.12,5.31894,21.2079>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp31AV8 { 
    Id  3743955280
    Geometry  Geometry_140569433619192
    Appearance  ecran
}


TriangleSet Geometry_140569433619928 { 
    PointList [ 
        <20.3,13.291,21.07>, 
        <20.3,13.265,20.9987>, 
        <20.3,13.1993,20.9607>, 
        <20.3,13.1245,20.9739>, 
        <20.3,13.0757,21.032>, 
        <20.3,13.0757,21.108>, 
        <20.3,13.1245,21.1661>, 
        <20.3,13.1993,21.1793>, 
        <20.3,13.265,21.1413>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV { 
    Id  3743956016
    Geometry  Geometry_140569433619928
    Appearance  ecran
}


TriangleSet Geometry_140569433621320 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.2701,20.9944>, 
        <20.15,13.2976,21.07>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR0 { 
    Id  3743957408
    Geometry  Geometry_140569433621320
    Appearance  ecran
}


TriangleSet Geometry_140569433622056 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.2976,21.07>, 
        <20.15,13.2701,21.1456>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR1 { 
    Id  3743958144
    Geometry  Geometry_140569433622056
    Appearance  ecran
}


TriangleSet Geometry_140569433622792 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.2701,21.1456>, 
        <20.15,13.2004,21.1858>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR2 { 
    Id  3743958880
    Geometry  Geometry_140569433622792
    Appearance  ecran
}


TriangleSet Geometry_140569433623528 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.2004,21.1858>, 
        <20.15,13.1212,21.1718>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR3 { 
    Id  3743959616
    Geometry  Geometry_140569433623528
    Appearance  ecran
}


TriangleSet Geometry_140569433624264 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.1212,21.1718>, 
        <20.15,13.0695,21.1102>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR4 { 
    Id  3743960352
    Geometry  Geometry_140569433624264
    Appearance  ecran
}


TriangleSet Geometry_140569433625000 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.0695,21.1102>, 
        <20.15,13.0695,21.0298>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR5 { 
    Id  3743961088
    Geometry  Geometry_140569433625000
    Appearance  ecran
}


TriangleSet Geometry_140569433625736 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.0695,21.0298>, 
        <20.15,13.1212,20.9682>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR6 { 
    Id  3743961824
    Geometry  Geometry_140569433625736
    Appearance  ecran
}


TriangleSet Geometry_140569433626472 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.1212,20.9682>, 
        <20.15,13.2004,20.9542>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR7 { 
    Id  3743962560
    Geometry  Geometry_140569433626472
    Appearance  ecran
}


TriangleSet Geometry_140569433627208 { 
    PointList [ 
        <20,13.18,21.07>, 
        <20.15,13.2004,20.9542>, 
        <20.15,13.2701,20.9944>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AR8 { 
    Id  3743963296
    Geometry  Geometry_140569433627208
    Appearance  ecran
}


TriangleSet Geometry_140569433627944 { 
    PointList [ 
        <19.937,13.252,21.07>, 
        <19.937,13.2352,21.1163>, 
        <19.937,13.1925,21.1409>, 
        <19.937,13.144,21.1324>, 
        <19.937,13.1123,21.0946>, 
        <19.937,13.1123,21.0454>, 
        <19.937,13.144,21.0076>, 
        <19.937,13.1925,20.9991>, 
        <19.937,13.2352,21.0237>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32ARx { 
    Id  3743964032
    Geometry  Geometry_140569433627944
    Appearance  ecran
}


TriangleSet Geometry_140569433629336 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.2489,21.1279>, 
        <20.15,13.27,21.07>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV0 { 
    Id  3743965424
    Geometry  Geometry_140569433629336
    Appearance  ecran
}


TriangleSet Geometry_140569433630072 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.27,21.07>, 
        <20.15,13.2489,21.0121>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV1 { 
    Id  3743966160
    Geometry  Geometry_140569433630072
    Appearance  ecran
}


TriangleSet Geometry_140569433630808 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.2489,21.0121>, 
        <20.15,13.1956,20.9814>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV2 { 
    Id  3743966896
    Geometry  Geometry_140569433630808
    Appearance  ecran
}


TriangleSet Geometry_140569433631544 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.1956,20.9814>, 
        <20.15,13.135,20.9921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV3 { 
    Id  3743967632
    Geometry  Geometry_140569433631544
    Appearance  ecran
}


TriangleSet Geometry_140569433632280 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.135,20.9921>, 
        <20.15,13.0954,21.0392>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV4 { 
    Id  3743968368
    Geometry  Geometry_140569433632280
    Appearance  ecran
}


TriangleSet Geometry_140569433633016 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.0954,21.0392>, 
        <20.15,13.0954,21.1008>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV5 { 
    Id  3743969104
    Geometry  Geometry_140569433633016
    Appearance  ecran
}


TriangleSet Geometry_140569433633752 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.0954,21.1008>, 
        <20.15,13.135,21.1479>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV6 { 
    Id  3743969840
    Geometry  Geometry_140569433633752
    Appearance  ecran
}


TriangleSet Geometry_140569433634488 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.135,21.1479>, 
        <20.15,13.1956,21.1586>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV7 { 
    Id  3743970576
    Geometry  Geometry_140569433634488
    Appearance  ecran
}


TriangleSet Geometry_140569433635224 { 
    PointList [ 
        <20.315,13.18,21.07>, 
        <20.15,13.1956,21.1586>, 
        <20.15,13.2489,21.1279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp32AV8 { 
    Id  3743971312
    Geometry  Geometry_140569433635224
    Appearance  ecran
}


TriangleSet Geometry_140569433635960 { 
    PointList [ 
        <3.65,13.019,21.1>, 
        <3.65,13.045,21.0287>, 
        <3.65,13.1107,20.9907>, 
        <3.65,13.1855,21.0039>, 
        <3.65,13.2343,21.062>, 
        <3.65,13.2343,21.138>, 
        <3.65,13.1855,21.1961>, 
        <3.65,13.1107,21.2093>, 
        <3.65,13.045,21.1713>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV { 
    Id  3743972048
    Geometry  Geometry_140569433635960
    Appearance  ecran
}


TriangleSet Geometry_140569433637352 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.0399,21.0244>, 
        <3.8,13.0124,21.1>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR0 { 
    Id  3743973440
    Geometry  Geometry_140569433637352
    Appearance  ecran
}


TriangleSet Geometry_140569433638088 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.0124,21.1>, 
        <3.8,13.0399,21.1756>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR1 { 
    Id  3743974176
    Geometry  Geometry_140569433638088
    Appearance  ecran
}


TriangleSet Geometry_140569433638824 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.0399,21.1756>, 
        <3.8,13.1096,21.2158>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR2 { 
    Id  3743974912
    Geometry  Geometry_140569433638824
    Appearance  ecran
}


TriangleSet Geometry_140569433639560 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.1096,21.2158>, 
        <3.8,13.1888,21.2018>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR3 { 
    Id  3743975648
    Geometry  Geometry_140569433639560
    Appearance  ecran
}


TriangleSet Geometry_140569433640296 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.1888,21.2018>, 
        <3.8,13.2405,21.1402>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR4 { 
    Id  3743976384
    Geometry  Geometry_140569433640296
    Appearance  ecran
}


TriangleSet Geometry_140569433641032 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.2405,21.1402>, 
        <3.8,13.2405,21.0598>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR5 { 
    Id  3743977120
    Geometry  Geometry_140569433641032
    Appearance  ecran
}


TriangleSet Geometry_140569433641768 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.2405,21.0598>, 
        <3.8,13.1888,20.9982>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR6 { 
    Id  3743977856
    Geometry  Geometry_140569433641768
    Appearance  ecran
}


TriangleSet Geometry_140569433642504 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.1888,20.9982>, 
        <3.8,13.1096,20.9842>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR7 { 
    Id  3743978592
    Geometry  Geometry_140569433642504
    Appearance  ecran
}


TriangleSet Geometry_140569433643240 { 
    PointList [ 
        <3.95,13.13,21.1>, 
        <3.8,13.1096,20.9842>, 
        <3.8,13.0399,21.0244>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AR8 { 
    Id  3743979328
    Geometry  Geometry_140569433643240
    Appearance  ecran
}


TriangleSet Geometry_140569433643976 { 
    PointList [ 
        <4.013,13.058,21.1>, 
        <4.013,13.0748,21.1463>, 
        <4.013,13.1175,21.1709>, 
        <4.013,13.166,21.1624>, 
        <4.013,13.1977,21.1246>, 
        <4.013,13.1977,21.0754>, 
        <4.013,13.166,21.0376>, 
        <4.013,13.1175,21.0291>, 
        <4.013,13.0748,21.0537>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33ARx { 
    Id  3743980064
    Geometry  Geometry_140569433643976
    Appearance  ecran
}


TriangleSet Geometry_140569433645368 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.0611,21.1579>, 
        <3.8,13.04,21.1>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV0 { 
    Id  3743981456
    Geometry  Geometry_140569433645368
    Appearance  ecran
}


TriangleSet Geometry_140569433646104 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.04,21.1>, 
        <3.8,13.0611,21.0421>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV1 { 
    Id  3743982192
    Geometry  Geometry_140569433646104
    Appearance  ecran
}


TriangleSet Geometry_140569433646840 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.0611,21.0421>, 
        <3.8,13.1144,21.0114>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV2 { 
    Id  3743982928
    Geometry  Geometry_140569433646840
    Appearance  ecran
}


TriangleSet Geometry_140569433647576 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.1144,21.0114>, 
        <3.8,13.175,21.0221>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV3 { 
    Id  3743983664
    Geometry  Geometry_140569433647576
    Appearance  ecran
}


TriangleSet Geometry_140569433648312 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.175,21.0221>, 
        <3.8,13.2146,21.0692>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV4 { 
    Id  3743984400
    Geometry  Geometry_140569433648312
    Appearance  ecran
}


TriangleSet Geometry_140569433649048 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.2146,21.0692>, 
        <3.8,13.2146,21.1308>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV5 { 
    Id  3743985136
    Geometry  Geometry_140569433649048
    Appearance  ecran
}


TriangleSet Geometry_140569433649784 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.2146,21.1308>, 
        <3.8,13.175,21.1779>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV6 { 
    Id  3743985872
    Geometry  Geometry_140569433649784
    Appearance  ecran
}


TriangleSet Geometry_140569433650520 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.175,21.1779>, 
        <3.8,13.1144,21.1886>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV7 { 
    Id  3743986608
    Geometry  Geometry_140569433650520
    Appearance  ecran
}


TriangleSet Geometry_140569433651256 { 
    PointList [ 
        <3.635,13.13,21.1>, 
        <3.8,13.1144,21.1886>, 
        <3.8,13.0611,21.1579>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp33AV8 { 
    Id  3743987344
    Geometry  Geometry_140569433651256
    Appearance  ecran
}


TriangleSet Geometry_140569433651992 { 
    PointList [ 
        <1.831,5.2,21.05>, 
        <1.80503,5.2,20.9787>, 
        <1.73927,5.2,20.9407>, 
        <1.6645,5.2,20.9539>, 
        <1.61569,5.2,21.012>, 
        <1.61569,5.2,21.088>, 
        <1.6645,5.2,21.1461>, 
        <1.73927,5.2,21.1593>, 
        <1.80503,5.2,21.1213>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV { 
    Id  3743988080
    Geometry  Geometry_140569433651992
    Appearance  ecran
}


TriangleSet Geometry_140569433653384 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.81009,5.35,20.9744>, 
        <1.8376,5.35,21.05>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR0 { 
    Id  3743989472
    Geometry  Geometry_140569433653384
    Appearance  ecran
}


TriangleSet Geometry_140569433654120 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.8376,5.35,21.05>, 
        <1.81009,5.35,21.1256>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR1 { 
    Id  3743990208
    Geometry  Geometry_140569433654120
    Appearance  ecran
}


TriangleSet Geometry_140569433654856 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.81009,5.35,21.1256>, 
        <1.74042,5.35,21.1658>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR2 { 
    Id  3743990944
    Geometry  Geometry_140569433654856
    Appearance  ecran
}


TriangleSet Geometry_140569433655592 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.74042,5.35,21.1658>, 
        <1.6612,5.35,21.1518>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR3 { 
    Id  3743991680
    Geometry  Geometry_140569433655592
    Appearance  ecran
}


TriangleSet Geometry_140569433656328 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.6612,5.35,21.1518>, 
        <1.60949,5.35,21.0902>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR4 { 
    Id  3743992416
    Geometry  Geometry_140569433656328
    Appearance  ecran
}


TriangleSet Geometry_140569433657064 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.60949,5.35,21.0902>, 
        <1.60949,5.35,21.0098>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR5 { 
    Id  3743993152
    Geometry  Geometry_140569433657064
    Appearance  ecran
}


TriangleSet Geometry_140569433657800 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.60949,5.35,21.0098>, 
        <1.6612,5.35,20.9482>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR6 { 
    Id  3743993888
    Geometry  Geometry_140569433657800
    Appearance  ecran
}


TriangleSet Geometry_140569433658536 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.6612,5.35,20.9482>, 
        <1.74042,5.35,20.9342>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR7 { 
    Id  3743994624
    Geometry  Geometry_140569433658536
    Appearance  ecran
}


TriangleSet Geometry_140569433659272 { 
    PointList [ 
        <1.72,5.5,21.05>, 
        <1.74042,5.35,20.9342>, 
        <1.81009,5.35,20.9744>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AR8 { 
    Id  3743995360
    Geometry  Geometry_140569433659272
    Appearance  ecran
}


TriangleSet Geometry_140569433660008 { 
    PointList [ 
        <1.792,5.563,21.05>, 
        <1.77516,5.563,21.0963>, 
        <1.7325,5.563,21.1209>, 
        <1.684,5.563,21.1124>, 
        <1.65234,5.563,21.0746>, 
        <1.65234,5.563,21.0254>, 
        <1.684,5.563,20.9876>, 
        <1.7325,5.563,20.9791>, 
        <1.77516,5.563,21.0037>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40ARx { 
    Id  3743996096
    Geometry  Geometry_140569433660008
    Appearance  ecran
}


TriangleSet Geometry_140569433661400 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.78894,5.35,21.1079>, 
        <1.81,5.35,21.05>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV0 { 
    Id  3743997488
    Geometry  Geometry_140569433661400
    Appearance  ecran
}


TriangleSet Geometry_140569433662136 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.81,5.35,21.05>, 
        <1.78894,5.35,20.9921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV1 { 
    Id  3743998224
    Geometry  Geometry_140569433662136
    Appearance  ecran
}


TriangleSet Geometry_140569433662872 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.78894,5.35,20.9921>, 
        <1.73563,5.35,20.9614>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV2 { 
    Id  3743998960
    Geometry  Geometry_140569433662872
    Appearance  ecran
}


TriangleSet Geometry_140569433663608 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.73563,5.35,20.9614>, 
        <1.675,5.35,20.9721>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV3 { 
    Id  3743999696
    Geometry  Geometry_140569433663608
    Appearance  ecran
}


TriangleSet Geometry_140569433664344 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.675,5.35,20.9721>, 
        <1.63543,5.35,21.0192>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV4 { 
    Id  3744000432
    Geometry  Geometry_140569433664344
    Appearance  ecran
}


TriangleSet Geometry_140569433665080 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.63543,5.35,21.0192>, 
        <1.63543,5.35,21.0808>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV5 { 
    Id  3744001168
    Geometry  Geometry_140569433665080
    Appearance  ecran
}


TriangleSet Geometry_140569433665816 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.63543,5.35,21.0808>, 
        <1.675,5.35,21.1279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV6 { 
    Id  3744001904
    Geometry  Geometry_140569433665816
    Appearance  ecran
}


TriangleSet Geometry_140569433666552 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.675,5.35,21.1279>, 
        <1.73563,5.35,21.1386>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV7 { 
    Id  3744002640
    Geometry  Geometry_140569433666552
    Appearance  ecran
}


TriangleSet Geometry_140569433667288 { 
    PointList [ 
        <1.72,5.185,21.05>, 
        <1.73563,5.35,21.1386>, 
        <1.78894,5.35,21.1079>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp40AV8 { 
    Id  3744003376
    Geometry  Geometry_140569433667288
    Appearance  ecran
}


TriangleSet Geometry_140569433668024 { 
    PointList [ 
        <22.201,5.22,21.1>, 
        <22.175,5.22,21.0287>, 
        <22.1093,5.22,20.9907>, 
        <22.0345,5.22,21.0039>, 
        <21.9857,5.22,21.062>, 
        <21.9857,5.22,21.138>, 
        <22.0345,5.22,21.1961>, 
        <22.1093,5.22,21.2093>, 
        <22.175,5.22,21.1713>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV { 
    Id  3744004112
    Geometry  Geometry_140569433668024
    Appearance  ecran
}


TriangleSet Geometry_140569433669416 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.1801,5.37,21.0244>, 
        <22.2076,5.37,21.1>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR0 { 
    Id  3744005504
    Geometry  Geometry_140569433669416
    Appearance  ecran
}


TriangleSet Geometry_140569433670152 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.2076,5.37,21.1>, 
        <22.1801,5.37,21.1756>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR1 { 
    Id  3744006240
    Geometry  Geometry_140569433670152
    Appearance  ecran
}


TriangleSet Geometry_140569433670888 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.1801,5.37,21.1756>, 
        <22.1104,5.37,21.2158>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR2 { 
    Id  3744006976
    Geometry  Geometry_140569433670888
    Appearance  ecran
}


TriangleSet Geometry_140569434345320 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.1104,5.37,21.2158>, 
        <22.0312,5.37,21.2018>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR3 { 
    Id  3744007712
    Geometry  Geometry_140569434345320
    Appearance  ecran
}


TriangleSet Geometry_140569434346056 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.0312,5.37,21.2018>, 
        <21.9795,5.37,21.1402>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR4 { 
    Id  3744682144
    Geometry  Geometry_140569434346056
    Appearance  ecran
}


TriangleSet Geometry_140569434346792 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <21.9795,5.37,21.1402>, 
        <21.9795,5.37,21.0598>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR5 { 
    Id  3744682880
    Geometry  Geometry_140569434346792
    Appearance  ecran
}


TriangleSet Geometry_140569337705464 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <21.9795,5.37,21.0598>, 
        <22.0312,5.37,20.9982>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR6 { 
    Id  3648041744
    Geometry  Geometry_140569337705464
    Appearance  ecran
}


TriangleSet Geometry_140569337706200 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.0312,5.37,20.9982>, 
        <22.1104,5.37,20.9842>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR7 { 
    Id  3648042288
    Geometry  Geometry_140569337706200
    Appearance  ecran
}


TriangleSet Geometry_140569337706968 { 
    PointList [ 
        <22.09,5.52,21.1>, 
        <22.1104,5.37,20.9842>, 
        <22.1801,5.37,21.0244>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AR8 { 
    Id  3648043024
    Geometry  Geometry_140569337706968
    Appearance  ecran
}


TriangleSet Geometry_140569337707704 { 
    PointList [ 
        <22.162,5.583,21.1>, 
        <22.1452,5.583,21.1463>, 
        <22.1025,5.583,21.1709>, 
        <22.054,5.583,21.1624>, 
        <22.0223,5.583,21.1246>, 
        <22.0223,5.583,21.0754>, 
        <22.054,5.583,21.0376>, 
        <22.1025,5.583,21.0291>, 
        <22.1452,5.583,21.0537>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41ARx { 
    Id  3648043792
    Geometry  Geometry_140569337707704
    Appearance  ecran
}


TriangleSet Geometry_140569337709096 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.1589,5.37,21.1579>, 
        <22.18,5.37,21.1>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV0 { 
    Id  3648045184
    Geometry  Geometry_140569337709096
    Appearance  ecran
}


TriangleSet Geometry_140569337709832 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.18,5.37,21.1>, 
        <22.1589,5.37,21.0421>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV1 { 
    Id  3648045920
    Geometry  Geometry_140569337709832
    Appearance  ecran
}


TriangleSet Geometry_140569337710568 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.1589,5.37,21.0421>, 
        <22.1056,5.37,21.0114>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV2 { 
    Id  3648046656
    Geometry  Geometry_140569337710568
    Appearance  ecran
}


TriangleSet Geometry_140569337711336 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.1056,5.37,21.0114>, 
        <22.045,5.37,21.0221>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV3 { 
    Id  3648047392
    Geometry  Geometry_140569337711336
    Appearance  ecran
}


TriangleSet Geometry_140569337712072 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.045,5.37,21.0221>, 
        <22.0054,5.37,21.0692>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV4 { 
    Id  3648048160
    Geometry  Geometry_140569337712072
    Appearance  ecran
}


TriangleSet Geometry_140569337712840 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.0054,5.37,21.0692>, 
        <22.0054,5.37,21.1308>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV5 { 
    Id  3648048896
    Geometry  Geometry_140569337712840
    Appearance  ecran
}


TriangleSet Geometry_140569337713576 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.0054,5.37,21.1308>, 
        <22.045,5.37,21.1779>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV6 { 
    Id  3648049664
    Geometry  Geometry_140569337713576
    Appearance  ecran
}


TriangleSet Geometry_140569433671624 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.045,5.37,21.1779>, 
        <22.1056,5.37,21.1886>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV7 { 
    Id  3648050400
    Geometry  Geometry_140569433671624
    Appearance  ecran
}


TriangleSet Geometry_140569433672360 { 
    PointList [ 
        <22.09,5.205,21.1>, 
        <22.1056,5.37,21.1886>, 
        <22.1589,5.37,21.1579>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp41AV8 { 
    Id  3744008448
    Geometry  Geometry_140569433672360
    Appearance  ecran
}


TriangleSet Geometry_140569433673096 { 
    PointList [ 
        <22.471,12.78,20.97>, 
        <22.445,12.78,20.8987>, 
        <22.3793,12.78,20.8607>, 
        <22.3045,12.78,20.8739>, 
        <22.2557,12.78,20.932>, 
        <22.2557,12.78,21.008>, 
        <22.3045,12.78,21.0661>, 
        <22.3793,12.78,21.0793>, 
        <22.445,12.78,21.0413>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV { 
    Id  3744009184
    Geometry  Geometry_140569433673096
    Appearance  ecran
}


TriangleSet Geometry_140569433674488 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.4501,12.93,20.8944>, 
        <22.4776,12.93,20.97>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR0 { 
    Id  3744010576
    Geometry  Geometry_140569433674488
    Appearance  ecran
}


TriangleSet Geometry_140569433675224 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.4776,12.93,20.97>, 
        <22.4501,12.93,21.0456>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR1 { 
    Id  3744011312
    Geometry  Geometry_140569433675224
    Appearance  ecran
}


TriangleSet Geometry_140569433675960 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.4501,12.93,21.0456>, 
        <22.3804,12.93,21.0858>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR2 { 
    Id  3744012048
    Geometry  Geometry_140569433675960
    Appearance  ecran
}


TriangleSet Geometry_140569433676696 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.3804,12.93,21.0858>, 
        <22.3012,12.93,21.0718>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR3 { 
    Id  3744012784
    Geometry  Geometry_140569433676696
    Appearance  ecran
}


TriangleSet Geometry_140569433677432 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.3012,12.93,21.0718>, 
        <22.2495,12.93,21.0102>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR4 { 
    Id  3744013520
    Geometry  Geometry_140569433677432
    Appearance  ecran
}


TriangleSet Geometry_140569433678168 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.2495,12.93,21.0102>, 
        <22.2495,12.93,20.9298>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR5 { 
    Id  3744014256
    Geometry  Geometry_140569433678168
    Appearance  ecran
}


TriangleSet Geometry_140569433678904 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.2495,12.93,20.9298>, 
        <22.3012,12.93,20.8682>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR6 { 
    Id  3744014992
    Geometry  Geometry_140569433678904
    Appearance  ecran
}


TriangleSet Geometry_140569433679640 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.3012,12.93,20.8682>, 
        <22.3804,12.93,20.8542>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR7 { 
    Id  3744015728
    Geometry  Geometry_140569433679640
    Appearance  ecran
}


TriangleSet Geometry_140569433680376 { 
    PointList [ 
        <22.36,13.08,20.97>, 
        <22.3804,12.93,20.8542>, 
        <22.4501,12.93,20.8944>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AR8 { 
    Id  3744016464
    Geometry  Geometry_140569433680376
    Appearance  ecran
}


TriangleSet Geometry_140569433681112 { 
    PointList [ 
        <22.432,13.143,20.97>, 
        <22.4152,13.143,21.0163>, 
        <22.3725,13.143,21.0409>, 
        <22.324,13.143,21.0324>, 
        <22.2923,13.143,20.9946>, 
        <22.2923,13.143,20.9454>, 
        <22.324,13.143,20.9076>, 
        <22.3725,13.143,20.8991>, 
        <22.4152,13.143,20.9237>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42ARx { 
    Id  3744017200
    Geometry  Geometry_140569433681112
    Appearance  ecran
}


TriangleSet Geometry_140569433682504 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.4289,12.93,21.0279>, 
        <22.45,12.93,20.97>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV0 { 
    Id  3744018592
    Geometry  Geometry_140569433682504
    Appearance  ecran
}


TriangleSet Geometry_140569433683240 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.45,12.93,20.97>, 
        <22.4289,12.93,20.9121>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV1 { 
    Id  3744019328
    Geometry  Geometry_140569433683240
    Appearance  ecran
}


TriangleSet Geometry_140569433683976 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.4289,12.93,20.9121>, 
        <22.3756,12.93,20.8814>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV2 { 
    Id  3744020064
    Geometry  Geometry_140569433683976
    Appearance  ecran
}


TriangleSet Geometry_140569433684712 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.3756,12.93,20.8814>, 
        <22.315,12.93,20.8921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV3 { 
    Id  3744020800
    Geometry  Geometry_140569433684712
    Appearance  ecran
}


TriangleSet Geometry_140569433685448 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.315,12.93,20.8921>, 
        <22.2754,12.93,20.9392>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV4 { 
    Id  3744021536
    Geometry  Geometry_140569433685448
    Appearance  ecran
}


TriangleSet Geometry_140569433686184 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.2754,12.93,20.9392>, 
        <22.2754,12.93,21.0008>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV5 { 
    Id  3744022272
    Geometry  Geometry_140569433686184
    Appearance  ecran
}


TriangleSet Geometry_140569433686920 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.2754,12.93,21.0008>, 
        <22.315,12.93,21.0479>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV6 { 
    Id  3744023008
    Geometry  Geometry_140569433686920
    Appearance  ecran
}


TriangleSet Geometry_140569433687656 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.315,12.93,21.0479>, 
        <22.3756,12.93,21.0586>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV7 { 
    Id  3744023744
    Geometry  Geometry_140569433687656
    Appearance  ecran
}


TriangleSet Geometry_140569433688392 { 
    PointList [ 
        <22.36,12.765,20.97>, 
        <22.3756,12.93,21.0586>, 
        <22.4289,12.93,21.0279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp42AV8 { 
    Id  3744024480
    Geometry  Geometry_140569433688392
    Appearance  ecran
}


TriangleSet Geometry_140569433689128 { 
    PointList [ 
        <1.589,13.12,21.15>, 
        <1.61497,13.12,21.0787>, 
        <1.68073,13.12,21.0407>, 
        <1.7555,13.12,21.0539>, 
        <1.80431,13.12,21.112>, 
        <1.80431,13.12,21.188>, 
        <1.7555,13.12,21.2461>, 
        <1.68073,13.12,21.2593>, 
        <1.61497,13.12,21.2213>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV { 
    Id  3744025216
    Geometry  Geometry_140569433689128
    Appearance  ecran
}


TriangleSet Geometry_140569433690520 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.60991,12.97,21.0744>, 
        <1.5824,12.97,21.15>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR0 { 
    Id  3744026608
    Geometry  Geometry_140569433690520
    Appearance  ecran
}


TriangleSet Geometry_140569433691256 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.5824,12.97,21.15>, 
        <1.60991,12.97,21.2256>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR1 { 
    Id  3744027344
    Geometry  Geometry_140569433691256
    Appearance  ecran
}


TriangleSet Geometry_140569433691992 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.60991,12.97,21.2256>, 
        <1.67958,12.97,21.2658>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR2 { 
    Id  3744028080
    Geometry  Geometry_140569433691992
    Appearance  ecran
}


TriangleSet Geometry_140569433692728 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.67958,12.97,21.2658>, 
        <1.7588,12.97,21.2518>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR3 { 
    Id  3744028816
    Geometry  Geometry_140569433692728
    Appearance  ecran
}


TriangleSet Geometry_140569433693464 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.7588,12.97,21.2518>, 
        <1.81051,12.97,21.1902>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR4 { 
    Id  3744029552
    Geometry  Geometry_140569433693464
    Appearance  ecran
}


TriangleSet Geometry_140569433694200 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.81051,12.97,21.1902>, 
        <1.81051,12.97,21.1098>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR5 { 
    Id  3744030288
    Geometry  Geometry_140569433694200
    Appearance  ecran
}


TriangleSet Geometry_140569433694936 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.81051,12.97,21.1098>, 
        <1.7588,12.97,21.0482>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR6 { 
    Id  3744031024
    Geometry  Geometry_140569433694936
    Appearance  ecran
}


TriangleSet Geometry_140569433695672 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.7588,12.97,21.0482>, 
        <1.67958,12.97,21.0342>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR7 { 
    Id  3744031760
    Geometry  Geometry_140569433695672
    Appearance  ecran
}


TriangleSet Geometry_140569433696408 { 
    PointList [ 
        <1.7,12.82,21.15>, 
        <1.67958,12.97,21.0342>, 
        <1.60991,12.97,21.0744>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AR8 { 
    Id  3744032496
    Geometry  Geometry_140569433696408
    Appearance  ecran
}


TriangleSet Geometry_140569433697144 { 
    PointList [ 
        <1.628,12.757,21.15>, 
        <1.64484,12.757,21.1963>, 
        <1.6875,12.757,21.2209>, 
        <1.736,12.757,21.2124>, 
        <1.76766,12.757,21.1746>, 
        <1.76766,12.757,21.1254>, 
        <1.736,12.757,21.0876>, 
        <1.6875,12.757,21.0791>, 
        <1.64484,12.757,21.1037>
    ]
    IndexList [ 
        [0,1,2], 
        [3,4,5], 
        [6,7,8]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43ARx { 
    Id  3744033232
    Geometry  Geometry_140569433697144
    Appearance  ecran
}


TriangleSet Geometry_140569433698536 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.63106,12.97,21.2079>, 
        <1.61,12.97,21.15>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV0 { 
    Id  3744034624
    Geometry  Geometry_140569433698536
    Appearance  ecran
}


TriangleSet Geometry_140569433699272 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.61,12.97,21.15>, 
        <1.63106,12.97,21.0921>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV1 { 
    Id  3744035360
    Geometry  Geometry_140569433699272
    Appearance  ecran
}


TriangleSet Geometry_140569433700008 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.63106,12.97,21.0921>, 
        <1.68437,12.97,21.0614>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV2 { 
    Id  3744036096
    Geometry  Geometry_140569433700008
    Appearance  ecran
}


TriangleSet Geometry_140569433700744 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.68437,12.97,21.0614>, 
        <1.745,12.97,21.0721>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV3 { 
    Id  3744036832
    Geometry  Geometry_140569433700744
    Appearance  ecran
}


TriangleSet Geometry_140569433701480 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.745,12.97,21.0721>, 
        <1.78457,12.97,21.1192>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV4 { 
    Id  3744037568
    Geometry  Geometry_140569433701480
    Appearance  ecran
}


TriangleSet Geometry_140569433702216 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.78457,12.97,21.1192>, 
        <1.78457,12.97,21.1808>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV5 { 
    Id  3744038304
    Geometry  Geometry_140569433702216
    Appearance  ecran
}


TriangleSet Geometry_140569433702952 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.78457,12.97,21.1808>, 
        <1.745,12.97,21.2279>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV6 { 
    Id  3744039040
    Geometry  Geometry_140569433702952
    Appearance  ecran
}


TriangleSet Geometry_140569433703688 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.745,12.97,21.2279>, 
        <1.68437,12.97,21.2386>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV7 { 
    Id  3744039776
    Geometry  Geometry_140569433703688
    Appearance  ecran
}


TriangleSet Geometry_140569433704424 { 
    PointList [ 
        <1.7,13.135,21.15>, 
        <1.68437,12.97,21.2386>, 
        <1.63106,12.97,21.2079>
    ]
    IndexList [ 
        [0,1,2]
    ]
}


Material ecran { 
    Ambient Black
    Shininess 1
}


Shape lamp43AV8 { 
    Id  3744040512
    Geometry  Geometry_140569433704424
    Appearance  ecran
}


TriangleSet Geometry_140569433705160 { 
    PointList [ 
        <0,4.7,9>, 
        <20.4,4.7,9>, 
        <20.4,13.7,9>, 
        <0,13.7,9>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape tableAMaree { 
    Id  3744041248
    Geometry  Geometry_140569433705160
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433705928 { 
    PointList [ 
        <0,13.7,8.995>, 
        <20.4,13.7,8.995>, 
        <20.4,4.7,8.995>, 
        <0,4.7,8.995>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape soustableAMaree { 
    Id  3744042016
    Geometry  Geometry_140569433705928
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433706696 { 
    PointList [ 
        <0,13.7,7.4>, 
        <0,13.7,9.4>, 
        <20.4,13.7,9.4>, 
        <20.4,13.7,7.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteGtableAMaree { 
    Id  3744042784
    Geometry  Geometry_140569433706696
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433707464 { 
    PointList [ 
        <20.4,13.705,7.4>, 
        <20.4,13.705,9.4>, 
        <0,13.705,9.4>, 
        <0,13.705,7.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteGtableAMareer { 
    Id  3744043552
    Geometry  Geometry_140569433707464
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433708232 { 
    PointList [ 
        <0,4.7,7.4>, 
        <0,4.7,9.4>, 
        <20.4,4.7,9.4>, 
        <20.4,4.7,7.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteDtableAMaree { 
    Id  3744044320
    Geometry  Geometry_140569433708232
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433709000 { 
    PointList [ 
        <20.4,4.695,7.4>, 
        <20.4,4.695,9.4>, 
        <0,4.695,9.4>, 
        <0,4.695,7.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteDtableAMareer { 
    Id  3744045088
    Geometry  Geometry_140569433709000
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433709768 { 
    PointList [ 
        <20.4,4.7,7.4>, 
        <20.4,13.7,7.4>, 
        <20.4,13.7,9.4>, 
        <20.4,4.7,9.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteAVtableAMaree { 
    Id  3744045856
    Geometry  Geometry_140569433709768
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433710536 { 
    PointList [ 
        <20.405,13.7,7.4>, 
        <20.405,4.7,7.4>, 
        <20.405,4.7,9.4>, 
        <20.405,13.7,9.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteAVtableAMareer { 
    Id  3744046624
    Geometry  Geometry_140569433710536
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433711304 { 
    PointList [ 
        <0.01,4.7,7.4>, 
        <0.01,13.7,7.4>, 
        <0.01,13.7,9.4>, 
        <0.01,4.7,9.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteARtableAMaree { 
    Id  3744047392
    Geometry  Geometry_140569433711304
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433712072 { 
    PointList [ 
        <0.005,13.7,7.4>, 
        <0.005,4.7,7.4>, 
        <0.005,4.7,9.4>, 
        <0.005,13.7,9.4>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Aquanappe { 
    Ambient 10
    Specular 76
    Shininess 1
}


Shape coteARtableAMareer { 
    Id  3744048160
    Geometry  Geometry_140569433712072
    Appearance  Aquanappe
}


TriangleSet Geometry_140569433712840 { 
    PointList [ 
        <0,18,19.7>, 
        <24,18,19.7>, 
        <24,18.4,19.7>, 
        <0,18.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheG { 
    Id  3744048928
    Geometry  Geometry_140569433712840
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433713608 { 
    PointList [ 
        <0,18.4,19.7>, 
        <24,18.4,19.7>, 
        <24,18,19.7>, 
        <0,18,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheGr { 
    Id  3744049696
    Geometry  Geometry_140569433713608
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433714376 { 
    PointList [ 
        <0,0,19.7>, 
        <24,0,19.7>, 
        <24,0.4,19.7>, 
        <0,0.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheD { 
    Id  3744050464
    Geometry  Geometry_140569433714376
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433715144 { 
    PointList [ 
        <0,0.4,19.7>, 
        <24,0.4,19.7>, 
        <24,0,19.7>, 
        <0,0,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheDr { 
    Id  3744051232
    Geometry  Geometry_140569433715144
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433715912 { 
    PointList [ 
        <23.6,0,19.7>, 
        <24,0,19.7>, 
        <24,18.4,19.7>, 
        <23.6,18.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheAV { 
    Id  3744052000
    Geometry  Geometry_140569433715912
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433716680 { 
    PointList [ 
        <23.6,18.4,19.7>, 
        <24,18.4,19.7>, 
        <24,0,19.7>, 
        <23.6,0,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheAVr { 
    Id  3744052768
    Geometry  Geometry_140569433716680
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433717448 { 
    PointList [ 
        <0,0,19.7>, 
        <0.4,0,19.7>, 
        <0.4,18.4,19.7>, 
        <0,18.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheAR { 
    Id  3744053536
    Geometry  Geometry_140569433717448
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433718216 { 
    PointList [ 
        <0,18.4,19.7>, 
        <0.4,18.4,19.7>, 
        <0.4,0,19.7>, 
        <0,0,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CorniereAlu { 
    Ambient 169
    Diffuse 1.50888
    Specular 76
    Shininess 1
}


Shape cornicheARr { 
    Id  3744054304
    Geometry  Geometry_140569433718216
    Appearance  CorniereAlu
}


TriangleSet Geometry_140569433718984 { 
    PointList [ 
        <0,0,19.7>, 
        <0,0,21.8>, 
        <24,0,21.8>, 
        <24,0,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurMetal { 
    Ambient 164
    Diffuse 1.55488
    Specular 76
    Shininess 1
}


Shape caissonx0 { 
    Id  3744055072
    Geometry  Geometry_140569433718984
    Appearance  MurMetal
}


TriangleSet Geometry_140569433719752 { 
    PointList [ 
        <24,18.4,19.7>, 
        <24,18.4,21.8>, 
        <0,18.4,21.8>, 
        <0,18.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurMetal { 
    Ambient 164
    Diffuse 1.55488
    Specular 76
    Shininess 1
}


Shape caissonx1 { 
    Id  3744055840
    Geometry  Geometry_140569433719752
    Appearance  MurMetal
}


TriangleSet Geometry_140569433720520 { 
    PointList [ 
        <0,0,19.7>, 
        <0,18.4,19.7>, 
        <0,18.4,21.8>, 
        <0,0,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurBlanc { 
    Ambient 196
    Diffuse 1.30102
    Specular 51
    Shininess 1
}


Shape caissony0 { 
    Id  3744056608
    Geometry  Geometry_140569433720520
    Appearance  MurBlanc
}


TriangleSet Geometry_140569433721288 { 
    PointList [ 
        <24,18.4,19.7>, 
        <24,0,19.7>, 
        <24,0,21.8>, 
        <24,18.4,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MurBlanc { 
    Ambient 196
    Diffuse 1.30102
    Specular 51
    Shininess 1
}


Shape caissony1 { 
    Id  3744057376
    Geometry  Geometry_140569433721288
    Appearance  MurBlanc
}


TriangleSet Geometry_140569433722056 { 
    PointList [ 
        <0.5,0.5,20.35>, 
        <0.5,0.5,21.8>, 
        <23.5,0.5,21.8>, 
        <23.5,0.5,20.35>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refcaissonX0n { 
    Id  3744058144
    Geometry  Geometry_140569433722056
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433722824 { 
    PointList [ 
        <23.5,0.5,20.35>, 
        <23.5,0.5,21.8>, 
        <0.5,0.5,21.8>, 
        <0.5,0.5,20.35>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refcaissonX0a { 
    Id  3744058912
    Geometry  Geometry_140569433722824
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433723592 { 
    PointList [ 
        <0.5,17.9,20.35>, 
        <0.5,17.9,21.8>, 
        <23.5,17.9,21.8>, 
        <23.5,17.9,20.35>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refcaissonXYn { 
    Id  3744059680
    Geometry  Geometry_140569433723592
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433724360 { 
    PointList [ 
        <23.5,17.9,20.35>, 
        <23.5,17.9,21.8>, 
        <0.5,17.9,21.8>, 
        <0.5,17.9,20.35>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refcaissonXYa { 
    Id  3744060448
    Geometry  Geometry_140569433724360
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433725128 { 
    PointList [ 
        <23.5,0.5,20.35>, 
        <23.5,17.9,20.35>, 
        <23.5,17.9,21.8>, 
        <23.5,0.5,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refcaissonY0n { 
    Id  3744061216
    Geometry  Geometry_140569433725128
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433725896 { 
    PointList [ 
        <23.5,17.9,20.35>, 
        <23.5,0.5,20.35>, 
        <23.5,0.5,21.8>, 
        <23.5,17.9,21.8>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refcaissonY0a { 
    Id  3744061984
    Geometry  Geometry_140569433725896
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433726664 { 
    PointList [ 
        <0.25,18.15,21.799>, 
        <23.75,18.15,21.799>, 
        <23.75,0.25,21.799>, 
        <0.25,0.25,21.799>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material MiroirCaissonLampes { 
    Ambient 143
    Diffuse 1.78322
    Specular 102
    Shininess 1
}


Shape refPlafond { 
    Id  3744062752
    Geometry  Geometry_140569433726664
    Appearance  MiroirCaissonLampes
}


TriangleSet Geometry_140569433727432 { 
    PointList [ 
        <7.7,13.65,21.798>, 
        <16.3,13.65,21.798>, 
        <16.3,4.75,21.798>, 
        <7.7,4.75,21.798>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material CentrePlafond { 
    Ambient 138
    Diffuse 1.84783
    Specular 127
    Shininess 1
}


Shape depoli { 
    Id  3744063520
    Geometry  Geometry_140569433727432
    Appearance  CentrePlafond
}


TriangleSet Geometry_140569433728200 { 
    PointList [ 
        <0,0,19.7>, 
        <24,0,19.7>, 
        <24,18.4,19.7>, 
        <0,18.4,19.7>
    ]
    IndexList [ 
        [0,1,2], 
        [0,2,3]
    ]
}


Material Makrolon { 
    Ambient 41
    Specular 76
    Shininess 0.5
    Transparency 0.755474
}


Shape fauxPlafondInf { 
    Id  3744064288
    Geometry  Geometry_140569433728200
    Appearance  Makrolon
}


