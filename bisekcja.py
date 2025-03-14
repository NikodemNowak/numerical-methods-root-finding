from horner import horner

def bisekcja(f, a, b, con, val, *args):
    c = 0
    j = -1
    if len(args) > 0:
        fa = horner(a, args[0], args[1])
        fb = horner(b, args[0], args[1])
    else:
        fa = f(a)
        fb = f(b)
    if fa * fb > 0:
        raise ValueError("BISEKCJA: f(a) i f(b) muszą mieć przeciwne znaki")

    # Dla ilości iteracji
    if con == 't':
        for i in range(val):
            c = (a + b) / 2

            if len(args) > 0:
                fc = horner(c, args[0], args[1])
            else:
                fc = f(c)

            if abs(fc) <= 0.0001:
                return True, c, (i + 1)

            if len(args) > 0:
                fa = horner(a, args[0], args[1])
                fc = horner(c, args[0], args[1])
            else:
                fa = f(a)
                fc = f(c)

            if fa * fc < 0:
                b = c
            else:
                a = c
            j = i

    # Dla dokładności
    else:
        while abs(a - b) > val:
            j += 1
            c = (a + b) / 2

            if len(args) > 0:
                fa = horner(a, args[0], args[1])
                fc = horner(c, args[0], args[1])
            else:
                fa = f(a)
                fc = f(c)

            if abs(fc) < val:
                return True, c, j
            if fa * fc < 0:
                b = c
            else:
                a = c
    return False, c, j

# wykazac jak metoda sie zachowuje, nie koniecznie jaki jest dokladny wynik,
# czyli w sprawozdaniu damy wnioski typu "metoda x jest szybsza od y"