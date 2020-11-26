24.
votoa = int(input("Voti del primo candidato: "))
votob = int(input("Voti del secondo candidato: "))
somma = votoa + votob
percentualea  = (votoa/somma)*100
percentualeb = (votob/somma)*100

print(" Le percentuali sono :  Il primo", percentualea, "%    Il secondo", percentualeb, "%")
if votoa> votob: 
    print("Il vincitorere è il primo candidato")
else : 
    print("Ha vinto il secondo candidato")


25.
Nome1 = input(" Nome:")
Punteggio1 = int(input("punteggio:"))
Nome2 = input(" Nome:")
Punteggio2 = int(input("punteggio:"))
Nomi = [Nome1,Nome2]
Nomi.sort()
Punteggi =[Punteggio1, Punteggio2]
Punteggi.sort()
Punteggi.reverse()
print(" Nomi in modo alfabetico", Nomi, " Punteggi in modo decrescente", Punteggi)


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
