import requests

def main():
    print 'Hello, world!'
    flag = requests.get('https://lemni.top/')
    # print flag.status_code
    print flag.content
    r = requests.post('https://lemni.top/submit.php', data={'flag': 'flag{salut_python}'})
    print r.content

if __name__ == '__main__':
    main()