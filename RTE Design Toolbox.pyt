import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "RTE Design Toolbox"
        self.alias = "RTE Design Toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [InstlCode]


class InstlCode(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Install Code Generator"
        self.description = "Calculates Install Codes based on the Luminaire Type and each unique value found in the LED Designed field."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter("InputFeatureClass","Municipality Dataset","Input","DEFeatureClass","Required")
        param0.summary = "some description here"
        param1 = arcpy.Parameter("field","Luminaire Type Field","Input", "Field","Required")
        param1.filter.list = ['Text']
        param1.parameterDependencies = [param0.name]  
        param2 = arcpy.Parameter("field2", "LED Designed Field","Input", "Field","Required")
        param2.filter.list = ['Text']
        param2.parameterDependencies = [param0.name]  
        param3 = arcpy.Parameter("field3", "Install Code Field", "Input", "Field","Required")
        param3.filter.list = ['Text']
        param3.parameterDependencies = [param0.name]  

        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        import re, arcpy

        InputFeatureClass = parameters[0].valueAsText
        field = parameters[1].valueAsText
        field2 = parameters[2].valueAsText
        field3 = parameters[3].valueAsText

        def atoi(text):
            return int(text) if text.isdigit() else text

        def natural_keys(text):
            return [ atoi(c) for c in re.split(r'(\d+)W', text) ]

        instlCodeMap = {}

        with arcpy.da.UpdateCursor(InputFeatureClass, [field, field2, field3]) as cursor:
            for row in cursor:
                luminaireType = row[0][0].upper()
                ledDesigned = row[1].upper()
                if ledDesigned != u'NO REPLACEMENT':
                    if luminaireType not in instlCodeMap:
                        instlCodeMap[luminaireType] = []
                        instlCodeMap[luminaireType].append(ledDesigned)
                    else:
                        if ledDesigned not in instlCodeMap[luminaireType]:
                            instlCodeMap[luminaireType].append(ledDesigned)

        for luminaireType in instlCodeMap:
            instlCodeMap[luminaireType].sort(key=natural_keys)

        with arcpy.da.UpdateCursor(InputFeatureClass, [field, field2, field3]) as cursor:
            for row in cursor:
                luminaireType = row[0][0].upper()
                ledDesigned = row[1].upper()
                if ledDesigned != u'NO REPLACEMENT':
                    row[2] = luminaireType + str(instlCodeMap[luminaireType].index(ledDesigned) + 1)
                    cursor.updateRow(row)

        print(instlCodeMap)
        
        return
        