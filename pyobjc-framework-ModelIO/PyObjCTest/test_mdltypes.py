from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import objc
import ModelIO


class TestMDLTypesHelper(ModelIO.NSObject):
    def objectAtIndexedSubscript_(self, i):
        return 1


class TestMDLTypes(TestCase):
    def testConstants(self):
        self.assertIsInstance(ModelIO.kUTTypeAlembic, str)
        self.assertIsInstance(ModelIO.kUTType3dObject, str)
        self.assertIsInstance(ModelIO.kUTTypePolygon, str)
        self.assertIsInstance(ModelIO.kUTTypeStereolithography, str)

        self.assertEqual(ModelIO.MDLDataPrecisionUndefined, 0)
        self.assertEqual(ModelIO.MDLDataPrecisionFloat, 1)
        self.assertEqual(ModelIO.MDLDataPrecisionDouble, 2)

        self.assertEqual(ModelIO.MDLIndexBitDepthInvalid, 0)
        self.assertEqual(ModelIO.MDLIndexBitDepthUInt8, 8)
        self.assertEqual(ModelIO.MDLIndexBitDepthUint8, 8)
        self.assertEqual(ModelIO.MDLIndexBitDepthUInt16, 16)
        self.assertEqual(ModelIO.MDLIndexBitDepthUint16, 16)
        self.assertEqual(ModelIO.MDLIndexBitDepthUInt32, 32)
        self.assertEqual(ModelIO.MDLIndexBitDepthUint32, 32)

        self.assertEqual(ModelIO.MDLGeometryTypePoints, 0)
        self.assertEqual(ModelIO.MDLGeometryTypeLines, 1)
        self.assertEqual(ModelIO.MDLGeometryTypeTriangles, 2)
        self.assertEqual(ModelIO.MDLGeometryTypeTriangleStrips, 3)
        self.assertEqual(ModelIO.MDLGeometryTypeQuads, 4)
        self.assertEqual(ModelIO.MDLGeometryTypeVariableTopology, 5)

        self.assertEqual(ModelIO.MDLProbePlacementUniformGrid, 0)
        self.assertEqual(ModelIO.MDLProbePlacementIrradianceDistribution, 1)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(ModelIO.kUTTypeUniversalSceneDescription, str)

    def testProtocolObjects(self):
        objc.protocolNamed("MDLNamed")
        objc.protocolNamed("MDLComponent")
        objc.protocolNamed("MDLObjectContainerComponent")

    def testMethods(self):
        self.assertArgHasType(
            TestMDLTypesHelper.objectAtIndexedSubscript_, 0, objc._C_NSUInteger
        )

    @expectedFailure
    def testStructs(self):
        self.fail("MDLAxisAlignedBoundingBox is SIMD type")
