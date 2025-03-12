def bisekcja(f, a, b, con, val):
    c = 0
    j = -1
    if f(a) * f(b) > 0:
        raise ValueError("BISEKCJA: f(a) i f(b) muszą mieć przeciwne znaki")
    if con == 't':
        for i in range(val):
            c = (a + b) / 2
            if abs(f(c)) == 0:
                return True, c, (i + 1)
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            j = i
    else:
        while abs(a - b) > val:
            j += 1
            c = (a + b) / 2
            if abs(f(c)) < val:
                return True, c, j
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
    return False, c, j

# wykazac jak metoda sie zachowuje, nie koniecznie jaki jest dokladny wynik,
# czyli w sprawozdaniu damy wnioski typu "metoda x jest szybsza od y"