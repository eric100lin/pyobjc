# This file is generated by objective.metadata
#
# Last update: Mon Mar 16 21:51:29 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$OSAScriptErrorAppAddressKey$OSAScriptErrorAppName$OSAScriptErrorAppNameKey$OSAScriptErrorBriefMessage$OSAScriptErrorBriefMessageKey$OSAScriptErrorExpectedTypeKey$OSAScriptErrorMessage$OSAScriptErrorMessageKey$OSAScriptErrorNumber$OSAScriptErrorNumberKey$OSAScriptErrorOffendingObjectKey$OSAScriptErrorPartialResultKey$OSAScriptErrorRange$OSAScriptErrorRangeKey$OSAStorageApplicationBundleType$OSAStorageApplicationType$OSAStorageScriptBundleType$OSAStorageScriptType$OSAStorageTextType$"""
enums = """$OSACompileIntoContext@2$OSADontSetScriptLocation@16777216$OSANull@0$OSAPreventGetSource@1$OSAScriptRecording@2$OSAScriptRunning@1$OSAScriptStopped@0$OSAShowStartupScreen@536870912$OSAStayOpenApplet@268435456$OSASupportsAECoercion@8$OSASupportsAESending@16$OSASupportsCompiling@2$OSASupportsConvenience@64$OSASupportsDialects@128$OSASupportsEventHandling@256$OSASupportsGetSource@4$OSASupportsRecording@32$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"OSALanguage", b"isThreadSafe", {"retval": {"type": b"Z"}})
    r(
        b"OSAScript",
        b"compileAndReturnError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"compiledDataForType:usingStorageOptions:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"executeAndReturnDisplayValue:error:",
        {"arguments": {2: {"type_modifier": b"o"}, 3: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"executeAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"executeAppleEvent:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"executeHandlerWithName:arguments:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"initWithCompiledData:error:",
        {"deprecated": 1006, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"initWithCompiledData:fromURL:usingStorageOptions:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"initWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"initWithContentsOfURL:language:error:",
        {"deprecated": 1006, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"initWithContentsOfURL:languageInstance:usingStorageOptions:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"initWithScriptDataDescriptor:fromURL:languageInstance:usingStorageOptions:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(b"OSAScript", b"isCompiled", {"retval": {"type": b"Z"}})
    r(
        b"OSAScript",
        b"writeToURL:ofType:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"OSAScript",
        b"writeToURL:ofType:usingStorageOptions:error:",
        {"retval": {"type": b"Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(b"OSAScriptController", b"isCompiling", {"retval": {"type": b"Z"}})
    r(b"OSAScriptView", b"indentsWrappedLines", {"retval": {"type": b"Z"}})
    r(b"OSAScriptView", b"setIndentsWrappedLines:", {"arguments": {2: {"type": b"Z"}}})
    r(b"OSAScriptView", b"setUsesScriptAssistant:", {"arguments": {2: {"type": b"Z"}}})
    r(b"OSAScriptView", b"setUsesTabs:", {"arguments": {2: {"type": b"Z"}}})
    r(b"OSAScriptView", b"setWrapsLines:", {"arguments": {2: {"type": b"Z"}}})
    r(b"OSAScriptView", b"usesScriptAssistant", {"retval": {"type": b"Z"}})
    r(b"OSAScriptView", b"usesTabs", {"retval": {"type": b"Z"}})
    r(b"OSAScriptView", b"wrapsLines", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
