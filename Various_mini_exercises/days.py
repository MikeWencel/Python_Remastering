#Dni tygodnia - if, else
#Wartość wpisana przez użytkownika w postaci liczby ma wypisać dzień tygodnia

name = (str(input("Jak masz na imię?\n")))

print(name,"kilka pytań do Ciebie")

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


def letter_days_of_month():
    month = (str(input("Napisz słownie nazwę miesiąca, by wyświetlić nazwę i ilość dnia \n")))
    month = month.upper()

    if month == "STYCZEŃ":
        print("Styczeń ma 31 dni")
    elif month == "LUTY":
        print("Luty ma 28 dni")
    elif month == "MARZEC":
        print("Marzec ma 31 dni")
    elif month == "KWIECIEŃ":
        print("Kwiecień ma 30 dni")
    elif month == "STYCZEŃ":
        print("Maj ma 31 dni")
    elif month == "STYCZEŃ":
        print("Czerwiec ma 30 dni")
    elif month == "Lipiec":
        print("Lipiec ma 31 dni")
    elif month == "SIERPIEŃ":
        print("Sierpień ma 31 dni")
    elif month == "WRZESIEŃ":
        print("Wrzesień ma 30 dni")
    elif month == "PAŹDZIERNIK":
        print("Październik ma 31 dni")
    elif month == "LISTOPAD":
        print("Listopad ma 30 dni")
    elif month == "Grudzień":
        print("Grudzień ma 31 dni")
    else:
        print("Wpisałeś zły miesiąc")

letter_days_of_month()