import random

answer = int(input("Podaj ile liczb wylosować\n"))
max_numbers = int(input("Podaj zakres liczb\n"))

myList = []

i = 0
while i < answer:
    #Funkcja randint losuje liczbę w podanym przez nas zakresie
    number = random.randint(1,max_numbers)
    #Funkcja count sprawdza ile razy pojawiła się ta liczba (number) w mojej liście (myList)
    if myList.count(number) == 0:
        #Jeśli pojawiła się 0 razy dodaj ją do listy
        myList.append(number)
        # Zwiększam licznik i
        i = i + 1


print("numbers: ", myList)




