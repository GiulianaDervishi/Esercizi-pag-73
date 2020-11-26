voto1 = int(input("Voti del primo candidato: "))
voto2 = int(input("Voti del secondo candidato: "))
somma = voto1 + voto2
percentuale1  = (votoa/somma)*100
percentuale2 = (votob/somma)*100

print(" Le percentuali sono :  Il primo", percentuale1, "%    Il secondo", percentuale2, "%")
if voto1> voto2: 
    print("Il vincitorere è il primo candidato")
else : 
    print("Ha vinto il secondo candidato")
