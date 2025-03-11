def bisekcja(f, a, b, con, val):
    if f(a) * f(b) < 0:
        raise ValueError("f(a) i f(b) muszą mieć przeciwne znaki")
    if con:
        for i in range(val):
            c = (a + b) / 2
            if abs(f(c)) == 0:
                return c, (i + 1)
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        raise ValueError("Nie znaleziono rozwiązania w {} iteracjach".format(val))
    else:
        i = 0
        while abs(a - b) > val:
            i += 1
            c = (a + b) / 2
            if abs(f(c)) < val:
                return c, i
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

# wykazac jak metoda sie zachowuje, nie koniecznie jaki jest dokladny wynik,
# czyli w sprawozdaniu damy wnioski typu "metoda x jest szybsza od y"