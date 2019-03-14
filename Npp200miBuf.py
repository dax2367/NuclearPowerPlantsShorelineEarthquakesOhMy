#Creates 200mi buffer around CA nuc reactors
import arcpy
arcpy.env.workspace = "C:/CapStnPrj/CapTest/CapTest.mdb"
arcpy.Buffer_analysis("CAnr", "Npp200miBufPy", "200 miles", "", "", "all")