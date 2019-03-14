#Clips US coast 2mi buffer to include only 200mi buffer of CA nuc reactors
#Takes at least 6min to execute
import arcpy
arcpy.env.workspace = "C:/CapStnPrj/CapTest/CapTest.mdb"
arcpy.Clip_analysis("US2mi_Buffer","Npp200miBuf", "CAcst2miBuf")