#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli 
#prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět 
#jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň 
#60 bodů. Pokud má méně než 60, hodnota bude "Fail".

#Výsledný slovník ulož jako JSON do souboru prospech.json.

import json

with open("body.json", mode = "r", encoding = "utf-8") as soubor:
    hodnoceni = json.load(soubor)

print(hodnoceni)

nove_hodnoceni = {}

for jmeno, body in hodnoceni.items():
    if body >= 60:
        nove_hodnoceni[jmeno] = "Pass"
    elif body < 60:
        nove_hodnoceni[jmeno] = "Fail"
       

with open("prospech.json", mode = "w", encoding="utf-8") as file:
    json.dump(nove_hodnoceni, file, ensure_ascii=False)

print(nove_hodnoceni)


