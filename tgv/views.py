from django.shortcuts import render
from tgv.models.gares import Gares, db_gares
from tgv.models.tarif import Tarif, db_tarif
import json
from django.http import HttpResponse

'''url localhost:8000/browse: Load all data of Gares object'''
def browse(request):
    gares = Gares.objects
    gares_unique = list(set(gares))
    return render(request, 'browse.html',{'Gares': gares_unique})

'''url localhost:8000/find: Load google maps API'''
def gares_list(request):
    list_gares = []
    all_gares = db_gares.gares.find()
    for gare in all_gares:
        record = {}
        record['libelle'] = gare['libelle']
        coordone = gare['coordonne'].split(',')
        if len(coordone) == 2:
            record['lat'] = gare['coordonne'].split(',')[0].strip()
            record['lng'] = gare['coordonne'].split(',')[1].strip()
        list_gares.append(record)
    data = json.dumps(list_gares)
    return HttpResponse(data, content_type='application/javascript')

'''url localhost:8000/find: Get tarif with specific departure and destination'''
def find(request):
    depart = request.GET['depart']
    destination = request.GET['destination']
    
    gare_depart = db_gares.gares.find_one({'code_uic': depart})
    gare_destination = db_gares.gares.find_one({'code_uic': destination})
    libelle_depart = gare_depart['libelle']
    libelle_destination = gare_destination['libelle']
    
    trip1 = db_tarif.tarif.find_one({'$and': [{'oc1': {'$regex': r'%s' % libelle_depart.upper()}},
                                        {'oc2': {'$regex': r'%s' % libelle_destination.upper()}}]
                                 })
    
    trip2 = db_tarif.tarif.find_one({'$and': [{'oc1': {'$regex': r'%s' % libelle_destination.upper()}},
                                        {'oc2': {'$regex': r'%s' % libelle_depart.upper()}}]
                                 })

    if trip1:
        appel_2nde = trip1['appel_2nde']
        loisir_2nde = trip1['loisir_2nde']
        loisir_1ere = trip1['loisir_1ere']
    elif trip2:
        appel_2nde = trip2['appel_2nde']
        loisir_2nde = trip2['loisir_2nde']
        loisir_1ere = trip2['loisir_1ere']
    else:
        appel_2nde = 0
        loisir_2nde = 0
        loisir_1ere = 0
    params = {"libelle_depart": libelle_depart,
              "libelle_destination": libelle_destination,
              "appel_2nde" : appel_2nde,
              "loisir_2nde" : loisir_2nde,
              "loisir_1ere" : loisir_1ere,
              }
    return render(request, 'find.html', params)

'''url localhost:8000/inspire: Get tarif with specific departure
    and all possible destination'''
def inspire(request):
    depart = request.GET['depart_inspire']

    gare_depart = db_gares.gares.find_one({'code_uic': depart})
    libelle_depart = gare_depart['libelle']
    trip1_list = db_tarif.tarif.find({'oc1': {'$regex': r'%s' % libelle_depart.upper()}})
    trip2_list = db_tarif.tarif.find({'oc2': {'$regex': r'%s' % libelle_depart.upper()}})
    list_destination = []
    if trip1_list.count() > 0:
        for trip1 in trip1_list:
            record = {}
            record['libelle_destination'] = trip1['oc2']
            record['appel_2nde'] = trip1['appel_2nde']
            record['loisir_2nde'] = trip1['loisir_2nde']
            record['loisir_1ere'] = trip1['loisir_1ere']
            list_destination.append(record)
    elif trip2_list.count() > 0:
        for trip2 in trip2_list:
            record = {}
            record['libelle_destination'] = trip2['oc1']
            record['appel_2nde'] = trip2['appel_2nde']
            record['loisir_2nde'] = trip2['loisir_2nde']
            record['loisir_1ere'] = trip2['loisir_1ere']
            list_destination.append(record)
    else:
        record = {}
        record['libelle_destination'] = None
        record['appel_2nde'] = None
        record['loisir_2nde'] = None
        record['loisir_1ere'] = None
        list_destination.append(record)
    
    params = {"libelle_depart": libelle_depart,
              "list_destination": list_destination
              }
    return render(request, 'inspire.html', params)

