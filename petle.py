def petle():
    #for
    print("for")
    for i in range(0, 10):
        print(i)
    #while
    print("while")
    i = 0

    while i < 10:
        print(i)
        i += 1
    #średnia z paru liczb
    print("średnia ocen")

    liczba_ocen = int(input("podaj liczbę ocen, z których chcesz policzyć średnią: "))
    suma = 0
    for i in range(1,liczba_ocen+1):
        ocena = float(input(f'Podaj ocenę numer {i}: '))
        suma += ocena

    print(f'Suma: {suma}')
    print(f'Średnia: {suma/liczba_ocen}')

    print("średnia ocen while")

    suma = 0
    j = 1
    while j <= liczba_ocen:
        ocena = float(input(f'Podaj ocenę numer {j}: '))
        if ocena < 0:
            continue
        elif ocena > 100:
            break
        suma += ocena
        j += 1

    print(f'Suma: {suma}')
    print(f'Średnia: {suma / liczba_ocen}')


if __name__ == "__main__":
    petle()