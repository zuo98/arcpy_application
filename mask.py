#-*- coding:UTF-8 -*-
import os
import glob
import arcpy

#该脚本需要自定义填写:输入文件路劲，裁剪所用的shp。
#运行完后裁剪后的文件名为在原名的基础加“_clip”，保存在Result文件夹中

arcpy.CheckOutExtension('Spatial')

#path是待裁剪影像所存放的文件夹路径；
path=r"F:/123/input"

#mask用于裁剪的shp，这里不是文件夹路径，而是指定的shp文
mask=r"F:/123/shp/mask.shp"

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

fileList = os.listdir(path)
for files in fileList:
    fileDir = os.path.join(path,files)
    if ".img" in files:
        print files
        name = files.split('.')
        outFullPath = resultDataPath + "\\"+ str(name[0]) + "_clip.img"
        arcpy.env.workspace = intermediateDataPath
        arcpy.env.overwriteOutput = True
        out_extract=arcpy.sa.ExtractByMask(fileDir,mask)
        out_extract.save(outFullPath)
        print "success"
    if ".tif" in files:
        print files
        name = files.split('.')
        outFullPath = resultDataPath + "\\"+ str(name[0]) + "_clip.tif"
        arcpy.env.workspace = intermediateDataPath
        arcpy.env.overwriteOutput = True
        out_extract=arcpy.sa.ExtractByMask(fileDir,mask)
        out_extract.save(outFullPath)
        print "success"
        
# delete intermediate data floder
for i in os.listdir(intermediateDataPath):
    path_file = os.path.join(intermediateDataPath,i)
    if os.path.isfile(path_file):
        os.remove(path_file)


print "Finish!"
endTime = datetime.datetime.now()
print "Time use: " + str((endTime - startTime).seconds)+ " (second)"
print "-----------------------------------------------------------"


    







