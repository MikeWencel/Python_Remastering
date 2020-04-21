x = (int(input("Podaj liczbę dla jakiej obliczymy silnię\n")))

def fact(x):
    sum = 1
    for i in range(1,x+1):
        sum = i * sum
        print(sum)


fact(x)