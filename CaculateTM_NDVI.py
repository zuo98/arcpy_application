# -*- coding: utf-8 -*-
import os,arcpy,datetime
from arcpy.sa import *

#存放文件夹的位置
path = r"D:\321"

# start calculate time
startTime = datetime.datetime.now()

# set the intermediate data folder
intermediateDataPath = path+"\\"+"IntermediateData"
# set result data folder
resultDataPath = path+"\\"+"Result"

# determine if the folder exists
if os.path.exists(intermediateDataPath):
    print "IntermediateData floder exists"
else:
    # create a intermediate data floder
    arcpy.CreateFolder_management(path, "IntermediateData")    
if os.path.exists(resultDataPath):
    print "Result floder exists"
else:   
    # create a result floder
    arcpy.CreateFolder_management(path, "Result")


print "-----------------------------------------------------------"
print "Under calculation......"
print "Please do not close the window."

# get files in your path 
fileList = os.listdir(path)
for files in fileList:
    outFullPath = resultDataPath + "\\"+files+'NDVI'+ ".tif"
    fileDir = os.path.join(path,files)#每个files的路径        
    TMlist=os.listdir(fileDir)
    
    if 'LC8' in files:
        print TMlist[5]
        print TMlist[6]
        # set workspace
        arcpy.env.workspace = intermediateDataPath
        arcpy.env.overwriteOutput = True
        # Caculate NDVI
        # Check out the ArcGIS 3D Analyst extension license
        arcpy.CheckOutExtension("3D")
        # Converted to floating-point data
        arcpy.Float_3d(fileDir+'\\'+TMlist[5], "floatRedBand.tif")
        arcpy.Float_3d(fileDir+'\\'+TMlist[6], "floatNIRRedBand.tif")
        #后续操作在workspace中进行不需要设置具体路径
        arcpy.Minus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outminus.tif")
        arcpy.Plus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outplus.tif")        
        arcpy.Divide_3d("outminus.tif", "outplus.tif", outFullPath)
        print "The " + files+'NDVI'+ " has been processed."
        
    if 'LE7' in files or 'LT5' in files:
        print TMlist[2]
        print TMlist[3]
        # set workspace
        arcpy.env.workspace = intermediateDataPath
        arcpy.env.overwriteOutput = True
        # Caculate NDVI
        # Check out the ArcGIS 3D Analyst extension license
        arcpy.CheckOutExtension("3D")
        # Converted to floating-point data
        arcpy.Float_3d(fileDir+'\\'+TMlist[2], "floatRedBand.tif")
        arcpy.Float_3d(fileDir+'\\'+TMlist[3], "floatNIRRedBand.tif")
        #后续操作在workspace中进行不需要设置具体路径
        arcpy.Minus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outminus.tif")
        arcpy.Plus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outplus.tif")        
        arcpy.Divide_3d("outminus.tif", "outplus.tif", outFullPath)
        print "The " + files+'NDVI'+ " has been processed."
        
    if 'LM1' in files:
        print TMlist[1]
        print TMlist[2]
        # set workspace
        arcpy.env.workspace = intermediateDataPath
        arcpy.env.overwriteOutput = True
        # Caculate NDVI
        # Check out the ArcGIS 3D Analyst extension license
        arcpy.CheckOutExtension("3D")
        # Converted to floating-point data
        arcpy.Float_3d(fileDir+'\\'+TMlist[1], "floatRedBand.tif")
        arcpy.Float_3d(fileDir+'\\'+TMlist[2], "floatNIRRedBand.tif")
        #后续操作在workspace中进行不需要设置具体路径
        arcpy.Minus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outminus.tif")
        arcpy.Plus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outplus.tif")        
        arcpy.Divide_3d("outminus.tif", "outplus.tif", outFullPath)
        print "The " + files+'NDVI'+ " has been processed."

#清理workspace中的缓存数据        
for i in os.listdir(intermediateDataPath):
    path_file = os.path.join(intermediateDataPath,i)
    if os.path.isfile(path_file):
        os.remove(path_file)

print "Finish!"
endTime = datetime.datetime.now()
print "Time use: " + str((endTime - startTime).seconds)+ " (second)"
print "-----------------------------------------------------------"
        
        
