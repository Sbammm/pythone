vittoria=True

punteggio_giocatore1=0
punteggio_giocatore2=0


while vittoria==True:

    giocata=input("inserire la combinazione delle giocate nel formato 'carattere, spazio, carattere': ")

    giocata=giocata.upper()
    giocata=giocata.split()

    if(giocata[0]=="C" and giocata[1]=="F"):
        punteggio_giocatore2+=1
    elif(giocata[0]=="F" and giocata[1]=="C"):
        punteggio_giocatore1+=1

    elif(giocata[0]=="S" and giocata[1]=="F"):
        punteggio_giocatore2+=1
    elif(giocata[0]=="F" and giocata[1]=="S"):
        punteggio_giocatore1+=1
    
    elif(giocata[0]=="C" and giocata[1]=="S"):
        punteggio_giocatore2+=1
    elif(giocata[0]=="S" and giocata[1]=="C"):
        punteggio_giocatore1+=1
    
    elif(giocata[0]=="C" and giocata[1]=="C") or (giocata[0]=="F" and giocata[1]=="F") or (giocata[0]=="S" and giocata[1]=="S") :
        punteggio_giocatore2=0
        punteggio_giocatore1=0
       
    else:
        giocata=input("l'input inserito non è corretto. inserire nuovamente un input valido: ")
    
    #RESET DEI PUNTI SE IL GIOCATORE NON HA 3 VITTORIE IN FILA
    if((punteggio_giocatore1>0  and punteggio_giocatore2>0) or (punteggio_giocatore2>0 and punteggio_giocatore1>0)):
        punteggio_giocatore1=0
        punteggio_giocatore2=0 
    
    if(punteggio_giocatore2==3):
        vittoria=False
        print("il vincitore è il giocatore due!!")

    elif( punteggio_giocatore1==3):
        vittoria=False
        print("il vincitore è il giocatore uno!!")



    print(giocata)
    print(punteggio_giocatore1)
    print(punteggio_giocatore2)
