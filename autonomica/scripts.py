import requests

url = 'http://10.0.0.111:8080/macro?'



resp = requests.get(url=url)
data = resp.content.decode().replace('<br>', '').replace('<null>', '').replace(' ', '').replace(r'\r', '').replace("\r\n","").replace("=","").split(',')

# print(data)

for v in data:
    print(v)

from urllib.request import urlopen
from bs4 import BeautifulSoup
soup = BeautifulSoup(urlopen(url).read(), "html.parser")

print(soup.get_text())
