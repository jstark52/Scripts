import csv


#headers = ['Transaction ID', 'Account Number', 'Account Name', 'Banke Name', 'Trans DateTime', 'Description', 'Amount','Type','Channel' ]
with open("CHI2011.csv","r") as infile,open("CHI2011_coords.csv","w", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        row[21] = cords.replace('(', '"').replace(')', '"')
        writer.writerow(row)
