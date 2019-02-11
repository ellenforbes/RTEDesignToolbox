InputFeatureClass = "Cityname_SP_YYYYMMDD"
field = "LEDDesigned"
field2 = "LuminaireType"
field3 = "InstlCode"

uniques = {}

with arcpy.da.UpdateCursor(InputFeatureClass, [field, field2, field3]) as cursor:
   for row in cursor:
        print("This is the row variable found in loop: ")

        # Exclude fields where it says "No replacement" from our logic
        if row[0].lower() != u'no replacement':
            luminaireType = row[1][0]
            ledDesigned = row[0]
            concatenatedProperties = luminaireType + " --- " + ledDesigned
            uniques[concatenatedProperties] = "UniqueValue"
            row[2] = luminaireType
            cursor.updateRow(row)

print(uniques)