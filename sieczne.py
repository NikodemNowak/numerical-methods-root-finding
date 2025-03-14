from horner import horner

def sieczne(f, a, b, con, val, *args):
    j = -1
    czy_wielomian = len(args) > 0

    if czy_wielomian:
        fa = horner(a, args[0], args[1])
        fb = horner(b, args[0], args[1])
    else:
        fa = f(a)
        fb = f(b)

    if fa * fb > 0:
        raise ValueError("f(a) i f(b) muszą mieć przeciwne znaki")
    if con == 't':
        for i in range(val):
            j = i

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
    else:
        while abs(a - b) > val:
            j += 1

            isOk, c = calculate(f, a, b, czy_wielomian, *args)

            if not isOk:
                return False, c, (j + 1)

            if abs(f(c)) < val:
                return True, c, (j + 1)

            a, b = b, c

    return False, b, j

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