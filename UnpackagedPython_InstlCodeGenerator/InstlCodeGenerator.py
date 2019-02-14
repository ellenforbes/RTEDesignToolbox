import re, arcpy

InputFeatureClass = "Cityname_SP_YYYYMMDD"
field = "LuminaireType"
field2 = "LEDDesigned"
field3 = "InstlCode"


# Copied from stackoverflow: https://stackoverflow.com/a/5967539/7216271
# Apparently sorting strings with numbers inside gives ugly issues.
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)W', text) ]

instlCodeMap = {}

# Create the instlCodeMap
with arcpy.da.UpdateCursor(InputFeatureClass, [field, field2, field3]) as cursor:
    for row in cursor:
        luminaireType = row[0][0].upper()
        ledDesigned = row[1].upper()
        # Exclude fields where it says "No replacement" from our logic
        if ledDesigned != u'NO REPLACEMENT':
            # Step 1: If luminaireType is new, add it to the map of instlCodes
            # and push the ledDesigned value onto this new list of luminaireTypes
            if luminaireType not in instlCodeMap:
                instlCodeMap[luminaireType] = []
                instlCodeMap[luminaireType].append(ledDesigned)
            # If luminaireType exists already but ledDesigned is NOT its list,
            # add it to the list
            else:
                if ledDesigned not in instlCodeMap[luminaireType]:
                    instlCodeMap[luminaireType].append(ledDesigned)

# Sort all entries in the instlCodeMap alphabetically
for luminaireType in instlCodeMap:
    instlCodeMap[luminaireType].sort(key=natural_keys)

# Final step: Change the instlCode row to say "C1", "D3" etc
with arcpy.da.UpdateCursor(InputFeatureClass, [field, field2, field3]) as cursor:
    for row in cursor:
        luminaireType = row[0][0].upper()
        ledDesigned = row[1].upper()
        if ledDesigned != u'NO REPLACEMENT':
            row[2] = luminaireType + str(instlCodeMap[luminaireType].index(ledDesigned) + 1)
            cursor.updateRow(row)

print(instlCodeMap)
