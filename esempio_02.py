valore= int(input(" dammi un input numerico seguito dalla lettera di rferimento : "))
lettera= input("dammi la lettera ")

for i in range(0,valore):
    print(" " * (valore-i-1) + lettera * (1+i*2) )




