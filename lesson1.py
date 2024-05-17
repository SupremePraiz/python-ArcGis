from time import ctime
import arcpy

print(f"the start time and date is {ctime()}")


fc = r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_admin_0_countries.shp"

count = arcpy.GetCount_management(fc)
print(count)

print(f"the current time and date is {ctime()}")
