tab = [1,2,3,4,5,6,7,8]

print("****Zwykła tablica od 1 do 8***")
for x in tab:
    print(x)

print("****Tablica range do 5 'UWAGA CHODZI O INDEKS!! ****")
for x in range(5):
    print(x)


print("****Tablica range (3,6) 'UWAGA CHODZI O INDEKS!! ****")
for x in range(3,6):
    print(x)


print("****Pętla while, kończy się jeśli będzie <= 10 ****")

counter = 0

while counter <= 10:
    print(counter)
    counter += 1

counter = 0

print("****Pętla while TRUE, kończy się jeśli będzie jeśli będzie licznik będize >= 5 ****")

while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break

for x in range(51):
    if x % 2 == 0:
        print(x,"jest liczbą parzystą")
    else:
        print(x,"nie jest liczbą parzystą")


