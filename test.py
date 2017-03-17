import rdflib

staticPage = 'http://opensensingcity.emse.fr/tuba/data/static-rdf/nantes/nantes.parking.ttl'
dynamicPage = 'http://opensensingcity.emse.fr/sparql-generate/api/transform?queryurl=http%3A%2F%2Fopensensingcity.emse.fr%2Ftuba%2Fquery%2Fnantes.parking1.rqg'


def main():

    graphStatic=rdflib.Graph()
    graphStatic.load(staticPage, format='n3');

    print "Static Parking Page Load"

    graphDynamic=rdflib.Graph()
    graphDynamic.load(dynamicPage);

    print "Dynamic Parking Page Load"



    graph = rdflib.Graph()
    graph = graphDynamic + graphStatic

    print("Graph has %s statements." % len(graph))
    for s,p,o in graph:
        print s
        #print "Sujet"
        #print s
        #print "Predicat"
        #print p
        #print "Objet"
        #print o

    #print("Parking Found:")

    #for row in g.query('select ?parking ?predicat ?objet where { ?parking rdfs:label "ARISTIDE BRIAND"}'):
    #    print(row.parking)
    #    print type(row.parking)
    #    print(row.predicat)
    #    print type(row.predicat)
    #    print(row.objet)



    #for row in g.query("""SELECT ?parking ? ?objet ?author WHERE {
    #   [ a rdfs:label "FEYDEAU" ; """):
    #print("%s by %s"%(row.title, row.author))

if __name__ == '__main__':
    main()