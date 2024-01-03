import math

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

num1 = get_float_input("Enter the side a of the triangle: ")
num2 = get_float_input("Enter the side b of the triangle: ")
num3 = get_float_input("Enter the side c of the triangle: ")

s = (num1 + num2 + num3) / 2
area = math.sqrt(s * (s - num1) * (s - num2) * (s - num3))

print(f"The area of the triangle is {area:.2f}")