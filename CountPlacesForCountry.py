import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\Supremepraiz\Documents\ArcGIS\Projects\learning_buffering\learning_buffering.gdb"

country_name = "China"

arcpy.analysis.Select(
    in_features= r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_admin_0_countries.shp",
    out_feature_class=r"C:\Users\Supremepraiz\Documents\ArcGIS\Projects\learning_buffering\learning_buffering.gdb\Countries_Select",
    where_clause="NAME = '{0}'".format(country_name)
)

arcpy.analysis.Buffer(
    in_features="Countries_Select",
    out_feature_class="Countries_Select_Buffer",
    buffer_distance_or_field="200 Kilometers",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)
arcpy.analysis.Clip(
    in_features=r"C:\Users\Supremepraiz\Desktop\LPC\Data\ne_10m_populated_places.shp",
    clip_features="Countries_Select_Buffer",
    out_feature_class=r"C:\Users\Supremepraiz\Documents\ArcGIS\Projects\learning_buffering\learning_buffering.gdb\Places_Clip",
    cluster_tolerance=None
)

print("there's {0} populated places in and within 200k of {1}".format(arcpy.management.GetCount("Places_Clip"),country_name))

# <Result '119'>


print("Script ran Successfully")