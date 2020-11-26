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
