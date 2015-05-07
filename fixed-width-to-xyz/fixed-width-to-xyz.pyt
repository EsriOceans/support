def parse_line(line, length):
    column_pos = range(0, length, 10)
    return [line[i:i+10].strip() for i in column_pos]


class Toolbox(object):
    def __init__(self):
        self.label = 'fw2xyz'
        self.alias = ''
        self.tools = [fw2xyz]

class fw2xyz(object):
    """ Convert a fixed width ASCII file to an XYZ file."""
    def __init__(self):
        self.label = "fixed width to XYZ"
        self.canRunInBackground = True

    def getParameterInfo(self):
        input_text = arcpy.Parameter()
        input_text.name = u'Input Text File'
        input_text.displayName = u'Input Text File'
        input_text.parameterType = 'Required'
        input_text.direction = 'Input'
        input_text.datatype = 'DEFile'

        output_text = arcpy.Parameter()
        output_text.name = u'Output Text File'
        output_text.displayName = u'Output Text File'
        output_text.parameterType = 'Required'
        output_text.direction = 'Output'
        output_text.datatype = 'DEFile'

        return [input_text, output_text]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):

        input_file = parameters[0].valueAsText
        output_file = parameters[1].valueAsText

        with open(input_file, 'r') as f:
            with open(output_file, 'w') as out_f:
                header = f.readline().strip()
                header_len = len(header)
                column_pos = range(0, len(header), 10)
                longitudes = parse_line(header, header_len)
                out_f.write("longitude,latitude,value\n")

                for line in f:
                    row = parse_line(line, header_len)
                    latitude = row[0]
                    for (i, col) in enumerate(row[1:]):
                        if col != 'NaN':
                            line = ",".join([longitudes[i], latitude, col]) + "\n"
                            out_f.write(line)
