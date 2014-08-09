import arcpy
import re

# a projection with a latitude of origin property
proj = 'NAD 1983 Contiguous USA Albers'

sr = arcpy.SpatialReference(proj)

lat_of_origin_regex = "Latitude_Of_Origin',(\d+\.?\d*)]"
match = re.search(lat_of_origin_regex, sr.exportToString())
if match:
   lat_of_origin = float(match.groups()[0])
   print "{0} has latitude of origin {1}".format(proj, lat_of_origin)
else:
   print "no latitude of origin detected."
