import arcpy

arcpy.env.overwriteOutput = True
arcpy.analysis.Select(
    in_features="Countries",
    out_feature_class=r"C:\Users\Supremepraiz\Documents\ArcGIS\Projects\learning_buffering\learning_buffering.gdb\Countries_Select",
    where_clause="NAME = 'India'"
)
arcpy.analysis.Buffer(
    in_features="Countries_Select",
    out_feature_class=r"C:\Users\Supremepraiz\Documents\ArcGIS\Projects\learning_buffering\learning_buffering.gdb\Countries_Select_Buffer",
    buffer_distance_or_field="200 Kilometers",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)
arcpy.analysis.Clip(
    in_features="Places",
    clip_features="Countries_Select_Buffer",
    out_feature_class=r"C:\Users\Supremepraiz\Documents\ArcGIS\Projects\learning_buffering\learning_buffering.gdb\Places_Clip",
    cluster_tolerance=None
)
arcpy.management.GetCount(
    in_rows="Places_Clip"
)
arcpy.management.GetCount(
    in_rows="Places_Clip"
)
arcpy.management.GetCount("Places_Clip")
# <Result '119'>
