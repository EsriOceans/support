import arcpy

input_coord = arcpy.Point(51.028, 13.746) # Dresden, DE
point = arcpy.PointGeometry(input_coord, '4326')

with open (r'C:\temp\projected.txt', 'w') as f:
    for sr_name in arcpy.ListSpatialReferences("*", "PCS"):
        # create an sr from the name
        sr = arcpy.SpatialReference(sr_name)
        print("On {}".format(sr.factoryCode), end="...")
        try:
            projected_point = point.projectAs(sr)
            coord = projected_point.firstPoint
            if projected_point:
                f.write("{}\n".format(projected_point.JSON))
        except RuntimeError as e:
            print("Unable to reproject point to {}".format(sr))


"""
Note: this would be nice to trap this error a little better, currently creates:
    RuntimeError: Object: CreateObject error creating spatial reference
this happens when passing a STRING from ListSpatialReferences() to projectAs(),
which really asks for a SR object but will try to make due with a string. 
About 1/2 of the strings do work, the other half fail.


A second problem: many of the projected points end up with 'NaN' values for their
output coordinates. This probably means that the output coordinates are invalid 
given the input coordinate space -- e.g. the point is out of the valid bounds. If possible,
it'd be great to show this as the error, and not just return NULL coordinates. PE does know
when the coordinates are invalid, based on the spatial filtering available in ArcMap / Pro.
"""
