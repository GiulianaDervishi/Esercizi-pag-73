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
