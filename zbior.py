def zbior():

    zbior_pusty = set()
    print(zbior_pusty)

    zbior = {1,3,5}
    print(zbior)

    print(1 in zbior)
    print(1 not in zbior)

    zbior.add(2)
    print(zbior)

    zbior.discard(2)
    print(zbior)

    print({1,5,8}|{1,5,9}) #suma zbiorów
    print({1,5,8}-{1,5,9}) #róznica
    print({1, 5, 8} & {1, 5, 9})  # iloczyn


if __name__ == "__main__":
    zbior()