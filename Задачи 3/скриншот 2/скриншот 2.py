import csv
def Vika():
    with open('yyy.csv') as a:
        reader=csv.reader(a)
        for row in reader:
            print (row)
Vika()