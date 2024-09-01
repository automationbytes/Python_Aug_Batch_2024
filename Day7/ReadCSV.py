import csv

with open("sample.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        print(r['Name'],r['Country'])

'''        
set proxy = ""
set https-proxy =""
set http-proxy =""

'''