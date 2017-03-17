import requests

def test_requests():
    request = requests.get('https://google.com')
    print request.status_code
    #print request.content
    return request.status_code

def main():
    print "Hello, OpenSensingCity"
    #test_requests()

if __name__ == '__main__':
    main()