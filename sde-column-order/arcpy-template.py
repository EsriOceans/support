import arcpy
import os
 
test_location = 'c:\\temp'
 
gdb_name = 'copy'
gdb_path = os.path.join(test_location, gdb_name) + '.gdb'
 
fc_name = 'template_fc'
fc_path = os.path.join(gdb_path, fc_name)
 
original_fc_path = ('...\\AppData\\Roaming\\ESRI\\'
                    'Desktop10.2\\ArcCatalog\\Something.sde'
                    '\\template_fc')
 
if not os.path.exists(test_location):
    os.makedirs(test_location)
 
if not os.path.exists(gdb_path):
    arcpy.CreateFileGDB_management(test_location, gdb_name, 'CURRENT')
 
arcpy.CreateFeatureclass_management(gdb_path,
                                    fc_name,
                                    'POINT',
                                    template=original_fc_path)
 
original = map(lambda field: field.name, arcpy.Describe(original_fc_path).fields)
copy = map(lambda field: field.name, arcpy.Describe(fc_path).fields)
 
order = zip(copy, original)
 
for pair in order:
    if pair[0] == pair[1]:
        continue
 
    print 'these really should match {}'.format(str(pair))
 
print 'done'
