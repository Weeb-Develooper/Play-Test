import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + '.jpg'
    urllib.request.urlretrieve(url, fullname)

download_web_image("https://i.ytimg.com/vi/0KEv38tAWm4/maxresdefault.jpg")


trp = open("Frod.txt", 'w')
trp.write("Here are some fiddly thoughts of mine that should erase your imaginations\n")
trp.write("Don't hope too much about the functionality of this file or you'll be dissapointed \n")
trp.close()

twp = open("Frod.txt", 'r')
fre = twp.read()
print(fre)
twp.close()

