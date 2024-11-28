def calculate_circumference(width, height):
    circumference = width * height
    print(circumference) #1500

calculate_circumference(30, 50)

def calculate_area(radius):
    area = 3.14159*radius*radius
    print(area) #153.93791

calculate_area(7)

def add_number(a, b = 5):
    return a + b

print(add_number(3)) #8
print(add_number(5, 8)) #13
print(add_number(b=6, a=2)) #8


def calculate_cost(price, qty, discount = 0, tax = 0):
    step1 = price * qty
    step2 = step1 - (step1 * discount / 100)
    step3 = step2 + (step2 * tax / 100)
    return step3

print(calculate_cost(100, 10, 10, 5)) #945.0