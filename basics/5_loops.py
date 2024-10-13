#while

liczba = 100
while liczba >-1:
    print(liczba)
    liczba -=1


wynik = 0
i = 1
while i<=4:
    x = int(input("Podaj liczbę, ktora ma być dodana: "))
    wynik += x
    print("Aktualna suma to: ",wynik)
    i += 1

wynik = 0
for j in range(1,4): #in [0,1,2] lub in "tralala" lub in [32,55,44,20]
    x = int(input("Podaj liczbę, ktora ma być dodana: "))
    wynik += x
    print("Aktualna suma to: ",wynik)
