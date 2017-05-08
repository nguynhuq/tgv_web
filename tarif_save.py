import csv
from pymongo import MongoClient

mongo_client = MongoClient() 
db = mongo_client.tarif

csvfile = open("/home/nn251789/tgv_web/rsc/Tarif-fix.csv", "r")
reader = csv.DictReader(csvfile)
header = reader.fieldnames

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    db.tarif.insert(row)

