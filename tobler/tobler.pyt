import arcpy
import os

class Toolbox(object):
    def __init__(self):
        self.label = u'Path Distance'
        self.alias = ''
        self.tools = [PathD]


class PathD(object):

    def __init__(self):
        self.label = u'Path Distance'
        self.description = u''
        self.canRunInBackground = False

    def getParameterInfo(self):
        in_file = arcpy.Parameter(
            name="in_file",
            displayName="Input File",
            datatype="DEFile",
            direction="Input",
            parameterType="Required")

        return [in_file]

    def execute(self, parameters, messages):
        # note that we need to get the _text_ value back from the object
        tobler_file = parameters[0].valueAsText

        vertical_factor = arcpy.sa.VfTable(tobler_file)

        # pull in local data, these could be parameters.
        data_path = os.path.join(os.path.dirname(__file__), "data")

        cost_raster = os.path.join(data_path, "land.tif")
        fc_input = os.path.join(data_path, "sources.shp")

        out_path_dist = arcpy.sa.PathDistance(
            fc_input, cost_raster, "", "", "", "", vertical_factor)

        out_path_dist.save(r"C:/workspace/my_cost_rast.tif")
