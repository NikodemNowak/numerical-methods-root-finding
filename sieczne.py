from horner import horner

def sieczne(f, a, b, con, val, *args):
    global c
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
            is_ok, c = calculate(f, a, b, czy_wielomian, *args)

            if not is_ok:
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
        while abs(a - b) >= val:
            licznik_przejsc += 1

            is_ok, c = calculate(f, a, b, czy_wielomian, *args)

            if not is_ok:
                return False, c, (licznik_przejsc + 1)

            # Oblicz wartość funkcji w punkcie c
            if czy_wielomian:
                fc = horner(c, args[0], args[1])
            else:
                fc = f(c)

            # Sprawdź czy wartość bezwzględna funkcji w punkcie c jest prawie zerowa
            if abs(fc) <= 0.0001:
                return True, c, (licznik_przejsc + 1)

            # Przesuń punkty a i b
            a, b = b, c

        return False, c, licznik_przejsc

def calculate(f, a, b, czy_wielomian, *args):
    if czy_wielomian:
        f_a = horner(a, args[0], args[1])
        f_b = horner(b, args[0], args[1])
    else:
        f_a = f(a)
        f_b = f(b)

    # Sprawdź czy mianownik ze wzrou jest różny od zera
    if abs(f_b - f_a) < 1e-12:
        print("Ostrzeżenie: Mały mianownik - ryzyko błędu numerycznego")
        return False, b

    # Oblicz punkt c na podstawie punktów a i b
    return True, b - f_b * (b - a) / (f_b - f_a)