def napisy():
    napis = "Ala ma kota."
    print(napis[0])
    print(napis[0:3])

    print(len(napis))

    napis = "\tWiersz1\nWiersz2\nWiersz3"
    print(napis)
    napis = r"\tWiersz1\nWiersz2\nWiersz3"
    print(napis)
    napis = """Ala
ma
kota."""
    print(napis)

    print("a" < "b")
    print("aa" < "aaa")

    napis = "Ala ma kota."
    print(napis.lower())
    print(napis.upper())

    napis = "\t \n Napis ciekawy bardzo \n \t"
    print(napis.strip())

    napis = "wyraz, inny wyraz i jeszcze inny wyraz"
    print(napis.count("wyraz "))

    napis = napis.replace("wyraz", "WYRAZ")
    print(napis)

    lista_napisów = ["Ala", "ma", "kota"]
    print(" ".join(lista_napisów))

    napis = "Ala ma kota"
    print(napis.split(" "))

    napis = "Napis \" napis"
    print(napis)
    
if __name__ == "__main__":
    napisy()