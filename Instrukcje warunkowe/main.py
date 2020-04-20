x = 2


#Kiedy jest prawda
print(x == 2)
print(x != 3)

#Kiedy jest fałsz
print(x == 3)

print(x != 2)

imie = "Michał"


wiek = 33

if imie == "Michał" and wiek == 33:
    print("Wszystko się zgadza jego imię to", imie,",a wiek ",wiek)
else:
    print("Nie zgadza się zupełnie, jego imię to", imie, ",a wiek ",wiek)

if imie == "Michał" or imie == "Jan":
    print("On ma na imię albo,",imie, "albo Jan")

#Sprawdzamy czy dany obiekt znajduje się tablicy

tablice_imion = ["Michał","Robert","Tadeusz"]

name = "Michał"

if name in tablice_imion:
    print("Tak w tej tablicy jest osoba o imieniu", name)
else:
    print("Nie ma tutaj osoby o imieniu:", name)

temperature = 15
weather = "Sunny"

print("When it's",weather,"and",temperature,"deegres")

if temperature <= 20 and weather == "Sunny":
    print("You can wear T-Shirt, cause it's",temperature,"and it's sunny")
elif temperature <= 20 and weather != "Sunny":
    print("You can wear Jacket, cause it's", temperature,"and it can rain")
elif temperature > 20 and temperature >= 10 and weather == "Sunny":
    print("Please wear T-shirt, cause it's",temperature,"and it's sunny")
elif temperature > 20 and temperature >= 10 and weather != "Sunny":
    print("Please wear hoodie, cause it's", temperature,"and it can rain")
else:
    print("Please wear jacket cause it's",temperature)

print("***** DRY CODE *****")
#Remastering my own code

if weather != "Sunny":
    print("Take a Jacket and umbrella")
elif temperature >= 20:
    print("You don't have to take hoodie")
elif temperature >= 10 and temperature < 20:
    print("Take Hoodie")
else:
    print("Take Jacket")

#Checking tables

x = [1,2,3]
y = [1,2,3]

print(x == y)
print(x is y)

tab = [1,2,3]
tab2 = ["a","b",tab]

print(tab == tab2[2])
print(tab is tab2[2])

print(not False)
print(not False == False)