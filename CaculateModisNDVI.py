# -*- coding: utf-8 -*-
import os,arcpy,datetime
from arcpy.sa import *

# set your hdf data path
path = r"D:\11111111"
# start calculate time
startTime = datetime.datetime.now()
# get files in your path 
fileList = os.listdir(path)
print "The file under this folder has："
for files in fileList:
    fileDir = os.path.join(path,files)
    if os.path.isfile(fileDir):
        print files
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
for files in fileList:
    fileDir = os.path.join(path,files)
    if ".hdf" in files:
        name = files.split('.')
        newName = str(name[1]) + str(name[2]) + str(name[3]) + str(name[4])
        outFullPath = resultDataPath + "\\"+ newName + ".tif" 
    if ".hdf" in fileDir:
        file_extension = os.path.splitext(files)[1]
        if file_extension == ".hdf":
            # set workspace
            arcpy.env.workspace = intermediateDataPath
            arcpy.env.overwriteOutput = True #输出的文件已经存在则覆盖掉
            arcpy.ExtractSubDataset_management(fileDir,"RedBand.tif","0")#从波段组合图中提取红光波段
            arcpy.ExtractSubDataset_management(fileDir,"NIRRedBand.tif","1")#从波段组合图中提取近红外波段
            # Caculate NDVI
            # Check out the ArcGIS 3D Analyst extension license
            arcpy.CheckOutExtension("3D")
            # Converted to floating-point data
            arcpy.Float_3d("RedBand.tif", "floatRedBand.tif")
            arcpy.Float_3d("NIRRedBand.tif", "floatNIRRedBand.tif")
            arcpy.Minus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outminus.tif")
            arcpy.Plus_3d("floatNIRRedBand.tif", "floatRedBand.tif", "outplus.tif")        
            arcpy.Divide_3d("outminus.tif", "outplus.tif", outFullPath)
            print "The " + newName + " has been processed."

'''
#归一化处理
#Get the geoprocessing result object
minResult = arcpy.GetRasterProperties_management("midNDVI.tif", "MINIMUM")
maxResult = arcpy.GetRasterProperties_management("midNDVI.tif", "MAXIMUM")
#Get the elevation standard deviation value from geoprocessing result object
minValue = minResult.getOutput(0)
maxValue = maxResult.getOutput(0)
chazhi = float(maxValue) - float(minValue)
arcpy.Minus_3d("midNDVI.tif", minValue, "minuMin.tif")
arcpy.Divide_3d("minuMin.tif", chazhi, "norNDVI.tif")
'''

# delete intermediate data floder
for i in os.listdir(intermediateDataPath):
    path_file = os.path.join(intermediateDataPath,i)
    if os.path.isfile(path_file):
        os.remove(path_file)

print "Finish!"
endTime = datetime.datetime.now()
print "Time use: " + str((endTime - startTime).seconds)+ " (second)"
print "-----------------------------------------------------------"
print'\n'.join([''.join([('LoveJolin'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])


