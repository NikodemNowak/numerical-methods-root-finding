from horner import horner

def sieczne(f, a, b, con, val, *args):
    licznik_przejsc = -1
    czy_wielomian = len(args) > 0

    if czy_wielomian:
        fa = horner(a, args[0], args[1])
        fb = horner(b, args[0], args[1])
    else:
        fa = f(a)
        fb = f(b)

    if fa * fb > 0:
        raise ValueError("f(a) i f(b) muszą mieć przeciwne znaki")

    # Dla ilości iteracji
    if con == 't':
        for i in range(val):
            licznik_przejsc = i

            # Oblicz punkt c na podstawie punktów a i b
            isOk, c = calculate(f, a, b, czy_wielomian, *args)

            if not isOk:
                return False, c, (i + 1)

            if czy_wielomian:
                fc = horner(c, args[0], args[1])
            else:
                fc = f(c)

            if abs(fc) <= 0.0001:
                return True, c, (i + 1)

            a, b = b, c

    # Dla dokładności
    else:
        while True:
            licznik_przejsc += 1

            isOk, c = calculate(f, a, b, czy_wielomian, *args)

            if not isOk:
                return False, c, (licznik_przejsc + 1)

            # Oblicz wartość funkcji w punkcie c
            if czy_wielomian:
                fc = horner(c, args[0], args[1])
            else:
                fc = f(c)

            # Sprawdź czy wartość bezwzględna funkcji w punkcie c jest mniejsza od wartości val
            if abs(fc) < val:
                return True, c, (licznik_przejsc + 1)

            # Przesuń punkty a i b
            a, b = b, c

def calculate(f, a, b, czy_wielomian, *args):
    if czy_wielomian:
        f_a = horner(a, args[0], args[1])
        f_b = horner(b, args[0], args[1])
    else:
        f_a = f(a)
        f_b = f(b)

    if abs(f_b - f_a) < 1e-12:
        print("Ostrzeżenie: Mały mianownik - ryzyko błędu numerycznego")
        return False, b

    return True, b - f_b * (b - a) / (f_b - f_a)