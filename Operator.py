def operator():
    x = 7
    y = 3
    suma = x + y
    print("Suma: " + str(suma))
    print(f'Suma: {suma}')

    roznica = x-y
    print(f'Roznica: {roznica}')

    iloczyn = x * y
    print(f'Iloczyn: {iloczyn}')

    iloraz = x / y
    print(f'Iloraz: {iloraz}')

    modulo = x % y
    print(f'Modulo: {modulo}')

    x += 3
    y *= 3
    print(f'x+3: {x}')
    print(f'y*3: {y}')

    print(f'x<y: {x<y}')
    print(f'2=2: {2==2}')
    print(f'x rożne od y: {x!=y}')

    wiek = 36
    czy_wiek_produkcyjny = 18 <= wiek <=65
    print(czy_wiek_produkcyjny)
    #logiczne
    #and
    #or
    #not



if __name__ == "__main__":
    operator()