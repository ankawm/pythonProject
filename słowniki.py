def slowniki():

    baza_danych_polakow = {"89120612584": {"Jan", "Kowalski", 29},
                           "95092200000": {"Ania", "Nowak", 23},
                           "98122422222": {"Adam", "Mickiewicz", 220}
                           }
    print(baza_danych_polakow)
    print("89120612584" in baza_danych_polakow)
    print("89120612584" not in baza_danych_polakow)

    print(baza_danych_polakow["89120612584"])
    print(baza_danych_polakow.get("89120612584", "wartosc domyślna"))

    baza_danych_polakow["88081244444"]= ["Magda", "K", 30]
    print(baza_danych_polakow)

    del baza_danych_polakow["88081244444"]
    print(baza_danych_polakow)

    for klucz in baza_danych_polakow.keys():
        print(klucz)

    for wartosc in baza_danych_polakow.values():
        print(wartosc)

    for klucz, wartosc in baza_danych_polakow.items():
        print(klucz)
        print(wartosc)
        print("---")


if __name__ == "__main__":
    slowniki()