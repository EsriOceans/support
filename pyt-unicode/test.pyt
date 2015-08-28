# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import arcpy


class Toolbox(object):
    def __init__(self):
        self.label = 'Test'
        self.alias = ''
        self.tools = [Test]


class Test(object):

    def __init__(self):
        self.label = "Test"
        self.description = "test"
        self.canRunInBackground = False

    def getParameterInfo(self):
        param_1 = arcpy.Parameter()
        param_1.name = 'unicode string'
        param_1.displayName = 'Unicode String'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = 'String'
        param_1.value = "票西表島構内評豹掛川日本迎票府怖扶敷".encode(
            "cp1252", "replace").decode("utf-8", "ignore")

        return [param_1]

    def execute(self, parameters, messages):

        strings = [
            "as param: {}".format(parameters[0].valueAsText),
            "as string: 票西表島構内評豹掛川日本迎票府怖扶敷".encode("windows-1252", "replace"),
            'helló wörld'.encode("windows-1252"),
            "touché, un café".encode("windows-1252"),
        ]

        for entry in strings:
            try:
                u_e = entry.decode("utf-8", "ignore")
            except:
                u_e = entry
            arcpy.AddMessage(u_e)
