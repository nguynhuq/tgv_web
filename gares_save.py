import csv

from mongoengine.connection import connect
from pymongo import MongoClient, ASCENDING

mongo_client = MongoClient() 
db = mongo_client.gares

csvfile = open("/home/nn251789/tgv_web/rsc/Gares-fix.csv", "r")
reader = csv.DictReader(csvfile)
header = reader.fieldnames

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    db.gares.insert(row)
