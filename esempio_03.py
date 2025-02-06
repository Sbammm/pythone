partita = True
giocatore1=0
giocatore2=0
punto1=0
punto2=0

while partita:
    inserimento=int(input("inserire il numero del giocatore che ha fatto il punto : "))

    if inserimento==1 :

        if giocatore1<30 :
            giocatore1+=15

        else :
            giocatore1+=10
            punto1+=1
            if punto1>=2:
                giocatore1=giocatore1-10
                partita=False
                print("HA VINTO IL GIOCATORE 1")
        
    else:

        if giocatore2< 30:
            giocatore2+=15

        else:
            giocatore2+=10
            punto1+=1
            if punto2>=2:
                giocatore2=giocatore2-10
                partita=False
                print("HA VINTO IL GIOCATORE 2")


    #print("il punteggio del giocatore 1 è : ", giocatore1)
    #print("il punteggio del giocatore 2 è : ", giocatore2)

    

    
