import json

with open("uzd4.json", encoding="utf-8") as datne:
 dati=json.load(datne)
print(type(dati))
telefoni=[]
for vardnica in dati:
    modeli.append(vardnica["modelis"])
    modeli.sort()
    print(modeli)

for vardnica in dati:
 print(vardnica["LMT"])

for vardnica in dati:
    print(vardnica["Tet"])

for vardnica in dati:
    print(vardnica["Euronics"])

videja_cena=[]
vid=(vardnica["LMT"]+vardnica["Tet"]+vardnica["Euronics"])/3


import csv

datne.open("telefonu_analize.csv",encoding="utf-8")
satur=list(csv.reader(datne))
print(satur)

datne.close()




