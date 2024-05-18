from time import ctime
import arcpy

'''Overwriting arcpy.addmessage to ur own print function'''
def print_message(msg):
    arcpy.AddMessage(msg)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Supremepraiz\Desktop\LPC\Data\sample.gdb"

# fc = r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_admin_0_countries.shp"
fc = arcpy.GetParameterAsText(0)

if fc == "":
    fc = r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_admin_0_countries.shp"


num_feature = arcpy.GetCount_management(fc)
print_message("this shape file {0} has {1} in it".format(fc,num_feature))

# arcpy.CreateFileGDB_management(r"C:\Users\Supremepraiz\Desktop\LPC\Data","sample")
# arcpy.Select_analysis(fc, "Canada", "NAME = 'Canada'")



print_message("...........................................................................................")
print_message("Script Completed")
print_message("...........................................................................................")