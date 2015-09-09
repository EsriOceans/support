# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import arcpy


class Toolbox(object):
    def __init__(self):
        self.label = 'Touche'
        self.alias = u"touche" # u"touché"
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

        return [param_1]

    def execute(self, parameters, messages):
        arcpy.AddMessage(parameters[0].valueAsText)
