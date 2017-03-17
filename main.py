import requests
import geopy.distance
import test

import rdflib
from rdflib.namespace import Namespace, RDF
from rdflib.term import Literal

def test_geocoders():
    geolocator = geopy.geocoders.Nominatim()
    location = geolocator.geocode("1 Place Charles Beraudier, 69003 Lyon, France")
    # location = geolocator.geocode("175 5th Avenue NYC")
    print(location.address)
    print((location.latitude, location.longitude))

def test_distances():
    partdieu = (45.760086, 4.858450)
    la__doua = (45.783560, 4.873145)
    print(geopy.distance.vincenty(partdieu, la__doua).kilometers)

def test_requests():
    request = requests.get('https://google.com')
    print request.status_code
    # print request.content
    return request.status_code

def test_premier():
    staticPage = 'http://opensensingcity.emse.fr/tuba/data/static-rdf/nantes/nantes.parking.ttl'
    dynamicPage = 'http://opensensingcity.emse.fr/sparql-generate/api/transform?queryurl=http%3A%2F%2Fopensensingcity.emse.fr%2Ftuba%2Fquery%2Fnantes.parking1.rqg'
    pk = Namespace("http://opensensingcity.emse.fr/ontologies/parking/")

    graphStatic=rdflib.Graph()
    graphStatic.load(staticPage, format='n3');

    graphDynamic=rdflib.Graph()
    graphDynamic.load(dynamicPage);

    graph = rdflib.Graph()
    graph = graphDynamic + graphStatic

    #geolocator = geopy.geocoders.Nominatim()
    #location = geolocator.geocode("1 Place Charles Beraudier, 69003 Lyon, France")
    #print((location.latitude, location.longitude))

    for s, p, o in graph.triples((None, RDF.type, pk.ParkingPlace)):
        for p,o in graph.predicate_objects(s):
            if p == rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#label'):
                print "label: " + o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long'):
                long = o
                print "long: " + o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat'):
                print "lat: "+o
                lat = o

        break

def test_quasi():
    staticPage = 'http://opensensingcity.emse.fr/tuba/data/static-rdf/nantes/nantes.parking.ttl'
    dynamicPage = 'http://opensensingcity.emse.fr/sparql-generate/api/transform?queryurl=http%3A%2F%2Fopensensingcity.emse.fr%2Ftuba%2Fquery%2Fnantes.parking1.rqg'
    pk = Namespace("http://opensensingcity.emse.fr/ontologies/parking/")

    graphStatic=rdflib.Graph()
    graphStatic.load(staticPage, format='n3');

    graphDynamic=rdflib.Graph()
    graphDynamic.load(dynamicPage);

    graph = rdflib.Graph()
    graph = graphDynamic + graphStatic

    #geolocator = geopy.geocoders.Nominatim()
    #location = geolocator.geocode("27 Boulevard de Stalingrad, 44000 Nantes, France")
    gare_lat  = 47.2178988
    gare_long = -1.5429709
    #print((location.latitude, location.longitude))

    distanceMin = 9999999999
    best_long = 0.000000
    best_lat  = 0.000000
    best_label = "LABEL"

    for s, p, o in graph.triples((None, RDF.type, pk.ParkingPlace)):
        long = 0.000000
        lat = 0.000000
        label = ""
        for p,o in graph.predicate_objects(s):
            if p == rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#label'):
                label = o
                #print "label: " + o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long'):
                long = o
                #print "long: " + o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat'):
                #print "lat: "+o
                lat = o

        if geopy.distance.vincenty((gare_long,gare_lat), (long,lat)).kilometers<distanceMin:
            best_long = long
            best_lat = lat
            best_label = label
            distanceMin = geopy.distance.vincenty((gare_long,gare_lat), (long,lat)).kilometers
        #print (geopy.distance.vincenty((gare_long,gare_lat), (long,lat)).kilometers)

    print "Best parking "
    print best_label
    print "from"
    print distanceMin
    print "kms"

def test_final():
    staticPage = 'http://opensensingcity.emse.fr/tuba/data/static-rdf/nantes/nantes.parking.ttl'
    dynamicPage = 'http://opensensingcity.emse.fr/sparql-generate/api/transform?queryurl=http%3A%2F%2Fopensensingcity.emse.fr%2Ftuba%2Fquery%2Fnantes.parking1.rqg'
    pk = Namespace("http://opensensingcity.emse.fr/ontologies/parking/")

    graphStatic=rdflib.Graph()
    graphStatic.load(staticPage, format='n3');
    graphDynamic=rdflib.Graph()
    graphDynamic.load(dynamicPage);

    graph = rdflib.Graph()
    graph = graphDynamic + graphStatic

    geolocator = geopy.geocoders.Nominatim()
    location = geolocator.geocode("27 Boulevard de Stalingrad, 44000 Nantes, France")
    print((location.latitude, location.longitude))

    distanceMin = 9999999999
    best_label = "LABEL"

    for s, p, o in graph.triples((None, RDF.type, pk.ParkingPlace)):
        long = 0.000000
        lat = 0.000000
        label = ""
        for p,o in graph.predicate_objects(s):
            if p == rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#label'):
                label = o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long'):
                long = o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat'):
                lat = o

        if geopy.distance.vincenty((location.longitude,location.latitude), (long,lat)).kilometers<distanceMin:
            best_label = label
            distanceMin = geopy.distance.vincenty((location.longitude,location.latitude), (long,lat)).kilometers

    print "Best parking "
    print best_label
    print "from"
    print distanceMin
    print "kms"

def main():
    # print "Hello, OpenSensingCity"
    # test_geocoders()
    # test_distances()
    # test_requests()
    # test.main()
    # test_premier()
    # test_quasi()
    test_final()

if __name__ == '__main__':
    main()
