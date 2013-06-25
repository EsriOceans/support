# arcpy.da.Walk example #2 as included in 10.1 help

import arcpy
import os
workspace = "e:/workspace"
rasters = []
for dirpath, dirnames, filenames in arcpy.da.Walk(workspace,
                                                  topdown=True,
                                                  datatype="Raster"):
    # Disregard any folder named 'back_up' in creating list 
    #  of rasters
    if "back_up" in dirnames:
        dirnames.remove('back_up')
    for filename in filenames:
        rasters.append(os.path.join(dirpath, filename))

