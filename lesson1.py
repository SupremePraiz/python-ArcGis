from time import ctime
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Supremepraiz\Desktop\LPC\Data\sample.gdb"

fc = r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_admin_0_countries.shp"

num_feature = arcpy.GetCount_management(fc)
print("this shape file {0} has {1} in it".format(fc,num_feature))

arcpy.CreateFileGDB_management(r"C:\Users\Supremepraiz\Desktop\LPC\Data","sample")
arcpy.Select_analysis(fc, "Canada", "NAME = 'Canada'")

print("...........................................................................................")
print("Script Completed")