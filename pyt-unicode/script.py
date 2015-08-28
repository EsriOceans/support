# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import arcpy

strings = [
    "as param: {}".format(arcpy.GetParameterAsText(0)),
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
