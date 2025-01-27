import string

conferma=True
media=0
contatore=0

while( conferma==True ):

    numero =str(input("Dammi il numero: "))

    conferma = numero.isdigit()

    if(conferma==True):
        contatore=contatore+1
        numero=float(numero)
        print("numero :",numero)
        media=media+numero
        print("media :",media)

media= media/contatore

print("la media dei numeri dati è: ", media)