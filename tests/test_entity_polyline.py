# Created: 21.07.12
# License: MIT License
from __future__ import unicode_literals
__author__ = "mozman <mozman@gmx.at>"

import unittest
from dxfgrabber.tags import Tags
from dxfgrabber.entitysection import EntitySection


class DrawingProxy:
    def __init__(self, version):
        self.dxfversion = version


class TestPolylineDXF12(unittest.TestCase):
    def setUp(self):
        tags = Tags.from_text(POLYLINE_DXF12)
        self.entities = EntitySection.from_tags(tags, DrawingProxy('AC1009'))

    def test_polyline(self):
        self.assertEqual(len(self.entities), 1)

    def test_polyline_attribs(self):
        polyline = self.entities[0]
        self.assertEqual(polyline.default_start_width, 0.5)
        self.assertEqual(polyline.default_end_width, 0.6)

    def test_polyline_data(self):
        polyline = self.entities[0]
        self.assertEqual(len(polyline), 4)

    def test_polyline_points(self):
        polyline = self.entities[0]
        self.assertEqual(polyline.points[3], (0., 1., 0.))

    def test_polyline_width(self):
        polyline = self.entities[0]
        self.assertEqual(len(polyline.width), len(polyline.points))
        start_width, end_width = polyline.width[0]
        self.assertEqual(1.0, start_width)
        self.assertEqual(2.0, end_width)
        start_width, end_width = polyline.width[1]
        self.assertEqual(0.5, start_width)
        self.assertEqual(0.6, end_width)

    def test_polyline_bulge(self):
        polyline = self.entities[0]
        self.assertEqual(len(polyline.bulge), len(polyline.points))


class TestPolylineDXF13(unittest.TestCase):
    def setUp(self):
        tags = Tags.from_text(POLYLINE_DXF13)
        self.entities = EntitySection.from_tags(tags, DrawingProxy('AC1024'))


class Test2DSplineDXF12(unittest.TestCase):
    def setUp(self):
        tags = Tags.from_text(POLYLINE_2D_SPLINE)
        self.entities = EntitySection.from_tags(tags, DrawingProxy('AC1009'))

    def test_2d_spline_type(self):
        spline = self.entities[0]
        self.assertEqual('spline2d', spline.mode)

    def test_get_spline_points(self):
        spline = self.entities[0]
        self.assertEqual("cubic_bspline", spline.spline_type)
        self.assertTrue(spline.is_closed)
        self.assertEqual(60, len(spline.points))
        self.assertEqual(60, len(spline.tangents))
        self.assertEqual(6, len(spline.controlpoints))



POLYLINE_DXF13 = """  0
SECTION
  2
ENTITIES
  0
ENDSEC
"""

POLYLINE_DXF12 = """  0
SECTION
  2
ENTITIES
  0
POLYLINE
 62
7
  8
mozman
 66
1
 10
0.0
 20
0.0
 30
0.0
 70
8
 40
 0.5
 41
 0.6
  0
VERTEX
  8
0
 10
0.0
 20
0.0
 30
0.0
 40
 1.0
 41
 2.0
  0
VERTEX
  8
0
 10
1.0
 20
0.0
 30
0.0
  0
VERTEX
  8
0
 10
1.0
 20
1.0
 30
0.0
  0
VERTEX
  8
0
 10
0.0
 20
1.0
 30
0.0
  0
SEQEND
  0
ENDSEC
"""

POLYLINE_2D_SPLINE = """  0
SECTION
  2
ENTITIES
  0
POLYLINE
  5
298
  8
T-2DPLINE-CURVE
 66
     1
 10
0.0
 20
0.0
 30
6.0
 39
1.0
 70
     5
 40
0.5
 41
0.5
 75
     6
  0
VERTEX
  5
299
  8
T-2DPLINE-CURVE
 10
0.7332608367727893
 20
-5.4530081530669481
 30
6.0
 70
    16
  0
VERTEX
  5
29A
  8
T-2DPLINE-CURVE
 10
-0.2335983188724278
 20
-6.822587874955695
 30
6.0
 70
     8
  0
VERTEX
  5
29B
  8
T-2DPLINE-CURVE
 10
-0.5507281219240592
 20
-6.8963047629762722
 30
6.0
 70
     8
  0
VERTEX
  5
29C
  8
T-2DPLINE-CURVE
 10
-0.9142671644466606
 20
-6.9521441925656919
 30
6.0
 70
     8
  0
VERTEX
  5
29D
  8
T-2DPLINE-CURVE
 10
-1.31261313657249
 20
-6.9886636619554627
 30
6.0
 70
     8
  0
VERTEX
  5
29E
  8
T-2DPLINE-CURVE
 10
-1.7341637284338041
 20
-7.0044206693770947
 30
6.0
 70
     8
  0
VERTEX
  5
29F
  8
T-2DPLINE-CURVE
 10
-2.1673166301628601
 20
-6.9979727130620928
 30
6.0
 70
     8
  0
VERTEX
  5
2A0
  8
T-2DPLINE-CURVE
 10
-2.600469531891918
 20
-6.9678772912419671
 30
6.0
 70
     8
  0
VERTEX
  5
2A1
  8
T-2DPLINE-CURVE
 10
-3.022020123753232
 20
-6.912691902148226
 30
6.0
 70
     8
  0
VERTEX
  5
2A2
  8
T-2DPLINE-CURVE
 10
-3.4203660958790612
 20
-6.8309740440123772
 30
6.0
 70
     8
  0
VERTEX
  5
2A3
  8
T-2DPLINE-CURVE
 10
-3.7839051384016642
 20
-6.7212812150659271
 30
6.0
 70
     8
  0
VERTEX
  5
2A4
  8
T-2DPLINE-CURVE
 10
-4.1010349414532961
 20
-6.5821709135403861
 30
6.0
 70
     8
  0
VERTEX
  5
2A5
  8
T-2DPLINE-CURVE
 10
-4.3627979771506968
 20
-6.413692869097515
 30
6.0
 70
     8
  0
VERTEX
  5
2A6
  8
T-2DPLINE-CURVE
 10
-4.5708158455485526
 20
-6.2218657371200878
 30
6.0
 70
     8
  0
VERTEX
  5
2A7
  8
T-2DPLINE-CURVE
 10
-4.7293549286860239
 20
-6.014200404421131
 30
6.0
 70
     8
  0
VERTEX
  5
2A8
  8
T-2DPLINE-CURVE
 10
-4.8426816086022804
 20
-5.7982077578136737
 30
6.0
 70
     8
  0
VERTEX
  5
2A9
  8
T-2DPLINE-CURVE
 10
-4.9150622673364799
 20
-5.5813986841107432
 30
6.0
 70
     8
  0
VERTEX
  5
2AA
  8
T-2DPLINE-CURVE
 10
-4.9507632869277938
 20
-5.3712840701253644
 30
6.0
 70
     8
  0
VERTEX
  5
2AB
  8
T-2DPLINE-CURVE
 10
-4.9540510494153871
 20
-5.1753748026705662
 30
6.0
 70
     8
  0
VERTEX
  5
2AC
  8
T-2DPLINE-CURVE
 10
-4.9291919368384223
 20
-5.001181768559376
 30
6.0
 70
     8
  0
VERTEX
  5
2AD
  8
T-2DPLINE-CURVE
 10
-4.8804523312360626
 20
-4.8562158546048231
 30
6.0
 70
     8
  0
VERTEX
  5
2AE
  8
T-2DPLINE-CURVE
 10
-4.8120986146474767
 20
-4.7479879476199311
 30
6.0
 70
     8
  0
VERTEX
  5
2AF
  8
T-2DPLINE-CURVE
 10
-4.7277809431633369
 20
-4.6815733410713429
 30
6.0
 70
     8
  0
VERTEX
  5
2B0
  8
T-2DPLINE-CURVE
 10
-4.6286845690803453
 20
-4.6523049550401581
 30
6.0
 70
     8
  0
VERTEX
  5
2B1
  8
T-2DPLINE-CURVE
 10
-4.5153785187467088
 20
-4.6530801162610782
 30
6.0
 70
     8
  0
VERTEX
  5
2B2
  8
T-2DPLINE-CURVE
 10
-4.3884318185106403
 20
-4.6767961514688192
 30
6.0
 70
     8
  0
VERTEX
  5
2B3
  8
T-2DPLINE-CURVE
 10
-4.2484134947203449
 20
-4.7163503873980881
 30
6.0
 70
     8
  0
VERTEX
  5
2B4
  8
T-2DPLINE-CURVE
 10
-4.095892573724039
 20
-4.764640150783598
 30
6.0
 70
     8
  0
VERTEX
  5
2B5
  8
T-2DPLINE-CURVE
 10
-3.9314380818699242
 20
-4.814562768360056
 30
6.0
 70
     8
  0
VERTEX
  5
2B6
  8
T-2DPLINE-CURVE
 10
-3.7556190455062151
 20
-4.8590155668621691
 30
6.0
 70
     8
  0
VERTEX
  5
2B7
  8
T-2DPLINE-CURVE
 10
-3.569004490981118
 20
-4.8908958730246521
 30
6.0
 70
     8
  0
VERTEX
  5
2B8
  8
T-2DPLINE-CURVE
 10
-3.3721634446428439
 20
-4.9031010135822077
 30
6.0
 70
     8
  0
VERTEX
  5
2B9
  8
T-2DPLINE-CURVE
 10
-3.165853495679857
 20
-4.8906219570802723
 30
6.0
 70
     8
  0
VERTEX
  5
2BA
  8
T-2DPLINE-CURVE
 10
-2.9515864846416422
 20
-4.8568242393071461
 30
6.0
 70
     8
  0
VERTEX
  5
2BB
  8
T-2DPLINE-CURVE
 10
-2.7310628149179319
 20
-4.8071670378618547
 30
6.0
 70
     8
  0
VERTEX
  5
2BC
  8
T-2DPLINE-CURVE
 10
-2.50598288989847
 20
-4.7471095303434243
 30
6.0
 70
     8
  0
VERTEX
  5
2BD
  8
T-2DPLINE-CURVE
 10
-2.2780471129729878
 20
-4.6821108943508722
 30
6.0
 70
     8
  0
VERTEX
  5
2BE
  8
T-2DPLINE-CURVE
 10
-2.0489558875312279
 20
-4.6176303074832257
 30
6.0
 70
     8
  0
VERTEX
  5
2BF
  8
T-2DPLINE-CURVE
 10
-1.8204096169629249
 20
-4.55912694733951
 30
6.0
 70
     8
  0
VERTEX
  5
2C0
  8
T-2DPLINE-CURVE
 10
-1.59410870465782
 20
-4.5120599915187478
 30
6.0
 70
     8
  0
VERTEX
  5
2C1
  8
T-2DPLINE-CURVE
 10
-1.371753554005646
 20
-4.4818886176199673
 30
6.0
 70
     8
  0
VERTEX
  5
2C2
  8
T-2DPLINE-CURVE
 10
-1.155044568396143
 20
-4.474072003242183
 30
6.0
 70
     8
  0
VERTEX
  5
2C3
  8
T-2DPLINE-CURVE
 10
-0.9455706182798802
 20
-4.492729396415549
 30
6.0
 70
     8
  0
VERTEX
  5
2C4
  8
T-2DPLINE-CURVE
 10
-0.7444744423507462
 20
-4.5366203268947141
 30
6.0
 70
     8
  0
VERTEX
  5
2C5
  8
T-2DPLINE-CURVE
 10
-0.5527872463634634
 20
-4.6031643948654484
 30
6.0
 70
     8
  0
VERTEX
  5
2C6
  8
T-2DPLINE-CURVE
 10
-0.3715402360727527
 20
-4.6897812005135231
 30
6.0
 70
     8
  0
VERTEX
  5
2C7
  8
T-2DPLINE-CURVE
 10
-0.2017646172333356
 20
-4.7938903440247129
 30
6.0
 70
     8
  0
VERTEX
  5
2C8
  8
T-2DPLINE-CURVE
 10
-0.0444915955999334
 20
-4.9129114255847881
 30
6.0
 70
     8
  0
VERTEX
  5
2C9
  8
T-2DPLINE-CURVE
 10
0.0992476230727326
 20
-5.0442640453795198
 30
6.0
 70
     8
  0
VERTEX
  5
2CA
  8
T-2DPLINE-CURVE
 10
0.2284218330299415
 20
-5.1853678035946853
 30
6.0
 70
     8
  0
VERTEX
  5
2CB
  8
T-2DPLINE-CURVE
 10
0.3419998285169714
 20
-5.3336423004160496
 30
6.0
 70
     8
  0
VERTEX
  5
2CC
  8
T-2DPLINE-CURVE
 10
0.4389504037791019
 20
-5.4865071360293891
 30
6.0
 70
     8
  0
VERTEX
  5
2CD
  8
T-2DPLINE-CURVE
 10
0.5177416719647461
 20
-5.641504562328838
 30
6.0
 70
     8
  0
VERTEX
  5
2CE
  8
T-2DPLINE-CURVE
 10
0.5748390218348596
 20
-5.7966674380419949
 30
6.0
 70
     8
  0
VERTEX
  5
2CF
  8
T-2DPLINE-CURVE
 10
0.6062071610535336
 20
-5.9501512736048161
 30
6.0
 70
     8
  0
VERTEX
  5
2D0
  8
T-2DPLINE-CURVE
 10
0.6078107972848588
 20
-6.1001115794532579
 30
6.0
 70
     8
  0
VERTEX
  5
2D1
  8
T-2DPLINE-CURVE
 10
0.5756146381929264
 20
-6.2447038660232819
 30
6.0
 70
     8
  0
VERTEX
  5
2D2
  8
T-2DPLINE-CURVE
 10
0.5055833914418262
 20
-6.3820836437508479
 30
6.0
 70
     8
  0
VERTEX
  5
2D3
  8
T-2DPLINE-CURVE
 10
0.3936817646956503
 20
-6.5104064230719141
 30
6.0
 70
     8
  0
VERTEX
  5
2D4
  8
T-2DPLINE-CURVE
 10
0.2358744656184886
 20
-6.6278277144224367
 30
6.0
 70
     8
  0
VERTEX
  5
2D5
  8
T-2DPLINE-CURVE
 10
0.0281262018744326
 20
-6.7325030282383791
 30
6.0
 70
     8
  0
VERTEX
  5
2D6
  8
T-2DPLINE-CURVE
 10
0.7332608367727893
 20
-7.096503819333444
 30
6.0
 70
    16
  0
VERTEX
  5
2D7
  8
T-2DPLINE-CURVE
 10
-5.0678940970985131
 20
-7.096503819333444
 30
6.0
 70
    16
  0
VERTEX
  5
2D8
  8
T-2DPLINE-CURVE
 10
-5.0678940970985131
 20
-4.0105063845750957
 30
6.0
 70
    16
  0
VERTEX
  5
2D9
  8
T-2DPLINE-CURVE
 10
-3.5331212023923042
 20
-5.3493983280857629
 30
6.0
 70
    16
  0
VERTEX
  5
2DA
  8
T-2DPLINE-CURVE
 10
-1.0326017611893361
 20
-4.0105063845750957
 30
6.0
 70
    16
  0
SEQEND
  5
2DB
  8
T-2DPLINE-CURVE
  0
ENDSEC
"""