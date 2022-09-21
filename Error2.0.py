from unicodedata import name


def divide(DI, DV):
    if DV == 0:
        raise ZeroDivisionError("Divisor cannot be 0!!!")
    
    return DI / DV



students = [
    {"name": "Bob", "grades": [75, 85]},
    {"name": "Smith", "grades": [50, 65]},
    {"name": "John", "grades": []},
    {"name": "Tracey", "grades": [95, 85]},
]


try:
    for student in students:
        name =student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("ALL STUDENT AVERAGES CALCULATED")
finally:
    print("END OF STUDENT AVERAGE CALCULATION")