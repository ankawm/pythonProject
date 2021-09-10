def warunki():
    wiek = 10
    if wiek >= 18:
        print("Osoba jest pełnoletnia")
        print("Drugi wiersz w Ifie!")
    else:
        print("Osoba jest niepełnoletnia")
        print("Jesteśmy w else")
    print("To wykona się zawsze!")

    wiek = 22
    if wiek >= 21:
        print("Możesz kupić alko i broń")
    elif wiek >= 18:
        print("Możesz kupić alko")
    elif wiek >= 15:
        print("Możesz uprawiać sex")
    else:
        print("Jesteś bardzo młody ciesz się życiem")

if __name__ == "__main__":
    warunki()