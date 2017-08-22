# This file is generated by objective.metadata
#
# Last update: Tue Aug 22 21:52:38 2017

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$VNBarcodeSymbologyAztec$VNBarcodeSymbologyCode128$VNBarcodeSymbologyCode39$VNBarcodeSymbologyCode39Checksum$VNBarcodeSymbologyCode39FullASCII$VNBarcodeSymbologyCode39FullASCIIChecksum$VNBarcodeSymbologyCode93$VNBarcodeSymbologyCode93i$VNBarcodeSymbologyDataMatrix$VNBarcodeSymbologyEAN13$VNBarcodeSymbologyEAN8$VNBarcodeSymbologyI2of5$VNBarcodeSymbologyI2of5Checksum$VNBarcodeSymbologyITF14$VNBarcodeSymbologyPDF417$VNBarcodeSymbologyQR$VNBarcodeSymbologyUPCE$VNImageOptionCameraIntrinsics$VNImageOptionProperties$VNNormalizedIdentityRect@{CGRect={CGPoint=dd}{CGSize=dd}}$VNVisionVersionNumber@d$'''
enums = '''$VNErrorIOError@6$VNErrorInternalError@9$VNErrorInvalidArgument@14$VNErrorInvalidFormat@2$VNErrorInvalidImage@13$VNErrorInvalidModel@15$VNErrorInvalidOperation@12$VNErrorInvalidOption@5$VNErrorMissingOption@7$VNErrorNotImplemented@8$VNErrorOK@0$VNErrorOperationFailed@3$VNErrorOutOfBoundsError@4$VNErrorOutOfMemory@10$VNErrorRequestCancelled@1$VNErrorUnknownError@11$VNImageCropAndScaleOptionCenterCrop@0$VNImageCropAndScaleOptionScaleFill@2$VNImageCropAndScaleOptionScaleFit@1$VNRequestTrackingLevelAccurate@0$VNRequestTrackingLevelFast@1$'''
misc.update({})
functions={'VNImageRectForNormalizedRect': (b'{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}LL',), 'VNNormalizedRectIsIdentityRect': (b'B{CGRect={CGPoint=dd}{CGSize=dd}}',), 'VNImagePointForNormalizedPoint': (b'{CGPoint=dd}{CGPoint=dd}LL',), 'VNNormalizedRectForImageRect': (b'{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}LL',)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'VNCoreMLModel', b'modelForMLModel:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'VNCoreMLRequest', b'initWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNCoreMLRequest', b'initWithModel:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNDetectTextRectanglesRequest', b'reportCharacterBoxes', {'retval': {'type': 'Z'}})
    r(b'VNDetectTextRectanglesRequest', b'setReportCharacterBoxes:', {'arguments': {2: {'type': 'Z'}}})
    r(b'VNFaceLandmarkRegion', b'normalizedPoints', {'retval': {'c_array_of_variable_length': True}})
    r(b'VNFaceLandmarkRegion', b'pointsInImageOfSize:', {'retval': {'c_array_of_variable_length': True}})
    r(b'VNImageRequestHandler', b'performRequests:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'VNRequest', b'completionHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'VNRequest', b'initWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNRequest', b'preferBackgroundProcessing', {'retval': {'type': 'Z'}})
    r(b'VNRequest', b'setPreferBackgroundProcessing:', {'arguments': {2: {'type': 'Z'}}})
    r(b'VNRequest', b'setUsesCPUOnly:', {'arguments': {2: {'type': 'Z'}}})
    r(b'VNRequest', b'usesCPUOnly', {'retval': {'type': 'Z'}})
    r(b'VNSequenceRequestHandler', b'performRequests:onCGImage:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onCGImage:orientation:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onCIImage:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onCIImage:orientation:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onCVPixelBuffer:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onCVPixelBuffer:orientation:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onImageData:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onImageData:orientation:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onImageURL:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'VNSequenceRequestHandler', b'performRequests:onImageURL:orientation:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'VNTargetedImageRequest', b'initWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCGImage:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCGImage:options:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCGImage:orientation:options:completionHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCIImage:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCIImage:options:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCIImage:orientation:options:completionHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCVPixelBuffer:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCVPixelBuffer:options:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedCVPixelBuffer:orientation:options:completionHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedImageData:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedImageData:options:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedImageData:orientation:options:completionHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedImageURL:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedImageURL:options:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTargetedImageRequest', b'initWithTargetedImageURL:orientation:options:completionHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTrackObjectRequest', b'initWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTrackObjectRequest', b'initWithDetectedObjectObservation:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTrackRectangleRequest', b'initWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTrackRectangleRequest', b'initWithRectangleObservation:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTrackingRequest', b'initWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'VNTrackingRequest', b'isLastFrame', {'retval': {'type': 'Z'}})
    r(b'VNTrackingRequest', b'setLastFrame:', {'arguments': {2: {'type': 'Z'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
