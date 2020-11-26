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
