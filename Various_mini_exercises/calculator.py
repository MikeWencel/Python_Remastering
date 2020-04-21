name = (str(input("Jak masz na imię dobry ludziu\n")))

print("To jest prosty kalkulator")


number_one = (int(input("Podaj pierwszą liczbę\n")))
doing = (str(input("Co chcesz zrobić? Naciśnij odpowiedni symbol na klawiaturze '+', '-', '/', '*'\n")))
number_two = (int(input("Podaj drugą liczbę\n")))


if doing == "*":
    print(number_one * number_two)
elif doing == "+":
    print(number_one + number_two)
elif doing == "/":
    print(number_one / number_two)
elif doing == "-":
    print(number_one - number_two)
else:
    print("Podałeś/aś zły typ działania")
