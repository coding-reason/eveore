# https://esi.evetech.net/ui/?version=latest#/

import requests
import data

marketUri = "https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id="
compressedOre=[data.arkonor, data.primearkonor, data.crimsonarkonor]

for data in compressedOre:
    id = data["id"]
    uri = marketUri + str(id)
    response = requests.get(url = uri).json()
    print(response)



groupUri = "https://esi.evetech.net/latest/universe/groups/?datasource=tranquility&page=1"
# groups = requests.get(url=groupUri).json()
astroidItem = {}
itemUri = "https://esi.evetech.net/latest/universe/types/8/?datasource=tranquility&language=en"
groupIdUri = "https://esi.evetech.net/latest/universe/groups/25/?datasource=tranquility&language=en"
for g in data.astroidCatgories:
    gurl = "https://esi.evetech.net/latest/universe/groups/"+str(g)+"/?datasource=tranquility&language=en"
    response = requests.get(url=gurl)
    group = response.json()
    types = group['types']
    for t in types:
        typeUrl = "https://esi.evetech.net/latest/universe/types/" + str(t) + "/?datasource=tranquility&language=en"
        data = requests.get(url=typeUrl).json()
        print(data['name'], data['type_id'])
        astroidItem["data['name']"] = data['type_id']

stations = []

for d in stations:
    print("stationId:" , d)
    url = "https://esi.evetech.net/latest/universe/stations/" + str(d) + "/?datasource=tranquility"
    response = requests.get(url=url)
    data = response.json()
    print(data)




