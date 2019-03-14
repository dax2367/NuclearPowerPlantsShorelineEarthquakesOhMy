#2mi buffer of US coast
#Takes at least 2.5 hours to execute
import arcpy
arcpy.env.workspace = "C:/CapStnPrj/CapTest/CapTest.mdb"
arcpy.Buffer_analysis("CAnr", "UScst2miBuf", "2 miles", "Full", "Round", "all")