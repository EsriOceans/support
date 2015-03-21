import os
import platform

# confirm we're on 64-bit
print platform.architecture()

import arcpy
import rtree

sde_path = os.path.join(os.path.dirname(__file__), 'sde_conn.sde')
arcpy.env.workspace = sde_path

print arcpy.ListFeatureClasses()
sys.exit()

sde_conn = arcpy.ArcSDESQLExecute(sde_path)

sql_server_version = sde_conn.execute("select @@version")
print sql_server_version
"""
Microsoft SQL Server 2008 (SP3) - 10.0.5500.0 (Intel X86)
        Sep 22 2011 00:28:06
        Copyright (c) 1988-2008 Microsoft Corporation
        Enterprise Edition on Windows NT 6.0 <X86> (Build 6002: Service Pack 2) (VM)
"""

tables = sde_conn.execute("select name from sysobjects where xtype = 'U';")
print tables[0]
"""
[u's44559']
"""
