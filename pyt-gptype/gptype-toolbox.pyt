import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = u'Example_Toolbox'
        self.alias = ''
        self.tools = [FirstTool]


class FirstTool(object):

    def __init__(self):
        self.label = u'First Tool'
        self.description = u''
        self.canRunInBackground = False

    def getParameterInfo(self):
        in_table = arcpy.Parameter(
            name="in_table",
            displayName="Input Table",
            datatype="GPValueTable",
            direction="Input",
            parameterType="Required")

        in_table.columns = [['Feature Layer', 'Features'], ['Long', 'Count'], ['Any Value', 'Ranks']]
        return [in_table]

    def execute(self, parameters, messages):
        pass

