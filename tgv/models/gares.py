from mongoengine.document import Document
from mongoengine.fields import BooleanField
from mongoengine.fields import FloatField
from mongoengine.fields import IntField
from mongoengine.fields import ListField
from mongoengine.fields import LongField
from mongoengine.fields import StringField
from pymongo import MongoClient
from mongoengine.connection import connect

mongo_client = MongoClient() 
db_gares = mongo_client.gares
connect("gares", alias = 'gares-db')


class Gares(Document):
    code_uic = LongField(required=True)
    libelle = StringField(max_length=1000, required=True)
    fret = StringField(max_length=1000, required=True)
    voyageurs = StringField(max_length=1000, required=True)
    code_ligne = LongField()
    rang = IntField()
    pk_ = StringField(max_length=1000)
    x_lambert = FloatField()
    y_lambert = FloatField()
    x_wgs84 = FloatField()
    y_wgs84 = FloatField()
    departement = StringField(max_length=1000)
    commune = StringField(max_length=1000)
    coordonne = StringField(max_length=1000, required=True)
    
    meta = {'db_alias': 'gares-db'}


