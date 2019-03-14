#Clips US quake history to include only those within 200mi of CA nuc reactors
import arcpy
arcpy.env.workspace = "C:/CapStnPrj/CapTest/CapTest.mdb"
arcpy.Clip_analysis("Usquakehist","Npp200miBuf", "NppQuakeHistPy")