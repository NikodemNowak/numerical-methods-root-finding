import math
from bisekcja import bisekcja
import matplotlib.pyplot as plt
import numpy as np

# 1. Baza predefiniowanych funkcji
FUNKCJE = {
    1: {"nazwa": "x^3 - 2e^x + 5",
        "f": lambda x: x ** 3 - 2 * math.exp(x) + 5,
        "pochodna": lambda x: 3 * x ** 2 - 2 * math.exp(x),
        "xrange": (-3, 4),
        "yrange": (-30, 10)},

    2: {"nazwa": "sin(x) * ln(x+1)",
        "f": lambda x: math.sin(x) * math.log(x + 1),
        "pochodna": lambda x: math.cos(x) * math.log(x + 1) + math.sin(x) / (x + 1),
        "xrange": (-4, 4),
        "yrange": (-50, 1)},

    3: {"nazwa": "e^{cos(2x)}",
        "f": lambda x: math.exp(math.cos(2 * x)),
        "pochodna": lambda x: -2 * math.sin(2 * x) * math.exp(math.cos(2 * x)),
        "xrange": (-4, 4),
        "yrange": (-50, 1)},

    4: {"nazwa": "2^x + x^2 - tan(x)",
        "f": lambda x: 2 ** x + x ** 2 - math.tan(x),
        "pochodna": lambda x: (2 ** x) * math.log(2) + 2 * x - (1 / math.cos(x)) ** 2,
        "xrange": (-4, 4),
        "yrange": (-50, 1)},
}

def funkcja_menu():
    print("Wybierz funkcję:")
    for i in FUNKCJE:
        print(f"{i}. {FUNKCJE[i]['nazwa']}")
    while True:
        try:
            wybor = int(input("Wybierz numer funkcji: "))
            if wybor in FUNKCJE:
                return FUNKCJE[wybor]
            raise ValueError
        except ValueError:
            print("Błędny wybór, spróbuj ponownie!")

def wykres(f,fx, fy):
    # Stwórz 500 punktów w wybranym zakresie
    x = np.linspace(-5, 5, 500)

    # Oblicz wartości z obsługą błędów
    y = []
    for xi in x:
        try:
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
    plt.show()


def przedzial_menu(f):
    while True:
        try:
            a = float(input("Podaj początek przedziału: "))
            b = float(input("Podaj koniec przedziału: "))
            if a != b and f(a) * f(b) < 0:
                return a, b
        except ValueError:
            print("Dla podanych parametrów wartość funkcji musi mieć różne znaki, spróbuj ponownie!")


def opcja_menu():
    con = ''
    while con not in ['t', 'n']:
        try:
            con = input("Czy chcesz podać liczbę iteracji? (t/n): ").lower()
            if con not in ['t', 'n']:
                raise ValueError
        except ValueError:
            print("Błędny wybór, spróbuj ponownie!")
    if con == 't':
        val = int(input("Podaj liczbę iteracji: "))
    else:
        val = float(input("Podaj dokładność: "))
    return con, val


def main():
    f = funkcja_menu()
    print(f"Wybrana funkcja: {f['nazwa']}")
    wykres(f['f'], f['xrange'], f['yrange'])
    a, b = przedzial_menu(f['f'])
    con, val = opcja_menu()
    try:
        wynik, iteracje = bisekcja(f['f'], a, b, con, val)
        print(f"Znaleziono rozwiązanie: {wynik} w {iteracje} iteracjach")
    except ValueError as e:
        print(e)

main()