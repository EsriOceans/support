# -*- coding: utf-8 -*-
import arcpy
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
#script_dir = r'Z:\projects\support\pyt-import'

"""
# these will work
#
module = arcpy.ImportToolbox(os.path.join(script_dir, "test.pyt"))

input_str = u'Hello World!'

arcpy.Test_touche(input_str)
arcpy.touche.Test(input_str)
"""

# these don't
#
module = arcpy.ImportToolbox(os.path.join(script_dir, "test.pyt"), 'foo')

# this will fail
module.Test(input_str)

# as will this
arcpy.Test_foo(input_str)
