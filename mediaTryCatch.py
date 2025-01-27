conferma=True
media=0
contatore=0

while( conferma==True ):


    try:
        numero=float(input("Dammi il numero: "))
        contatore += 1
        media=media+numero
    except ValueError:
        #print("il numero inserito è sbagliato")
        conferma=False
        exit
        

if(contatore==0):
    contatore=1

media= media/contatore
print("\nil contatore è: ",contatore)
print("la media dei numeri dati è: ", media)
