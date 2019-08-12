import requests

url1 = 'http://192.168.0.171:7001/barcode'
url2 = 'http://192.168.0.171:7001/'
d = {'code':'123456'}

r = requests.post(url1,data = d)
#r2 = requests.get(url2)
print(r.text)