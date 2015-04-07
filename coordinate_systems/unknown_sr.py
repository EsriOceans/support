

"""
Related GeoNet question:
  https://geonet.esri.com/thread/75682


From bin/XMLSupport.dat:

<Type>
    <Name>ProjectedCoordinateSystem</Name>
    <Namespace>http://www.esri.com/schemas/ArcGIS/10.3</Namespace>
    <CLSID>{2a626700-1dd2-11b2-bf51-08002022f573}</CLSID>
</Type>
"""

# This works at 10.1+:
unknown_sr = arcpy.SpatialReference()
unknown_sr.loadFromString('{B286C06B-0879-11D2-AACA-00C04FA33C20}')

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

df.spatialRefernce = unknown_sr
