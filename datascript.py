import json

result = []

with open('data.json') as jsonfile:
    data = json.load(jsonfile)
    for item in data:
        aux = {}
        aux["name"] = data[item]["name"]
        aux["children"] = []

        data2 = data[item]["children"]
        for item2 in data2:
            aux2 = {}
            aux2["name"] = data2[item2]["name"]
            aux2["children"] = []
            aux["children"].append(aux2)
        
            data3 = data2[item2]["children"]
            for item3 in data3:
                aux3 = {}
                aux3["name"] = data3[item3]["name"]
                aux3["src"] = data3[item3]["src"]
                aux2["children"].append(aux3)

        result.append(aux)

with open('data3.json', 'w') as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)