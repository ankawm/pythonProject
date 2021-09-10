def srednia(liczby):
    suma = 0
    for i in range(0, len(liczby)):
        suma += liczby[i]
    return suma/len(liczby)

def srednia2(liczby):
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma/len(liczby)

def lista():
    lista = [1, False, "Napis"]
    print(lista)
    print(len(lista))

    lista.append(2.5+3.7j)
    print(lista)
    print(len(lista))

    lista.extend([97, 98, 99])
    print(lista)
    print(len(lista))

    lista.append([97,98,99])
    print(lista)
    print(len(lista))

    print(lista + [1, 2, 3])

    print([7, 8, 9]*3)

    print(lista[2])

    print(lista[-1])#przed ostatni element

    lista[1] = 66

    print(lista)

    print(lista[2:5]) #od 2 do 4 bez 5
    lista[2:5] = [98, 99, 100, 101, 102]

    print(lista)

    lista.insert(3, "Ala ma kota")
    print(lista)


    del lista[3]
    print(lista)

    liczby = [1,6,3,5,4,7]
    liczby.sort()
    print(liczby)
    liczby.reverse()
    print(liczby)

    print(srednia(liczby))
    print(srednia2(liczby))

if __name__ == "__main__":
    lista()