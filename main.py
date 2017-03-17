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

    for s, p, o in graph.triples((None, RDF.type, pk.ParkingPlace)):
        for p,o in graph.predicate_objects(s):
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long'):
                print "long: " + o
            if p == rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat'):
                print "lat: "+o
        break


def main():
    # print "Hello, OpenSensingCity"
    # test_geocoders()
    # test_distances()
    # test_requests()
    # test.main()
    test_final()

if __name__ == '__main__':
    main()
