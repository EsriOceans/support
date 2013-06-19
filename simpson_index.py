# simpson-index.py: Calculate the simpson indicies
#                   from a classified raster dataset.
# shaun walbridge 2013.06.18

r"""
Compute diversity indicies from a classified input raster. Computes:

Simpson's Index
.. math::
  \lambda = \sum_{i=1}^R p_i^2
 
where 
  p_i = proportion of each class
  R = number of classes

Simpson's Diversity Index
.. math::
  1 - \lambda

# Simpson's Reciprocal index
.. math::
  \frac{1}{lambda}

"""

import arcpy
import os
import sys

# requires Spatial Analyst extension to run.
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
else:
    print "unable to check out spatial analyst"
    sys.exit()

arcpy.env.workspace = "e:\\workspace\\btm"
raster_input = "zomg_classes"
raster_index = "simp_index"
raster_diversity = "simp_div"
raster_recip = "simp_recip"
raster_variety = "variety"

# set up our window. Here, just using a 9x9 square neighborhood.
neighborhood = arcpy.sa.NbrRectangle(9)

# other settings
arcpy.env.overwriteOutput = True

# import our classified raster
r = arcpy.Raster(raster_input)

# This step is only necessary if you don't know what the values are in your
# raster beforehand, to figure out what distinct classes are in the raster.
# Otherwise, just set the raster_values list directly.
raster_values = []
if r.hasRAT:
    # get the current raster attribute table list
    table = "raster_table_view"
    arcpy.MakeTableView_management(r, table)
    with arcpy.da.SearchCursor(table, 'VALUE') as cur:
        for row in cur:
            raster_values.append(row[0])
else:
    if r.isInteger:
        # assume we have a range from min to max of the classified raster
        raster_values = range(int(r.minimum), int(r.maximum) + 1)
    else:
        print "Unable to work with raster of type {}".format(r.pixelType)
        sys.exit()

# First, we want to calculate the variety, or number of distinct types seen
# within each neighborhood.
print "Computing variety...",
variety = arcpy.sa.FocalStatistics(r, neighborhood, 'VARIETY')
variety.save(raster_variety)
print "wrote to {}".format(os.path.join(arcpy.env.workspace, raster_variety))

# Now, we want to know how many cells of each type are within our neighborhood.
# Iterate over each type identified earlier, and compute the count of that
# type within the neighborhood. Store a dictionary which maps each class
# to a raster containing its count by neighborhood.
raster_counts = dict.fromkeys(raster_values)
sum_table = []
print "Computing statistics for:"
for value in raster_values:
    print "{}".format(value),
    # extract only the cells which have this value, set them to '1'
    raster_con = arcpy.sa.Con(r, 1, 0, "VALUE = {}".format(value))

    # sum the value, this is our count for this class.
    sum_count = arcpy.sa.FocalStatistics(raster_con, neighborhood, 'SUM')

    raster_counts[value] = sum_count
    sum_table.append([sum_count, "VALUE", 1])

print "\nSumming all raster counts per cell"
# Compute the sum of all values found in the neighborhood, from this we can 
# compute the proportion of each neighborhood covered by this type:
# ..math:: n_{all} = \sum_{i=1}^R n_i
n_all = arcpy.sa.WeightedSum(arcpy.sa.WSTable(sum_table))

p_sq_table = []
print "Computing proportions for:"
for value in raster_values: 
    print "{}".format(value),
    n_i = raster_counts[value]
    p_i = arcpy.sa.Divide(n_i, n_all)
    # square the result, we need to sum all
    # ..math:: p_i^2
    p_i_sq = arcpy.sa.Square(p_i)
    p_sq_table.append([p_i_sq, "VALUE", 1])

# Now, compute the indices:
print "\nComputing diversity index"
simpson_index = arcpy.sa.WeightedSum(arcpy.sa.WSTable(p_sq_table))
print "Wrote Simpson's Index to {}".format( \
        os.path.join(arcpy.env.workspace, raster_index))
simpson_index.save(raster_index)

simpson_diversity = 1 - simpson_index
print "Wrote Simpson's Index of Diversity (1 - D) to {}".format( \
        os.path.join(arcpy.env.workspace, raster_diversity))
simpson_diversity.save(raster_diversity)

print "Wrote Simpson's Reciprocal Index (1 / D) to {}".format( \
        os.path.join(arcpy.env.workspace, raster_recip))
simpson_recip = arcpy.sa.Divide(1, raster_index)
simpson_recip.save(raster_recip)
