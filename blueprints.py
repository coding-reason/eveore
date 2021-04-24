import requests
import data
categories = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 16, 17, 18, 20, 22, 23, 24, 25, 26, 29, 30, 32, 34, 35, 39, 40, 41, 42, 43, 46, 350001, 2100, 53, 54, 59, 63, 65, 66, 49, 87, 91]
bpGroupIds2 = [104, 105, 106, 107, 108, 109, 110, 111, 118, 119, 120, 121, 123, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 143, 145, 147, 148, 151, 152, 154, 156, 157, 158, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170, 172, 174, 175, 176, 177, 178, 218, 223, 224, 296, 342, 343, 344, 345, 346, 347, 348, 349, 350, 352, 356, 360, 371, 400, 401, 408, 410, 447, 477, 478, 486, 487, 489, 490, 503, 504, 516, 525, 532, 535, 537, 643, 651, 718, 722, 723, 724, 725, 726, 727, 787, 841, 853, 854, 855, 856, 857, 858, 859, 860, 870, 871, 888, 889, 890, 891, 912, 914, 915, 917, 918, 944, 945, 965, 973, 996, 1013, 1045, 1046, 1048, 1123, 1137, 1139, 1142, 1143, 1144, 1145, 1146, 1147, 1151, 1152, 1155, 1157, 1160, 1162, 1190, 1191, 1197, 1200, 1222, 1224, 1227, 1239, 1267, 1268, 1269, 1270, 1277, 1293, 1294, 1295, 1309, 1317, 1318, 1397, 1399, 1461, 1462, 1542, 1543, 1679, 1703, 1707, 1708, 1709, 1718, 1723, 1810, 1812, 1888, 1889, 1890, 1891, 1948, 1990, 1992, 1993, 1994, 2010, 2019, 2023, 4052, 4064, 4065, 4066, 4069, 4095, 4097]
bpGroupIds = [135, 136, 137, 139, 140, 141, 142, 143, 145, 147, 148, 151, 152, 154, 156, 157, 158, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170, 172, 174, 175, 176, 177, 178, 218, 223, 224, 296, 342, 343, 344, 345, 346, 347, 348, 349, 350, 352, 356, 360, 371, 400, 401, 408, 410, 447, 477, 478, 486, 487, 489, 490, 503, 504, 516, 525, 532, 535, 537, 643, 651, 718, 722, 723, 724, 725, 726, 727, 787, 841, 853, 854, 855, 856, 857, 858, 859, 860, 870, 871, 888, 889, 890, 891, 912, 914, 915, 917, 918, 944, 945, 965, 973, 996, 1013, 1045, 1046, 1048, 1123, 1137, 1139, 1142, 1143, 1144, 1145, 1146, 1147, 1151, 1152, 1155, 1157, 1160, 1162, 1190, 1191, 1197, 1200, 1222, 1224, 1227, 1239, 1267, 1268, 1269, 1270, 1277, 1293, 1294, 1295, 1309, 1317, 1318, 1397, 1399, 1461, 1462, 1542, 1543, 1679, 1703, 1707, 1708, 1709, 1718, 1723, 1810, 1812, 1888, 1889, 1890, 1891, 1948, 1990, 1992, 1993, 1994, 2010, 2019, 2023, 4052, 4064, 4065, 4066, 4069, 4095, 4097]
# def fn():
iter=0

for itmId in data.blueprintItems:
    itmUri = "https://esi.evetech.net/latest/universe/types/" +str(itmId)+ "/?datasource=tranquility&language=en"
    resp = requests.get(url=itmUri).json()
    print(resp)
    break
x = 2
for grpId in bpGroupIds:
    grpUri="https://esi.evetech.net/latest/universe/groups/"+str(grpId)+"/?datasource=tranquility&language=en"
    resp = requests.get(url=grpUri).json()
    #print(resp)
    print(str(resp['name']).replace("'", "").replace(" ", "" ) + "=" + str(resp['types']))




for catid in categories:
    categoryUri = "https://esi.evetech.net/latest/universe/categories/"+str(catid)+"/?datasource=tranquility&language=en"
    resp = requests.get(url=categoryUri).json()

    print(resp['name'] + "  "+ str(resp['category_id']))
    print (resp)
    if resp['category_id'] == 9:
        break




marketUri = "https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id="
compressedOre = [data.arkonor, data.primearkonor, data.crimsonarkonor]

for data in compressedOre:
    id = data["id"]
    uri = marketUri + str(id)
    response = requests.get(url=uri).json()
    print(response)

groupUri = "https://esi.evetech.net/latest/universe/groups/?datasource=tranquility&page=1"
# groups = requests.get(url=groupUri).json()
astroidItem = {}
itemUri = "https://esi.evetech.net/latest/universe/types/8/?datasource=tranquility&language=en"
groupIdUri = "https://esi.evetech.net/latest/universe/groups/25/?datasource=tranquility&language=en"
for g in data.astroidCatgories:
    gurl = "https://esi.evetech.net/latest/universe/groups/" + str(g) + "/?datasource=tranquility&language=en"
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
    print("stationId:", d)
    url = "https://esi.evetech.net/latest/universe/stations/" + str(d) + "/?datasource=tranquility"
    response = requests.get(url=url)
    data = response.json()
    print(data)
