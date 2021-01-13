import requests

print(requests.__version__)

url1 = "http://google.com"
r1 = requests.get(url1)
print(r1.status_code)
print(r1.text)