
Much of what's below isn't entirely accurate, able to get a crash correctly, just need to have NumPy before the other imports. See [email.txt](email.txt) for current analysis of the issue.




PYTHONHOME=C:\Python27\ArcGIS10.3
PYTHONPATH=%PYTHONHOME%;%PYTHONHOME%\Lib;%PYTHONHOME\DLLs

[Setting PYTHONPATH for ArcPy](https://pythongisandstuff.wordpress.com/2013/07/10/locating-python-adding-to-path-and-accessing-arcpy/)


Resources
---------

Mention on [GeoNet](https://geonet.esri.com/thread/121352) along with details and approaches.

'revisit' on the issue:
 - [Kube](http://kube.esri.com/index.cfm?event=ehContent.dspContent&type=NimbusBugs&id=BUG-000088701)
 - [CR](http://qamonitor/QACommon/CrLookup.aspx?id2=805554)

original issue (fixed 1.1):
 - [Kube](http://kube.esri.com/index.cfm?event=ehcontent.dspcontent&type=nimbusbugs&id=bug-000086098&kw=000086098)
 - [CR](http://qamonitor/QACommon/CrLookup.aspx?cr=308525)


PYTHONPATH
----------


manually setting the `PYTHONPATH` variable:

 - ArcGIS 10.3:

    "C:\Python27\ArcGIS10.3";"C:\Program Files (x86)\ArcGIS\Desktop10.3\bin";"C:\Program Files (x86)\ArcGIS\Desktop10.3\ArcPy"

 - ArcGIS 10.4:

    "C:\Python27\ArcGIS10.4";"C:\Program Files (x86)\ArcGIS\Desktop10.4\bin";"C:\Program Files (x86)\ArcGIS\Desktop10.4\ArcPy"

 - ArcGIS 10.4 dev:
    "C:\Python27\ArcGIS10.4";"C:\ArcGIS\bin";"C:\ArcGIS\ArcPy"



[details on how PYTHONPATH is set](http://kube.esri.com/index.cfm?event=ehcontent.dspcontent&type=supportincidents&id=1304308&kw=PYTHONPATH):

> Provided the following information to the user: The PYTHONPATH variable which can be used to specify where Python program modules like the ArcGIS modules are located. Through ArcGIS 9.3 ESRI used it to point to C:\Program Files\ArcGIS\bin (or on a 64-bit system that would be C:\Program Files (x86)\ArcGIS\bin) But at ArcGIS 10.0 it is no longer being set during installation. ESRI has instead added the Desktop10.pth configuration file. So if you have a %PYTHONPATH% set it may be held over from the prior ArcGIS 9.3 install or from components you loaded with Python 2.7, and so may be pointing to the wrong ArcGIS module location. Clear any ArcGIS content from PYTHONPATH 


...


OK, so potentially PYTHONPATH could include modules that the user wants to include in their Python environment. So, if they have 2.x and 3.x installed (as they do in the Pro+10.x case), then all of these paths potentially could point at the other installed location





...

Python Doc on `PYTHONPATH`:

PYTHONPATH

    Augment the default search path for module files. The format is the same as the shell’s PATH: one or more directory pathnames separated by os.pathsep (e.g. colons on Unix or semicolons on Windows). Non-existent directories are silently ignored.

    In addition to normal directories, individual PYTHONPATH entries may refer to zipfiles containing pure Python modules (in either source or compiled form). Extension modules cannot be imported from zipfiles.

    The default search path is installation dependent, but generally begins with prefix/lib/pythonversion (see PYTHONHOME above). It is always appended to PYTHONPATH.

    An additional directory will be inserted in the search path in front of PYTHONPATH as described above under Interface options. The search path can be manipulated from within a Python program as the variable sys.path.


[User post on ArcPy + Python](https://pythongisandstuff.wordpress.com/2013/07/10/locating-python-adding-to-path-and-accessing-arcpy/)


related minor thread, includes an issue where invalid license doesn't give a helpful error:
[Invalid license causes failed import](https://geonet.esri.com/thread/116150)


...


in the core InProcServer.cpp Initialize:

```cpp
FileSystemPath pythonPath = ESRISxS::GetCurrentInstallDir();
pythonPath.AppendFile(L"bin\\Python"); // this contains our DLLs, the Python DLL we want to use, and the core libraries.

// ... then a bunch more stuff to add our core Python environment.


// this function looks to be our processor for an 'import' statement. The pyd is crashing, so too late to matter
// for the problem we're having.
void ProcesNodeImport()
```

...

NumPyRasterConversions.cpp imports NumPy, probably the place to start looking:

```cpp
#define PY_ARRAY_UNIQUE_SYMBOL narray_api
#include <numpy/arrayobject.h>
```
