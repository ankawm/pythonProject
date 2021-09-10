def zad_modul_I():
    i = 0
    kolejne_działanie= "t"

    while i >= 0:
        if kolejne_działanie == "n":
            break
        else:
            x = float(input("Podaj pierwsza liczbę: "))
            operator = input("Podaj operator kalkulatora (+,-,*,/,//,%): ")
            y = float(input("Podaj drugą liczbę: "))
            if operator == "+":
                wynik = x + y
            elif operator == "-":
                wynik = x - y
            elif operator == "*":
                wynik = x * y
            elif operator == "/":
                wynik = x / y
            elif operator == "//":
                wynik = x // y
            elif operator == "%":
                wynik = x % y
            i += 1
            print(f'Wynik działania x {operator} y = {wynik}')
            kolejne_działanie = input("Wykonujemy kolejne działanie (t/n): ")


if __name__ == "__main__":
    zad_modul_I()