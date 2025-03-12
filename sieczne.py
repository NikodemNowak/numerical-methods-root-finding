def sieczne(f, a, b, con, val):
    j = -1
    if f(a) * f(b) > 0:
        raise ValueError("f(a) i f(b) muszą mieć przeciwne znaki")
    if con == 't':
        for i in range(val):
            j = i

            isOk, c = calculate(f, a, b)

            if not isOk:
                return False, c, (i + 1)

            if f(c) == 0:
                return True, c, (i + 1)

            a, b = b, c
    else:
        while abs(a - b) > val:
            j += 1

            isOk, c = calculate(f, a, b)

            if not isOk:
                return False, c, (j + 1)

            if abs(f(c)) < val:
                return True, c, (j + 1)

            a, b = b, c
    return False, b, j

def calculate(f, a, b):
    f_a = f(a)
    f_b = f(b)

    if abs(f_b - f_a) < 1e-12:
        print("Ostrzeżenie: Mały mianownik - ryzyko błędu numerycznego")
        return False, b

    return True, b - f_b * (b - a) / (f_b - f_a)