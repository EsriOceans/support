import json
import jsonpickle
import requests
import arcpy
import numpy as np    #NOTE THIS
import random
import timestring
import datetime



fc = "C:\MYLATesting.gdb\MYLA311Copy"
if arcpy.Exists(fc):
  arcpy.Delete_management(fc)




f2 = open('C:\Users\Administrator\Desktop\DetailView.json', 'r')
data2 = jsonpickle.encode( jsonpickle.decode(f2.read()) )

url2 = "https://myla311.lacity.org/myla311router/mylasrbe/1/QuerySR"
headers2 = {'Content-type': 'text/plain', 'Accept': '/'}



r2 = requests.post(url2, data=data2, headers=headers2)
decoded2 = json.loads(r2.text)

Start = datetime.datetime.now()
print Start


items = []
for sr in decoded2['Response']['ListOfServiceRequest']['ServiceRequest']:
    SRAddress = sr['SRAddress']
    Latitude = sr['Latitude']
    Longitude = sr['Longitude']
    SRNumber = sr['SRNumber']
    FirstName = sr['FirstName']
    LastName = sr['LastName']
    HomePhone = sr['HomePhone']
    CreatedDate = sr['CreatedDate']
    CreatedDate = datetime.datetime.strptime(CreatedDate, "%m/%d/%Y %H:%M:%S")


    ItemInfo = " "

    for ew in sr["ListOfLa311ElectronicWaste"][u"La311ElectronicWaste"]:
            CommodityType = ew['Type']
            ItemType = ew['ElectronicWestType']
            ItemCount = ew['ItemCount']
            ItemInfo += '{0},  {1}, '.format(ItemType, ItemCount)
            ParentNumber = ew['Name']




    for GIS in sr["ListOfLa311GisLayer"][u"La311GisLayer"]:
            Day = GIS['Day']
            DistrictName = GIS['DistrictName']
            ShortDay = GIS['ShortDay']
            A_Call_No = GIS['A_Call_No']
            Area = GIS['Area']
            DirectionSuffix = GIS['DirectionSuffix']
            DistrictAbbr = GIS['DistrictAbbr']
            DistrictNumber = GIS['DistrictNumber']
            DistrictOffice = GIS['DistrictOffice']
            Fraction = GIS['Fraction']
            R_Call_No = GIS['R_Call_No']
            SectionId = GIS['SectionId']
            StreetFrom = GIS ['StreetFrom']
            StreetTo = GIS ['StreetTo']
            StreetLightId = GIS ['StreetLightId']
            StreetLightStatus = GIS['StreetLightStatus']
            Y_Call_No = GIS ['Y_Call_No']
            CommunityPlanningArea = GIS['CommunityPlanningArea']
            LastUpdatedBy = GIS['LastUpdatedBy']
            BOSRadioHolderName = GIS['BOSRadioHolderName']


    comments = [ cl['Comment'] for cl in sr["ListOfLa311ServiceRequestNotes"][u"La311ServiceRequestNotes"]]
    Comment = ' '.join(comments)

dt = np.dtype([('SRAddress', 'U40'),
                ('LatitudeShape', '<f8'),
                ('LongitudeShape', '<f8'),
                ('Latitude', '<f8'),
                ('Longitude', '<f8'),
                ('Type', 'U40'),
                ('SRNumber', 'U40'),
                ('FirstName', 'U40'),
               ('LastName', 'U40'),
               ('HomePhone', 'U40'),
                ('CreatedDate', 'U128'),
               ('Comment', 'U128'),
                ('ItemInfo', 'U128'),
                ('DayTest', 'U128'),
                ('DistrictName', 'U128'),
                ('ShortDay', 'U128'),
                ('ParentNumber', 'U128'),
                ('A_Call_No','U128'),
                ('Area', 'U128'),
                ('DirectionSuffix','U128'),
                ('DistrictAbbr', 'U128'),
                ('DistrictNumber', 'U128'),
                ('DistrictOffice', 'U128'),
                ('Fraction', 'U128'),
                ('R_Call_No', 'U128'),
                ('SectionId', 'U128'),
                ('StreetTo', 'U128'),
                ('StreetFrom', 'U128'),
                ('StreetLightId', 'U128'),
                ('StreetLightStatus', 'U128'),
                ('Y_Call_No', 'U128'),
                ('CommunityPlanningArea', 'U128'),
                ('LastUpdatedBy', 'U128'),
                ('BOSRadioHolderName', 'U128'),
                ])


items.append((SRAddress,
                          Latitude,
                         Longitude,
                          Latitude,
                          Longitude,
                          CommodityType,
                          SRNumber,
                         FirstName,
                          LastName,
                          HomePhone,
                          CreatedDate,
                          Comment,
                          ItemInfo,
                          Day,
                          DistrictName,
                          ShortDay,
                          ParentNumber,
                         A_Call_No,
                        Area,
                        DirectionSuffix,
                        DistrictAbbr,
                        DistrictNumber,
                        DistrictOffice,
                        Fraction,
                        R_Call_No,
                        SectionId,
                        StreetFrom,
                        StreetTo,
                        StreetLightId,
                        StreetLightStatus,
                        Y_Call_No,
                        CommunityPlanningArea,
                        LastUpdatedBy,
                        BOSRadioHolderName
))


arr = np.array(items,dtype=dt)
sr = arcpy.SpatialReference(4326)

print arr

arcpy.da.NumPyArrayToFeatureClass(arr, fc, ['longitudeshape', 'latitudeshape'], sr )

arcpy.AddField_management(fc, "ArcPyDate", "DATE", '', 255)

field1 = "ArcPyDate"


cursor = arcpy.UpdateCursor(fc)
for row in cursor:
    row.setValue(field1, row.getValue("CreatedDate"))
    cursor.updateRow(row)


# print json.dumps(decoded2, sort_keys=True, indent=4)
