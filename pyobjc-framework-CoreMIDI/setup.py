"""
Wrappers for the "CoreMIDI" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "7.0a1"

setup(
    name="pyobjc-framework-CoreMIDI",
    description="Wrappers for the framework CoreMIDI on macOS",
    packages=["CoreMIDI"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)