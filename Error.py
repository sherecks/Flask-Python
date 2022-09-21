def divide(DI, DV):
    if DV == 0:
        print("Divisor cannot be 0")
        return
    
    return DI / DV




Notas = [100, 40, 64, 75, 68]


print("Welcome to the program")

average = divide(sum(Notas), len(Notas))


print(f"The Average grade is {average}!!!")