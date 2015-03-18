import datetime
import os


local_path = os.path.abspath(os.path.dirname(__file__))

target = os.path.join(local_path, "Export.gdb")

now = datetime.datetime.now();
print now;
import arcpy;
print "Import ArcPy: " + str(datetime.datetime.now() - now);
arcpy.env.overwriteOutput = True;

home = os.path.join(local_path, "HH_GrowthNC.xlsx")

now = datetime.datetime.now();
arcpy.ExcelToTable_conversion(home, target + "/NC_G_ETTPy1", "HH Growth Map_G");
print "NC_G_ETTPy1: " + str(datetime.datetime.now() - now);

home = os.path.join(local_path, "HH_GrowthUSA.xlsx")

now = datetime.datetime.now();
arcpy.ExcelToTable_conversion(home, target + "/USA_G_ETTPy1", "HH Growth Map_G");
"USA_G_ETTPy1: " + str(datetime.datetime.now() - now);
