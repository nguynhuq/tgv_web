from mongoengine.document import Document
from mongoengine.fields import FloatField
from mongoengine.fields import StringField
from pymongo import MongoClient
from mongoengine.connection import connect

mongo_client = MongoClient() 
db_tarif = mongo_client.tarif
connect("tarif", alias = 'tarif-db')


class Tarif(Document):
    oc1 = StringField(max_length=1000, required=True)
    oc2 = StringField(max_length=1000, required=True)
    appel_2nde = FloatField()
    loisir_2nde = FloatField()
    loisir_1ere = FloatField()
    comment = StringField(max_length=1000)
    
    meta = {'db_alias': 'tarif-db'}