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
            print(row)
            luminaireType = row[1][0]
            ledDesigned = row[0]
            concatenatedProperties = luminaireType + " --- " + ledDesigned
            uniques[concatenatedProperties] = True
            # arcpy.CalculateField_management(InputFeatureClass, "InstlCode", "\"" + luminaireType +"\"", "PYTHON")
            # This writes into the InstlCode column:
            subsetQuery = u"LuminaireType LIKE " + row[1] + u" AND LEDDesigned LIKE " + row[0]
            print(subsetQuery)
            arcpy.CalculateField_management(subsetQuery, field3, "\"" + luminaireType + "\"", "PYTHON")


print(uniques)


{
    u'D --- 81W_ATBM C MVOLT R2 3K MP NL P7': True,
    u'C --- 60W_ATBS H MVOLT R2 3K MP NL P7': True,
    u'D --- 31W_ATBS C MVOLT R2 3K MP NL P7': True,
    u'C --- 81W_ATBM C MVOLT R2 3K MP NL P7': True,
    u'C --- 24W_ATBS B MVOLT R2 3K MP NL P7': True,
    u'C --- 60W_ATBS H MVOLT R3 3K MP NL P7': True,
    u'C --- 40W_ATBS E MVOLT R3 3K MP NL P7': True
}

subsetQuery = "LEDDesigned LIKE '" + row[0] + "' AND LuminaireType LIKE '" + row[1] + '"

# query2 = "LEDDesigned LIKE '40W_ATBS E MVOLT R3 3K MP NL P7'"
# select2 = arcpy.SelectLayerByAttribute_management(InputFeatureClass, "SUBSET_SELECTION", query2)
# arcpy.CalculateField_management (select2, "InstlCode", "\"C2\"", "PYTHON")


# This is the row variable found in loop:
# (u'24W_ATBS B MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'24W_ATBS B MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'24W_ATBS B MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'24W_ATBS B MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'81W_ATBM C MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Other')
# This is the row variable found in loop:
# (u'81W_ATBM C MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'No replacement', u'Sentinel')
# This is the row variable found in loop:
# (u'No replacement', u'Sentinel')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'81W_ATBM C MVOLT R2 3K MP NL P7', u'Decorative - Acorn')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R2 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'40W_ATBS E MVOLT R3 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'40W_ATBS E MVOLT R3 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R3 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R3 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R3 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Other')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Other')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Other')
# This is the row variable found in loop:
# (u'31W_ATBS C MVOLT R2 3K MP NL P7', u'Decorative - Other')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R3 3K MP NL P7', u'Cobrahead')
# This is the row variable found in loop:
# (u'60W_ATBS H MVOLT R3 3K MP NL P7', u'Cobrahead')

