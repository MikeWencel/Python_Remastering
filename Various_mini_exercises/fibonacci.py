numbers = [0,1]

def fib(numbers,dlugosc_ciagu):
    newNumber = 0
    for i in range(dlugosc_ciagu):
        #dodaje dwa ostatnie wyrazy ciągu, który stworzyłem powyżej
        newNumber = numbers[-1] + numbers[-2]
        #dodaje do ciągu nowy numer
        numbers.append(newNumber)
        print(newNumber)

fib(numbers,4)