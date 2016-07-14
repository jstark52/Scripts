import sys
import os 
import schedule
import time
import collections
import datetime


#Using schedule, a continuous loop running every 1 second will monitor the folder "filedrop"
#defining the "job" that will be done
def job():
	#Find any file in the folder "filedrop" with a .txt then scan it
	for file in os.listdir("/Users/justinstarkman/Desktop/Filedrop/"):
		if file.endswith(".txt"):
			#open the file and check to see if it empty
			#if the file is empty it will be moved to the failure folder with a message why
			#if the file has contents the scanning will continue
			with open(file) as f:
				#save file name so it is easy to implement later
				flenme = os.path.basename(file) 	
				#find the amount of records in the file, if any
				cnt= os.stat(file).st_size  		
				try:
					#if there are contents in the file it will be moved to the success folder
					if cnt > 0:
						#date and time for a timestamp
						curtime = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
						#strips the \n 
						fle = [line.strip() for line in f] 	
						count= sum(1 for _ in fle)
						#find the most common length and makes it a variable
						most_common_length = collections.Counter(fle).most_common(1)[0][0]
						# determines the lines of any uncommon lengths
						uncommon = [n for n, v in enumerate(fle) if v != most_common_length]
						#add 1 to each element because the .txt file doesn't start counting from 0 like python does
						rt = [x+1 for x in uncommon]
		
						#moving files based on if all records are the same length or not
						if len(uncommon)==0:
							#if all lengths were the same the file will move to the success foler 
							os.rename("/Users/justinstarkman/Desktop/Filedrop/{0}".format(flenme) ,"/Users/justinstarkman/Desktop/Filedrop/Success/{0}".format(flenme))
							os.chdir("/Users/justinstarkman/Desktop/Filedrop/Success") 
							#opens the file to write to it
							FldFle= open("Processed_records.txt","a")
							#adds to the failed file which file failed, which line or lines made it fail and a timestamp
							FldFle.write('--"%s" was moved to the "Success" folder because all lines were the same length. A total number of "%s" records were processed. %s \n' % (flenme,count,curtime));
							FldFle.close()
							os.chdir("/Users/justinstarkman/Desktop/Filedrop") 
						else:
							#if all lengths were not the same the file will be moved to the failure folder
							os.rename("/Users/justinstarkman/Desktop/Filedrop/{0}".format(flenme) ,"/Users/justinstarkman/Desktop/Filedrop/Failure/{0}".format(flenme))		
							#changes directory to add to the failed_files document why the file failed
							os.chdir("/Users/justinstarkman/Desktop/Filedrop/Failure") 
							#opens the file to write to it
							FldFle= open("failed_files.txt","a")
							#adds to the failed file which file failed, which line or lines made it fail and a timestamp
							FldFle.write('--"%s" was moved to the "Failure" folder because line %s  was not like the rest. %s \n' % (flenme,rt,curtime));
							FldFle.close()
							os.chdir("/Users/justinstarkman/Desktop/Filedrop")
					#if the file was empty it will follow these rules
					else:
						#get date and time
						curtime = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
						#the file will be moved to the failure folder with a reason and time stamp
						os.rename("/Users/justinstarkman/Desktop/Filedrop/{0}".format(flenme) ,"/Users/justinstarkman/Desktop/Filedrop/Failure/{0}".format(flenme))
						os.chdir("/Users/justinstarkman/Desktop/Filedrop/Failure") 		
						FldFle= open("failed_files.txt","a")
						FldFle.write('--"%s" was moved to the "Failure" folder because it was an empty file. %s \n' % (flenme,curtime));
						FldFle.close()
						os.chdir("/Users/justinstarkman/Desktop/Filedrop")
				#for some reason if the file is opened but not a .txt an error message will be produced
				except :
					print 'ERROR'
#the program will check the folder for a new file ever 1 second
schedule.every(1).seconds.do(job)	
	
	

while True:
	schedule.run_pending()
	time.sleep(1)
		
	