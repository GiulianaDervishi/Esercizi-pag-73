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


26.
somma = 0
conto =0
while True:
    numero = int(input("scrivi stipendio: "))
    if numero == -1: 
        break
    else :
        somma += stipendio
        conto+= 1
        media = somma/ conto
print("la media è: %s" % media)


27.
somma = 0
conto =0
while True:
    numero = int(input("scrivi numero veicoli per giorno: "))
    if numero == 0: 
        break
    else :
        somma += numero
        conto+= 1
print("Il totale dei veicoli per ", conto, "giorni è: %s" % somma)
