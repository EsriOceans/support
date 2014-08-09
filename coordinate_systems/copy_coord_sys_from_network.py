import arcpy
import os
import shutil

def copy_directory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

# input network path
network_path = r'\\myserver\share\CoordinateSystems'

# default application data dir; e.g. c:\Users\scw\AppData\Roaming
app_data_path = os.getenv('APPDATA')

# get current ArcGIS version
arc_version = arcpy.GetInstallInfo()['Version']

# change this path if you'd like the spatial references to be written 
# out elsewhere, this is the default directory for .prj files.
output_base = '{0}\\ESRI\\Desktop{1}\\ArcMap\\Coordinate Systems'.format(app_data_path, arc_version)

coordinate_dest = os.path.join(output_base, 'From Network')

copy_directory(network_path, coordinate_dest)
