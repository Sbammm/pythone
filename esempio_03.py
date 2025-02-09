
giocatore1=0
giocatore2=0
valutazione_giocatore=0
vincitore=-1
finale=True
punto_vittoria1=0
punto_vittoria2=0
print("funziona?!?!?!??!")

while finale==True:
   
    valutazione_giocatore= int(input("Inserire chi ha vinto il set con 1 o 2: ")) 
    
    #pezzo di codice che assegna il punteggio ad il primo giocatore
    if valutazione_giocatore==1:
        if giocatore1<30:
            giocatore1+=15

        elif giocatore1<40:
            giocatore1+=10
            punto_vittoria1+=1
        else:
            punto_vittoria1+=1

    


    #pezzo di codice che assegna il punteggio ad il secondo giocatore
    if valutazione_giocatore==2:
        if giocatore2<30:
            giocatore2+=15

        elif giocatore2<40:
            giocatore2+=10
            punto_vittoria2+=1
        else:
            punto_vittoria2+=1




#pezzo di codice che mi controlla dai 40 punti il primo che fa due vittorie di fila sull avversario
    if punto_vittoria1==1 and punto_vittoria2==1:
        punto_vittoria1=0
        punto_vittoria2=0
    elif punto_vittoria1==2:
        vincitore=1
        finale=False
        print("il vincitore della competizione è il giocatore 1")
    elif punto_vittoria2==2:
        vincitore=2
        finale=False
        print("il vincitore della competizione è il giocatore 2")

    print("IL PUNTEGGIO 1: ",giocatore1)    
    print("il punteggio 2: ", giocatore2)
#print("punto vittoria 1 :",punto_vittoria1)
#print("PUNTO VITTORIA2: ", punto_vittoria2)
print("VINCITOREEEEE",vincitore)

    

        

    
