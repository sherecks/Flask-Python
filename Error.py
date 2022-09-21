def divide(DI, DV):
    if DV == 0:
        raise ZeroDivisionError("Divisor cannot be 0!!!")
    
    return DI / DV




Notas = []


print("Welcome to the program")

try:
    average = divide(sum(Notas), len(Notas))
except ZeroDivisionError as e:
    print("There are no grades yet in yout list.")
else:
    print(f"The Average grade is {average}!!!")