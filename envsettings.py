import arcpy



if arcpy.Exists(r"C:\Users\Supremepraiz\Desktop\LPC\Data\test.gdb"):
    print("already exixted but would delete to create another")
    arcpy.Delete_management(r"C:\Users\Supremepraiz\Desktop\LPC\Data\test.gdb")

arcpy.CreateFileGDB_management(r"C:\Users\Supremepraiz\Desktop\LPC\Data","test")
print("new gdb created")




print("Script Completed")