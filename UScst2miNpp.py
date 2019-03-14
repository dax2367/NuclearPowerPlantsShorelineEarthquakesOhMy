#Clips out US Npp within 2mi of coast from world reactors
#Takes at least 11 minutes to run
#Edit path of world reactors
#Check to see if coordinate system needs to be changed from world to
#North American projection
import arcpy
arcpy.env.workspace = "C:/CapStnPrj/CapTest/CapTest.mdb"
arcpy.Clip_analysis("NuclearReactors2011.shp","UScst2miBuf", "UScst2miNpp")