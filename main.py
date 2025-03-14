import math
from bisekcja import bisekcja
import matplotlib.pyplot as plt
import numpy as np
from sieczne import sieczne
from horner import horner

# 1. Baza predefiniowanych funkcji
FUNKCJE = {
    1: {"nazwa": "x^3 - 2x^2 + 1",
        "f": lambda x: x ** 3 - 2 * x ** 2 + 1,
        "xrange": (-3, 4),
        "yrange": (-5, 5),
        "wspolczynniki": (1, -2, 0, 1)},

    2: {"nazwa": "sin(x) * ln(x+1)",
        "f": lambda x: math.sin(x) * math.log(x + 1),
        "xrange": (-1, 4),
        "yrange": (-2, 3)},

    3: {"nazwa": "e^{cos(2x) - 1}",
        "f": lambda x: math.exp(math.cos(2 * x)) - 1,
        "xrange": (-4, 4),
        "yrange": (-1, 2)},

    4: {"nazwa": "2^x - 2sin(x) - 2",
        "f": lambda x: 2 ** x - 2 * math.sin(x) - 2,
        "xrange": (-3, 3),
        "yrange": (-3, 4)},
}

def funkcja_menu():
    print("Wybierz funkcję:")
    for i in FUNKCJE:
        print(f"{i}. {FUNKCJE[i]['nazwa']}")
    while True:
        try:
            wybor = int(input("Wybierz numer funkcji: "))
            if wybor in FUNKCJE:
                return FUNKCJE[wybor], wybor
            raise ValueError
        except ValueError:
            print("Błędny wybór, spróbuj ponownie!")

def wykres(f, fx, fy, wybor, *args):
    # Stwórz 5000 punktów w wybranym zakresie
    x = np.linspace(fx[0], fx[1], 5000)

    # Oblicz wartości z obsługą błędów
    y = []
    for xi in x:
        try:
            if wybor == 1:
                y.append(horner(xi, FUNKCJE[wybor]['wspolczynniki'], len(FUNKCJE[wybor]['wspolczynniki'])))
            else:
                y.append(f(xi))
        except:
            y.append(np.nan)  # Oznacz miejsca nieokreślone

    plt.figure(figsize=(12,6))
    plt.plot(x, y, 'b-', label="Funkcja")
    plt.xlim(fx[0], fx[1])
    plt.ylim(fy[0], fy[1])
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.title("Podgląd funkcji - wybierz przedział [a,b] na podstawie wykresu")
    plt.grid(True)

    if len(args) > 0:
        plt.title("Podgląd funkcji z zaznaczonymi punktami i wybranym przedziałem")
        plt.axvline(args[0], color='red', linestyle='--', label='Punkt startowy')
        plt.axvline(args[1], color='red', linestyle='--', label='Punkt końcowy')
        plt.xlim(args[0]-0.1, args[1]+0.1)
        plt.ylim(-1, 1)
        plt.plot(args[2], args[3], marker='o', markersize=10, markerfacecolor='none', markeredgecolor='red',
                 linestyle='None', label='Point 1')
        plt.plot(args[4], args[5], marker='s', markersize=10, markerfacecolor='none', markeredgecolor='green',
                 linestyle='None', label='Point 2')


    plt.show()


def przedzial_menu(f, wybor):
    while True:
        try:
            print("\nWybierz przedział [a,b] taki, że f(a) i f(b) mają różne znaki")
            a = float(input("Podaj początek przedziału (a): "))
            b = float(input("Podaj koniec przedziału (b): "))

            if a >= b:
                print("Błąd: Początek przedziału (a) musi być mniejszy niż koniec (b).")
            else:
                if wybor == 1:
                    fa = horner(a, FUNKCJE[wybor]['wspolczynniki'], len(FUNKCJE[wybor]['wspolczynniki']))
                    fb = horner(b, FUNKCJE[wybor]['wspolczynniki'], len(FUNKCJE[wybor]['wspolczynniki']))
                else:
                    fa = f(a)
                    fb = f(b)

                if fa * fb < 0:
                    print(f"OK: f({a}) = {fa:.4f}, f({b}) = {fb:.4f}")
                    return a, b
                else:
                    print(f"Błąd: Funkcja musi mieć różne znaki na końcach przedziału.")
                    print(f"f({a}) = {fa:.4f}, f({b}) = {fb:.4f}")
                    print("Spróbuj wybrać inny przedział na podstawie wykresu.")
        except ValueError as e:
            print(f"Błąd: {e}. Spróbuj ponownie.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}. Spróbuj inny przedział.")


def opcja_menu():
    con = ''
    val = 0
    while con not in ['t', 'n']:
        try:
            con = input("Czy chcesz podać liczbę iteracji? (t/n): ").lower()
            if con not in ['t', 'n']:
                raise ValueError
        except ValueError:
            print("Błędny wybór, spróbuj ponownie!")
    if con == 't':
        while val <= 0:
            try:
                val = int(input("Podaj liczbę iteracji: "))
                if val <= 0:
                    raise ValueError
            except ValueError:
                print("Wartość musi być dodatnia!")
    else:
        while val <= 0:
            try:
                val = float(input("Podaj dokładność: "))
                if val <= 0:
                    raise ValueError
            except ValueError:
                print("Wartość musi być dodatnia!")
    return con, val


def main():
    f, wybor = funkcja_menu()
    print(f"Wybrana funkcja: {f['nazwa']}")
    wykres(f['f'], f['xrange'], f['yrange'], wybor)
    a, b = przedzial_menu(f['f'], wybor)
    con, val = opcja_menu()
    try:

        if wybor == 1:
            bi_sukces, bi_wynik, bi_iteracje = bisekcja(f['f'], a, b, con, val, f['wspolczynniki'], len(f['wspolczynniki']))
            si_sukces, si_wynik, si_iteracje = sieczne(f['f'], a, b, con, val, f['wspolczynniki'], len(f['wspolczynniki']))
        else:
            bi_sukces, bi_wynik, bi_iteracje = bisekcja(f['f'], a, b, con, val)
            si_sukces, si_wynik, si_iteracje = sieczne(f['f'], a, b, con, val)

        if bi_sukces:
            print(f"BISEKCJA: Znaleziono rozwiązanie: {bi_wynik} w {bi_iteracje + 1} iteracjach")
        else:
            print(f"BISEKCJA: Nie znaleziono rozwiązania w {bi_iteracje + 1} iteracjach, zwrócono ostatnią wartość: {bi_wynik}")

        if si_sukces:
            print(f"SIECZNE: Znaleziono rozwiązanie: {si_wynik} w {si_iteracje + 1} iteracjach")
        else:
            print(f"SIECZNE: Nie znaleziono rozwiązania w {si_iteracje + 1} iteracjach, zwrócono ostatnią wartość: {si_wynik}")

        # Nowy wykres z zaznaczonymi punktami
        wykres(f['f'], f['xrange'], f['yrange'], wybor, a, b, bi_wynik, f['f'](bi_wynik), si_wynik, f['f'](si_wynik))

    except ValueError as e:
        print(e)

main()