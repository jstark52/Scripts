import os
import sys
import datetime
import time
import os.path
import glob
import shutil
import csv


#Get paths from bat file
try:
	DropFilePath=sys.argv[1]
	ProcessedPath=sys.argv[2]
	DuplicatePath=sys.argv[3]
	LoadedFileList=sys.argv[4]
	

except:
	errorlogging("Fatal Error","y","Invalid Number of arguments")
	sys.exit(1)
	
# Check if paths are valid
if not os.path.isdir(DropFilePath):
	print("Please check LandingZone path.")
	sys.exit(2)
elif not os.path.isdir(ProcessedPath):
	print("Please check Processed path.")
	sys.exit(3)	
elif not os.path.isdir(DuplicatePath):
	print("Please check Duplicate path.")
	sys.exit(4)
elif not os.path.isdir(LoadedFileList):
	print("Please check LsProcessedDocs path.")
	sys.exit(5)
	
	
#Switch to direcotry containg files
os.chdir(DropFilePath)
Files=glob.glob("*.*")
#Time Stamp
ID = '{:%Y-%b-%d %I.%M.%S.%p}'.format(datetime.datetime.now())
IdDate = '{:%Y-%b-%d}'.format(datetime.datetime.now())
IdTime= '{:%I:%M:%S %p}'.format(datetime.datetime.now())
#Make lists to append to
Docs=[]
date=[]
time=[]
Dup=[]
IsDup=('Y')
NotDup=('N')

#For all the files in the LSDROP folder
for data in Files:
	#Retrieve name file
	flenme = os.path.basename(data)
	#Create a new name for all files, just incase there is a duplicate
	newName= ID+"_"+flenme
	Docs.append(flenme)
	time.append(IdTime)
	date.append(IdDate)

	#Move file to duplicate folder with time stamp if it was already processed
	if os.path.exists(ProcessedPath+"\\"+flenme) is True:
		Dup.append(IsDup)
		os.rename(flenme,newName)
		shutil.move(newName,DuplicatePath)
	#Move file to process folder if it was not processed yet
	elif os.path.exists(ProcessedPath+"\\"+flenme)is False:
		Dup.append(NotDup)
		shutil.move(flenme, ProcessedPath)
#takes Docs and time list and combines them into a list of tuples 
tuplst=zip(Docs,date,time,Dup)
#change path to csv file to keep track of files processed
os.chdir(LoadedFileList) 
#opens the file to write to it
with open('LASProcessedDocs.csv', 'a+', newline='') as csvfile:
	#skips header
	next(csvfile,None)
	writer=csv.writer(csvfile, delimiter=',')
	#takes list of tuples and iterates over it distributing them into File Name, Date Loaded format, and writes to csv file
	for i in tuplst:
		writer.writerows([i])
	csvfile.close()
print ('                                   ')
print ('                                   ')
print ('                                   ')
print ("*****NO MORE FILES TO PROCESS*****")
print ('                                   ')
print ('                                   ')
print ('                                   ')

