import arcpy

arcpy.env.overwriteOutput = True

# Set the workspace for ListFeatureClasses
arcpy.env.workspace = r"C:\Users\Supremepraiz\Desktop\LPC\Data\practice.gdb"

fc = r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_admin_0_countries.shp"

for item in arcpy.Select_analysis(fc):
    print(item)


print("Script ran Successfully")