/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(NSFileProviderItem)); Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1103
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingOperation)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingIngestion)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingLookup)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingContentFetch)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingChildrenEnumeration)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingCreation)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingModification)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingDeletion)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFileProviderTestingCollisionResolution)); Py_XDECREF(p);
#endif
}
