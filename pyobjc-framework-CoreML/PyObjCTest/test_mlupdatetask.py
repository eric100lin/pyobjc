from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLUpdateTask(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            CoreML.MLUpdateTask.updateTaskForModelAtURL_trainingData_configuration_completionHandler_error_,
            3,
            b"v@",
        )
        self.assertArgIsOut(
            CoreML.MLUpdateTask.updateTaskForModelAtURL_trainingData_configuration_completionHandler_error_,
            4,
        )

        self.assertArgIsOut(
            CoreML.MLUpdateTask.updateTaskForModelAtURL_trainingData_configuration_progressHandlers_error_,
            4,
        )
