import arcpy
import os

# minor refactor of issue reported by steveoh here:
#  https://gist.github.com/steveoh/02a1896b5af4632ebed9

"""
Note: this issue is now logged as NIM103815: Data Access cursors should 
return the names of invalid columns in addition to the RuntimeError that results 
from creating a cursor object with field names that do not exist in the source table.
"""
arcpy.env.overwriteOutput = True

test_location = 'c:\\temp'
gdb_name = 'inspecific_error'
gdb_path = os.path.join(test_location, gdb_name) + '.gdb'
table_name = 'tell_me_the_column_name'
table_path = os.path.join(gdb_path, table_name)
fouled_up_fields = ['test', 'this_one']

if not os.path.exists(test_location):
    os.makedirs(test_location)

arcpy.CreateFileGDB_management(test_location, gdb_name, 'CURRENT')

arcpy.CreateTable_management(gdb_path, table_name)

arcpy.AddField_management(table_path, 'test', 'TEXT')

try:
    with arcpy.da.SearchCursor(table_path, fouled_up_fields) as cursor:
        for row in cursor:
            continue
except RuntimeError as e:
    print("We've now hit a runtime error, due to the missing column " + \
            "`this_one`, but we don't actually bubble up what the missing " + \
            " is named.")
    print(e)

# These steps are necessary to figure out which column(s) are missing
#

#: the fields in the feature class
actual = set([str(x.name) for x in arcpy.ListFields(table_path)])

#: the fields you are trying to use
my_silly_input = set(fouled_up_fields)

missing = my_silly_input - actual

print('the fouled up columns are {}'.format(missing))
