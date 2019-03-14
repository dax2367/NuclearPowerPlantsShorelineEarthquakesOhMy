import arcpy
arcpy.env.workspace = "C:/CapStnPrj/CapTest"
prjFile = "C:/CapStnPrj/CapTest/CapTest.mdb/states.prj"
spatial_ref = arcpy.SpatialReference(prjFile)
arcpy.DefineProjection_management("CAnr", spatial_ref)
#arcpy.DefineProjection_management("Npp200miBuf", spatial_ref)