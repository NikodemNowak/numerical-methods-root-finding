from horner import horner

def sieczne(f, a, b, opcja_zakonczenia, wartosc_z_opcji, *args):

    c = 0
    licznik_przejsc = -1

    # Jeśli podano więcej argumentów to znaczy, że funkcja jest wielomianem
    czy_wielomian = len(args) > 0

    # Funkcja do obliczania wartości funkcji w danym punkcie
    def wartosc_funkcji_w_punkcie(x):
        if czy_wielomian:
            return horner(x, args[0], args[1])
        else:
            return f(x)

    fa = wartosc_funkcji_w_punkcie(a)
    fb = wartosc_funkcji_w_punkcie(b)

    # Sprawdź czy f(a) i f(b) mają przeciwne znaki
    if fa * fb > 0:
        raise ValueError("f(a) i f(b) muszą mieć przeciwne znaki")


    # Główna pętla
    if opcja_zakonczenia == 't':
        max_iterations = wartosc_z_opcji
        should_continue = lambda i: i < max_iterations
    else:
        max_iterations = float('inf')  # Teoretycznie nieskończona liczba iteracji
        should_continue = lambda _: abs(a - b) >= wartosc_z_opcji

    i = 0
    while should_continue(i):
        licznik_przejsc = i

        # Oblicz punkt c na podstawie punktów a i b
        czy_c_ok, c = oblicz_x_dla_c(wartosc_funkcji_w_punkcie, a, b)

        if not czy_c_ok:
            return False, c, (licznik_przejsc + 1)

        fc = wartosc_funkcji_w_punkcie(c)

        if max_iterations == float('inf'):
            if abs(fc) <= wartosc_z_opcji:
                return True, c, (licznik_przejsc + 1)
        else:
            if abs(fc) <= 0.0001:
                return True, c, (licznik_przejsc + 1)

        a, b = b, c
        i += 1

    return False, c, licznik_przejsc + 1


def oblicz_x_dla_c(wartosc_funkcji_w_punkcie, a, b):

    # Oblicz wartość funkcji w punktach a i b
    f_a = wartosc_funkcji_w_punkcie(a)
    f_b = wartosc_funkcji_w_punkcie(b)

    # Sprawdź czy mianownik ze wzrou jest różny od zera
    if abs(f_b - f_a) < 1e-12:
        print("Ostrzeżenie: Mały mianownik - ryzyko błędu numerycznego")
        return False, b

    # Oblicz punkt c na podstawie punktów a i b
    return True, b - f_b * (b - a) / (f_b - f_a)

