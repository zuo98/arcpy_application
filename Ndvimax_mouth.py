import arcpy  
import time  
arcpy.CheckOutExtension("spatial")

time1=time.strftime('%y-%m-%d-%H:%M:%S')

Sname1="F:\\Modis_16\\1Moasic\\"

Sname2=".1_km_16_days_NDVI.tif"

for  i in range(2004,2014):
    
    for j in range(1,13):  
        if j>9:  
            Year= str(i)+str(j)+"0"  
        else:  
            Year= str(i)+"0"+str(j)+"0"  
        print Sname1+Year+"1"+Sname2  
        print Sname1+Year+"2"+Sname2  
        out="F:\\Modis_16\\2MVC\\"+Year[0:6]  #
        print out +" is being ........."  
        arcpy.gp.CellStatistics_sa((Sname1+Year+"1"+Sname2,Sname1+Year+"2"+Sname2) ,out, "MAXIMUM", "DATA")  
        print out +" has done.........."  
        print "-------------------------------------------------------"

        
print "<----------All are done !!!---------->"  
print "Start time : "+time1  
print "End   time : "+time.strftime('%y-%m-%d-%H:%M:%S')  
