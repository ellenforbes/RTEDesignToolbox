#Sort Fields Single
rows = arcpy.SearchCursor("Cityname_SP_YYYYMMDD",
                          fields="LEDDesigned",
                          sort_fields="LEDDesigned A")
for row in rows:
    print("{0}".format(
        row.getValue("LEDDesigned")))