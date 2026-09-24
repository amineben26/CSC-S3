import random


# gooit een dobbelsteen en geeft een getal van 1 t/m 6 terug
def dobbelsteen():
    getal = random.randint(1, 6)
    return getal


# kiest willekeurig kop of munt
def kop_of_munt():
    keuze = random.choice(["kop", "munt"])
    return keuze


# geeft een willekeurig getal onder de 100
def getal_onder_100():
    getal = random.randint(0, 99)
    return getal


# geeft een willekeurig getal tussen 1 en 10
def getal_1_tot_10():
    getal = random.randint(1, 10)
    return getal


# kiest willekeurig een kleur
def kleur():
    keuze = random.choice(["rood", "blauw", "groen"])
    return keuze