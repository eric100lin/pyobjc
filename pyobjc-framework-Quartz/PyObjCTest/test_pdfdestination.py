from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestPDFDestination(TestCase):
    def testConstants(self):
        # XXX: In the 10.13 SDK this is een "extern" defintion istead of an
        # #define.
        self.assertEqual(Quartz.kPDFDestinationUnspecifiedValue, objc._FLT_MAX)
