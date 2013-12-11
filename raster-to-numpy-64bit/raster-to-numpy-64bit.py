import arcpy
import os
import sys
import platform

# Before going any further, insure that we're running in 64-bit mode (MUST be
# either in background process, or directly run from the Python interpreter 
# bundled with Background Processing).
bits = platform.architecture()[0]
if bits == '64bit':
    print "64-bit Python detected, continuing. Machine must have 4GB+ of " + \
    "memory available for this task to run successfully."
else:
    print "{} Python detected, ABORTING. Must be run in a 64-bit Python environment.".format(bits)
    sys.exit(1) 

arcpy.CheckOutExtension("Spatial")

# make sure output directory exists

workspace_dir = 'C:/workspace'
gdb_name = 'big_raster.gdb'

if not os.path.exists(workspace_dir):
    os.mkdir(workspace_dir)

gdb_path = os.path.join(workspace_dir, gdb_name)
if not os.path.exists(gdb_path):
    arcpy.CreateFileGDB_management(workspace_dir, gdb_name)
else:
    print "skipping creation of GDB, already exists"

# create initial normal rasters of varying sizes
big_raster = os.path.join(gdb_path, "big_raster")
big_plus_raster = os.path.join(gdb_path, "bigp_raster")

arcpy.env.overwriteOutput = True

"""
print "creating big raster...",
r1 = arcpy.sa.CreateNormalRaster(1, arcpy.Extent(0, 0, 20000, 21474))
print "saving raster to disk...",
r1.save(big_raster)
"""
computed_size = 20000*21474
print "loading big raster ({} elements; {} bytes) into memory".format(computed_size, computed_size*32)
big_numpy_array = arcpy.RasterToNumPyArray(big_raster) # peak: 1.6Gb; 3.6 VS
print "loaded big raster, size: {}, data type: {}".format(big_numpy_array.size, big_numpy_array.dtype)
del big_numpy_array

# 4,294,967,296 == 4GB is the limit.
"""
print "creating big+1 raster...",
r2 = arcpy.sa.CreateNormalRaster(1, arcpy.Extent(0, 0, 25000, 21475))
print "saving raster to disk...",
r2.save(big_plus_raster)
print " done."
"""
computed_size = 20000*21475
print "loading big+1 raster ({} elements; {} bytes) into memory".format(computed_size, computed_size*32)
# THIS NEXT COMMAND WILL CRASH
big_plus_numpy_array = arcpy.RasterToNumPyArray(big_plus_raster) # peak: 1.6Gb; 3.6 VS
print "loaded big+1 raster, size: {}, data type: {}".format(big_plus_numpy_array.size, big_plus_numpy_array.dtype)


"""
Now, I get a big beautiful crash:
"Unhandled exception at 0x71c1e630 (msvcr90.dll) in python.exe: 0xC0000005: Access violation writing location 0x0000000115030000."

Digging deeper in Visual Studio, I can trace the exception back to RasterDB.dll, but no further -- I'm unable to download Symbols for the 64-bit versions of the libraries used, and the stack frame reports 'No Symbols for RasterDB.dll'.
"""
