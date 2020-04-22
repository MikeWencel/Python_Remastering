import random

answer = int(input("Podaj ile liczb wylosować\n"))
max_numbers = int(input("Podaj zakres liczb\n"))

myList = []
i = 0
while i < max_numbers:
    number = random.randint(1,max_numbers)
    if mylist.append(number) == 0:
        myList.append(number)
        i = i + 1

print(mylist)

