import urllib.request

fHand = urllib.request.urlopen('http://127.0.0.1:9001/test.txt')

for line in fHand:
    print(line.decode().strip())