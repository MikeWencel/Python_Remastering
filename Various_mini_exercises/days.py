#Dni tygodnia - if, else
#Wartość wpisana przez użytkownika w postaci liczby ma wypisać dzień tygodnia


def days_of_week():

    x = (int (input("Proszę wpisz liczbę od 1 do 7, aby wyświetlić odpowiedni dzień tygodnia\n")))

    if x == 1:
        print("Poniedziałek")
    elif x == 2:
        print("Wtorek")
    elif x == 3:
        print("Środa")
    elif x == 4:
        print("Czwartek")
    elif x == 5:
        print("Piątek")
    elif x == 6:
        print("Sobota")
    elif x == 7:
        print("Niedziela")
    else:
        print("Nie ma tylu dni tygodnia")

days_of_week()