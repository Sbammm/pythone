

#questo funziona
'''
# Lista iniziale con valori come stringhe
lista = ["10", "9", "5", "8", "7", "6", "4", "2", "8", "6", "7", "0"]

# Convertiamo la lista da stringhe a numeri interi
lista = [int(i) for i in lista]

# Troviamo il minimo e lo rimuoviamo dalla lista
minimo = min(lista)
lista.remove(minimo)

# Calcoliamo la somma dei numeri rimanenti
media = sum(lista) / len(lista)

# Stampiamo i risultati
print("La media dei numeri è:", media)
print("Il numero rimosso dalla lista è:", minimo)
'''

'''
#questo funziona

import string
media=0
numeri=0

lista=["10","9","5","8","7","6","4","2","8","6","7","0"]

minimo=min(lista)
lista.remove(minimo)
lunghezza=len(lista)

for i in range (lunghezza):

    media=media + int(lista[numeri])
    numeri+=1

media=media/numeri
print("la media dei numeri è: ",media)
print("il numero rimosso dalla lista è :", minimo)
'''

#questo funziona


voti=[]
riga=input() #si mette sta cosa per far fareun ciclo in più visto che non c'è il while in coda
while riga.isdigit():   #finchè è un numero, lo inserisce dentro voti 
    voti.append(int(riga))    #append inserisce un valore dentro una stringa/arrai e con "int" forziamo il valore ad essere intero
    riga=input()                #si prende un nuovo valore di input che però verrà preso in loop


voti.remove(min(voti))  #toglie i voti minimi 
voti.remove(max(voti))  #toglie i voti massimi

print("la media dei numeri è: ", sum(voti)/len(voti))   #usa la funzione sum e len per fare la media 

