cont=0
valore_precedente=-1
while(cont<1):
    
    valore= float(input("qui prendo l'acquisizione del numero :"))
    if valore==0 and valore_precedente==0:
        cont=cont+1
    valore_precedente=valore
    
    print("il valore inserito è :", valore)

print("la sequenza di numeri è finita")
