import csv
with open('data.tsv','r') as tsvin:
    for line in csv.reader(tsvin, delimiter='\t'):
        print(line)