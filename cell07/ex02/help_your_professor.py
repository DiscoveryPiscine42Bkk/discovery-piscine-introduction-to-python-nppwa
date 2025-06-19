def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "c": 2,
    "a": 0,
    "k": 0,
    "e": 7
}

class_C = {
    "w": 20,
    "a": 15,
    "x": 12
}

print(f"Average for class B: {average(class_B)}.")
print(f"Average for class C:{average(class_C)}.")