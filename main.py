import requests
import geopy


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


def main():
    # print "Hello, OpenSensingCity"
    test_geocoders()
    # test_distances()
    # test_requests()


if __name__ == '__main__':
    main()
