import random
import urllib.request


def image_downloader(url):
    name = random.randrange(1, 500)
    name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, name)

print("Enter the url to be downloaded!")

url = input()
image_downloader(url)
