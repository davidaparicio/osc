import requests
import geopy.distance

def test_distances():
    partdieu = (45.760086, 4.858450)
    la__doua = (45.783560, 4.873145)
    print(geopy.distance.vincenty(partdieu, la__doua).kilometers)

def test_requests():
    request = requests.get('https://google.com')
    print request.status_code
    #print request.content
    return request.status_code

def main():
    #print "Hello, OpenSensingCity"
    test_distances()
    #test_requests()

if __name__ == '__main__':
    main()