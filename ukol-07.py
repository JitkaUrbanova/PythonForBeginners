# č. 1: \d\d?[\./] ?\d[\./] ?\d{4}
# č. 2: \d{3} ?\d{2} [\w ]+

# BONUS:

import re

uzivatelske_jmeno = re.compile(r"^[a-zA-Z]{6,10}")
jmeno = input("Zadej přihlašovací jméno: ") 
shoda_jmena = uzivatelske_jmeno.fullmatch(jmeno)
if shoda_jmena:
    print("Uživatelské jméno je v pořádku.")
else:
    print("Nesprávné uživatelské jméno.")


heslo = re.compile(r"[\w\-\.\+\=]{12,30}")
heslo_uzivatele = input("Zadej heslo: ")
shoda_hesla = heslo_uzivatele.fullmatch(heslo)
if shoda_hesla:
    print("Heslo je správné")
else:
    print("Nesprávné heslo.")


mail = re.compile(r"[\w\"\+\.\-]+@[\w\[\]\.\-]+")
mail_uzivatele = input("Zadej e-mail: ")
shoda_mailu = mail_uzivatele.fullmatch(mail)
if shoda_mailu:
    print("E-mail je platný.")
else:
    print("Neplatný e-mail.")



