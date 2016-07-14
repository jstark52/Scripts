import os
import sys
import csv
import collections

#Name of files to be processed
file_txt2 = 'GADOC_payphone_20160615_cdr.txt'
file_txt1 = 'GADOC_inmate_20160615_cdr.txt'

#Name of files for output
file_csv = 'Inmate_GDOC.csv'
file_csv2= 'payphone_GDOC.csv'





#open files to read a write, change delimter form '|' to ',' and rename to .csv
with open(file_txt1,"r") as infile,open(file_csv,"w", newline='') as outfile:
	reader_pipe = csv.reader(infile, delimiter='|')
	writer_comma = csv.writer(outfile, delimiter=',')
	for row in reader_pipe:
		writer_comma.writerow(row)
		if (len(row[5])) > 10:
			print (row[5])
