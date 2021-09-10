import math


def zad_petle():
    # liczby parzyste do 100
    i = 0
    while i <=100:
        print(i, end=", ")
        i += 2
    # wersja for
    print("\n----")
    for i in range(0,101):
        if i % 2 == 0:
            print(i, end=", ")
    print("\n----")
    for i in range(0, 101, 2):
        print(i, end=", ")

    #wypisz potęgi 2 do 256
    print("\n----")
    potega = 1
    while potega <= 256:
        print(potega, end=", ")
        potega *= 2
    # Spr czy liczba pierwsza
    print("\n----")
    liczba = 31
    czy_pierwsza = True
    #for i in range(2, liczba):
    #optymalizacja
    for i in range(3, int(math.sqrt(liczba))+1, 2):
        if liczba % i == 0:
            print("To nie jest liczba pierwsza")
            czy_pierwsza = False
            break

    if czy_pierwsza:
        print("To jest liczba pierwsza")

if __name__ == "__main__":
    zad_petle()