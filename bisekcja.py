from horner import horner

def bisekcja(f, a, b, con, val, *args):

    c = 0
    licznik_przejsc = -1

    czy_wielomian = len(args) > 0

    def wartosc_funkcji_w_punkcie(x):
        if czy_wielomian:
            return horner(x, args[0], args[1])
        else:
            return f(x)

    fa = wartosc_funkcji_w_punkcie(a)
    fb = wartosc_funkcji_w_punkcie(b)

    if fa * fb > 0:
        raise ValueError("BISEKCJA: f(a) i f(b) muszą mieć przeciwne znaki")

    # Dla ilości iteracji
    if con == 't':
        for i in range(val):
            c = (a + b) / 2

            fc = wartosc_funkcji_w_punkcie(c)

            if abs(fc) <= 0.0001:
                return True, c, (i + 1)

            fa = wartosc_funkcji_w_punkcie(a)
            fc = wartosc_funkcji_w_punkcie(c)

            if fa * fc < 0:
                b = c
            else:
                a = c

            licznik_przejsc = i

    # Dla dokładności
    else:
        while abs(a - b) > val:
            licznik_przejsc += 1
            c = (a + b) / 2

            fa= wartosc_funkcji_w_punkcie(a)
            fc = wartosc_funkcji_w_punkcie(c)

            if abs(fc) < val:
                return True, c, licznik_przejsc
            if fa * fc < 0:
                b = c
            else:
                a = c
    return False, c, licznik_przejsc

# wykazac jak metoda sie zachowuje, nie koniecznie jaki jest dokladny wynik,
# czyli w sprawozdaniu damy wnioski typu "metoda x jest szybsza od y"