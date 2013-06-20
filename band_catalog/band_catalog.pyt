import arcpy
import os

class Toolbox(object):
    def __init__(self):
        self.label = u'Display Raster Attributes'
        self.alias = ''
        self.tools = [BandCatalog]

class BandCatalog(object):

    def __init__(self):
        self.label = u'Raster Band Catalog'
        self.description = u''
        self.canRunInBackground = False

    def getParameterInfo(self):
        input_folder = arcpy.Parameter(
            displayName='Input Folder',
            name='input_folder',
            datatype='DEFolder',
            parameterType='Required',
            direction='Input')

        output_csv = arcpy.Parameter(
            displayName='Output CSV',
            name='output_csv',
            datatype='File',
            parameterType='Required',
            direction='Output')
 
        return [input_folder, output_csv]

    def execute(self, parameters, messages):
        input_folder = parameters[0].valueAsText
        output_csv = parameters[1].valueAsText

        with open(output_csv, 'wb') as csv:
            csv.write("Path,Name,Data Type,Pixel Type,Cell Height,Cell Width,Height,Width\n")
            for dirpath, dirnames, filenames in \
                    arcpy.da.Walk(input_folder, datatype='RasterBand'):
                for fn in filenames:
                   desc = arcpy.Describe(os.path.join(dirpath, fn))
                   row = [desc.catalogPath, desc.name, desc.dataType, 
                         desc.pixelType, desc.meanCellHeight, 
                         desc.meanCellWidth, desc.height, desc.width]
                   csv.write(",".join(['"' + str(r) + '"' for r in row]) + "\n")
        arcpy.AddMessage("Output results to {}".format(output_csv))
        return
