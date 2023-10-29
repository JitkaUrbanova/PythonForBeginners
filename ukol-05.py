#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - 
#ráno, v poledne, večer a v noci.

#Vytvoř seznam průměrných teplot pro každý den.
#Vytvoř seznam ranních teplot.
#Vytvoř seznam nočních teplot.
#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.


teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerna = [sum(hodnoty) / len(hodnoty) for hodnoty in teploty]
ranni = [hodnoty[0] for hodnoty in teploty]
nocni = [hodnoty[3] for hodnoty in teploty]
poledni_a_nocni = [[hodnoty[1], hodnoty[3]] for hodnoty in teploty]




