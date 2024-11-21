# input
# x = int(input("Enter number: "))
# print(x)
x = 23

#if statement
if x % 2 == 0:
    print("Even")
else: 
    print("Odd")


if x > 0:
    print("Positive Number")
    if x % 7 == 0:
        print("Multiplication of 7")
    else:
        print("Not multiplication of 7" )
else:
    print("Negative Number")

#if-elif-else statement
x = 3
y = 4 

if x == y:
    print("Number are equal")
elif x > y:
    print("X is greater than y")
else:
    print("X is less than y")

marks = 100
if 0 <= marks <= 100:
    if marks >= 85:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 65:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print("Your grade is: ", grade)
else:
    print("Invalid input marks")

x = 11
result = "Even" if x % 2 == 0 else "Odd"
print(result)
