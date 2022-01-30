import urllib.request
import random
import time
import yaml

def start(data):
    while True:
        url = generate_url(data['generate'])

        try:
            contents = urllib.request.urlopen(url)
            print('Success: {}'.format(url))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print('Fail: {}'.format(url))
            elif e.code == 429:
                time.sleep(5)

def generate_url(generate):
    extension = ''

    for i in range(generate['length']):
        extension += random.choice(generate['chars'])
    
    return generate['url'] + extension

if __name__ == "__main__":
    f = open('websites.yaml')

    data = yaml.load(f, Loader=yaml.FullLoader)

    start(data['pastebin.com'])

    f.close()
    