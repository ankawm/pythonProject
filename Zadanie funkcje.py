import math

def bmi(waga, wzrost):
    return waga/ (wzrost ** 2)

def pierwsza(liczba):
    czy_pierwsza = True
    if liczba % 2 == 0 and liczba > 2:
        print("To nie jest liczba pierwsza")
        czy_pierwsza = False
    else:
        for i in range (3, int(math.sqrt(liczba)+1),2):
            if liczba % i == 0:
                print("To nie jest liczba pierwsza")
                czy_pierwsza = False
                break
    return czy_pierwsza

def funkcje_zad():
    print("BMI:")
    print(bmi(73, 1.7))
    print("Czy pierwsza:")
    print(pierwsza(4))

if __name__ == "__main__":
    funkcje_zad()