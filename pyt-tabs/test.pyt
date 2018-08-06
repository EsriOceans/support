# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import arcpy

def message(text):
    print(text)
    arcpy.AddMessage(text)


class Toolbox(object):
    def __init__(self):
        self.label = 'Tabs'
        self.alias = 'tabs' # "touché"
        self.tools = [Test]


class Test(object):

    def __init__(self):
        self.label = "Test Messages"
        self.description = "Test message output"
        self.canRunInBackground = False

    def getParameterInfo(self):
        return []

    def execute(self, parameters, messages):
        arcpy.AddMessage("\t\t\tThe IBM-1401 was used to generate a list of 185,000 four letter words with one vowel, leading to Tabb, later shortened to Tab. No relation to the tabulator key, 0x09.") 
        arcpy.AddMessage("    four spaces")
        arcpy.AddMessage("Tabs after the inital character are respected:\t\tSee?")
        arcpy.AddMessage("next up, a newline:\n\tI should be on the following line and indented")

        arcpy.GetMessages()
