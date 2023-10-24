#Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
#Tvůj program bude obsahovat dvě funkce:

#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné 
#(pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, 
#jinak vrátí hodnotu False.
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
#Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, 
#vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

#Tipy:

#Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. 
#To jsme v kurzu zatím neřešili.
#Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. 
#Ty porovnejte s řetězcem "+420".


telefonni_cislo = input("Zadej telefonní číslo: ")
predvolba = "+420"
delka_cisla = len(telefonni_cislo)

if delka_cisla == 9:
    print(True)
elif delka_cisla == 13:
    if telefonni_cislo[0:4] == predvolba:
        print(True)
    else:
        print(False)
else:
    print(False)

import math
text_zpravy = input("Zadej text zprávy: ")
delka_zpravy = len(text_zpravy)

pocet_zprav_nezao = delka_zpravy // 180

pocet_zprav = math.ceil(pocet_zprav_nezao)

print(f"Cena zprávy je {pocet_zprav * 3} Kč.")



