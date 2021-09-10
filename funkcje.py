def liniowa(x, a, b):
    return a * x + b
def potega(podstawa, wykladnik=2):
    #wykładnik ma wartość domyślną jak go nie podamy, to będzie 2
    i = 1
    wynik = 1
    while i <=wykladnik:
        wynik *= podstawa
        i +=1
    return wynik
#rekurencja
def silnia(n): # n!= n * (n-1)!, 0!=1
    if n == 0 :
        return 1
    return n * silnia(n-1)

def funkcje():
    x = 2
    a = 3
    print(liniowa(x, a, 5))
    print(liniowa(x, 1.5, 5))
    print(potega(2, 5))
    print(potega(5))
    print(silnia(5))
    #przykładowa funkcja liniowa
    # dane - agumenty
    # wartość szukana - to co funkcja zwróci
    # ciało - to co funk


if __name__ == "__main__":
    funkcje()