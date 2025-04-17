import random

def ListeHazirla(n):
    liste=[]
    while True:
        x = random.randint(0,100)
        if not(x in liste):
            liste.append(x)
        if len(liste)>=n:
            break
    return liste

print(ListeHazirla(10))