import requests

print(requests.__version__)

url1 = "http://google.com"
r1 = requests.get("http://google.com")
print(r1.status_code)
print(r1.text.encode('utf-8'))

rawUrl = requests.get("https://raw.githubusercontent.com/TaraYu/cmput404lab1/master/lab1.py")
print(rawUrl.text.encode('utf-8'))