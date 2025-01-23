#Prova ottimizzata del calcolo della aliquota
#premetto che non ho idea di come si calcola l'aliquota 

# Soldi dell'utente (il suo reddito).
reddito = float(input("Inserisci il reddito: "))
aliquota1=0.23
aliquota2=0.35
aliquota3=0.43

# Calcolo dell'aliquota e imposta

if reddito<=28000:
    imposta = reddito * aliquota1

elif reddito <= 50000:
    imposta= 28000*0.23 + (reddito - 28000)*0.35

else:
    imposta= 28000*0.23 + 50000*0.35 + ((reddito - 50000)*0.43)


'''if reddito <= 28000:
    aliquota = 0.23
elif reddito <= 50000:
    aliquota = 0.35
else:
    aliquota = 0.43
'''
'''
if reddito <= 28000:
    aliquota = 0.23
if reddito > 28000 and reddito <= 50000:
    aliquota = 0.35
if reddito > 50000:
    aliquota = 0.43

'''

#stampa a vide dei risultati 
#print(f"L'aliquota applicata è: {aliquota * 100}%") # x100 perchè in percetuale 
#print("\nL'aliquota applicata è :" aliquota * 100, "%")



print("\nL'imposta da pagare è :" , imposta , "euro") #il \n mi crea proprio una riga di separazione tra la riga sopra e la riga sotto
print(f"L'imposta da pagare è: {imposta} euro")     #imposta 






