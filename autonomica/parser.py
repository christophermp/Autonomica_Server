import requests
import json
url2 = 'http://10.0.0.111:8090/getconfiguration'

content = requests.get(url2).content

j = json.loads(content)

request_url = 'http://10.0.0.111:8090/getconfiguration'
r = requests.get(request_url).json()

for i in r["workspaces"][0]["tasks"]:
    print(i["name"], i['devicesReferenced'])