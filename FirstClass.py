def divide(DI, DV):
    if DI == 0:
        raise ZeroDivisionError("Divisor cannot be 0")

    return DI / DV

def multiplicate(M1, M2):
    return M1 * M2


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)
