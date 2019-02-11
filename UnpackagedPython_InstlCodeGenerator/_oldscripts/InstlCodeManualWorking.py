#Cobras
InputFeatureClass = "Cityname_SP_YYYYMMDD"
cobraQuery = "LuminaireType LIKE 'Cobra%'"
select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", cobraQuery)
query2 = "LEDDesigned LIKE '24W_ATBS B MVOLT R2 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"C1\"", "PYTHON")
print("Done")

select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", cobraQuery)
query2 = "LEDDesigned LIKE '40W_ATBS E MVOLT R3 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"C2\"", "PYTHON")
print("Done")

select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", cobraQuery)
query2 = "LEDDesigned LIKE '60W_ATBS H MVOLT R2 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"C3\"", "PYTHON")
print("Done")

select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", cobraQuery)
query2 = "LEDDesigned LIKE '60W_ATBS H MVOLT R3 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"C4\"", "PYTHON")
print("Done")

select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", cobraQuery)
query2 = "LEDDesigned LIKE '81W_ATBM C MVOLT R2 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"C5\"", "PYTHON")
print("Done")

#Decos
InputFeatureClass = "Cityname_SP_YYYYMMDD"
query = "LuminaireType LIKE 'Deco%'"
select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", query)
query2 = "LEDDesigned LIKE '31W_ATBS C MVOLT R2 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"D1\"", "PYTHON")
print("Done")

query = "LuminaireType LIKE 'Deco%'"
select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", query)
query2 = "LEDDesigned LIKE '81W_ATBM C MVOLT R2 3K MP NL P7'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"D2\"", "PYTHON")
print("Done")



#Sentis
InputFeatureClass = "Cityname_SP_YYYYMMDD"
sentiQuery = "LuminaireType LIKE '[Senti]%'"
select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", sentiQuery)
query2 = "LEDDesigned LIKE '25W_GCJ0-15H-MV-NW-2R-GY-490-PCR7-CR-WL'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"S1\"", "PYTHON")
print("Done")

#Floods
InputFeatureClass = "Cityname_SP_YYYYMMDD"
query = "LuminaireType LIKE '[Flood]%'"
select1 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "NEW_SELECTION", query)
query2 = "LEDDesigned LIKE '119W_ACP0LED-PK3-MVOLT-WFL-40K-YK-BZSDP-10KVMP-PER7-60-23-NL'"
select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
arcpy.CalculateField_management (select2, "InstlCode", "\"F1\"", "PYTHON")
print("Done")