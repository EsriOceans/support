#!/usr/bin/env python
# cpc_to_raster.py: Read a CPC CONUS binary file and create a raster
# Author: Shaun Walbridge
# License: Apache 2
# Credits: The raincpc R module handles the same dataset, used it to 
#          validate the generated output

import ftplib
import numpy as np
import os
import sys

host = 'ftp.cpc.ncep.noaa.gov'

# NOTE format below only correct for 2009+, earlier data uses
#      slightly different formats for its URLs
resource = {
    'path':  'precip/CPC_UNI_PRCP/GAUGE_CONUS/RT',
    'file': 'PRCP_CU_GAUGE_V1.0CONUS_0.25deg.lnx',
    'ext': 'RT',
    'year': 2015,
    'month': 9,
    'day': 7,
}

cpc_ftp = ftplib.FTP(host)
cpc_ftp.login()

filename = '{file}.{year}{month:02d}{day:02d}.{ext}'.format(**resource)
url = '{path}/{year}/{filename}'.format(path=resource['path'], year=resource['year'], filename=filename)

# some fixed properties of the CONUS data
dims = {
    'rows': 120,
    'cols': 300,
    'llx': 230.125 - 360, # lower left longitude, converted from 0-360 to -180-180
    'lly': 30.125, # lower left latitude
    'res': 0.25, # quarter degree resolution
    'nodata': -999.0,
}

if os.path.exists(filename):
    # poor man's checksumming, check against size of file on server
    size_on_disk = os.path.getsize(filename) 
    size_on_ftp = cpc_ftp.size(url)
    if size_on_disk != size_on_ftp:
        print("Failure: data download mismatch: {} instead of {} bytes".format(
            size_on_dis, size_on_ftp))
        sys.exit()

    # dims * two fields * four bytes per field
    size_expected = dims['rows'] * dims['cols'] * 2 * 4
    if size_on_disk != size_expected:
        print("Failure: size on disk doesn't match expected format.")
        sys.exit()
else:
    # only read in the data if we don't have it already on disk
    with open(filename, 'wb') as data_f:
        cpc_ftp.retrbinary('RETR {}'.format(url), lambda x: data_f.write(x))

res = np.fromfile(file=filename, dtype=np.float32)

shape = (dims['rows'], dims['cols'])

# really two datasets, one after the other: precip, then num gauges
datasets = {
    'precip': res[:len(res)/2].reshape(shape), # precip in tenths of a mm
    'gauges': res[len(res)/2:].reshape(shape), # number of gauges
}

# at this point, we could do what we will with the NumPy arrays, but will
# write them out instead.

try:
    import arcpy
    arcpy.env.overwriteOutput = True
    output_sr = arcpy.SpatialReference(4326)
    has_arcpy = True
except ImportError:
    has_arcpy = False

for (label, dataset) in datasets.items():
    if has_arcpy:
        llc_coord = arcpy.Point(dims['llx'], dims['lly'])
        
        output_raster = arcpy.NumPyArrayToRaster(
            in_array=dataset, lower_left_corner=llc_coord,
            x_cell_size=dims['res'], y_cell_size=dims['res'],
            value_to_nodata=dims['nodata'])

        output_name = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                "{}.tif".format(label))
        print("Saving to {}".format(output_name))
        # this is a hack, could be fixed in the NumPy array. Necessary because the 
        # data is stored in upper-left-corner to lower-right corner (rows inverted)
        arcpy.Flip_management(output_raster, output_name)

        # NumPy array to raster doesn't honor output spatial reference, set manually
        arcpy.DefineProjection_management(output_name, output_sr)
    else:
        print("ArcPy not found, stopping.")
        # TODO generate ASCII grid
