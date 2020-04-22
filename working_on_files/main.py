plik_testowy = open('plik.txt')

try:
    tekst = plik_testowy.read()
finally:
    plik_testowy.close()

print(tekst)

plik_dwa = open('pliczek','w')
plik_dwa.write("To jest nowa treść")
plik_dwa.close()

pliczek_drugi = open('pliczek')

try:
    tekst = pliczek_drugi.read()
finally:
    pliczek_drugi.close()

print(tekst)