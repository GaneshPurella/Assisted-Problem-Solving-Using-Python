def find_common(a, b):
    return list(set(a) & set(b))


# -------- USER INPUT --------
a = input("Enter list A elements (separated by space): ").split()
b = input("Enter list B elements (separated by space): ").split()

common = find_common(a, b)

print("Common Elements:", common)