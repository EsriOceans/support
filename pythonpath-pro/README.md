Current state: tried recreating this issue by installing 1.1 final on a machine that also has 10.4, no luck in reproducing the crash. Kicking back to users to see if they can provide details.

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
