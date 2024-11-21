fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)    #apple 
                    #banana 
                    #orange


numbers_1 = [7, 5, 8, 4, 9, 12]
numbers_2 = []
for number in numbers_1:
    numbers_2.append(number**2)

print(numbers_2) #[49, 25, 64, 16, 81, 144]


#input = int(input("Input number: "))
input = 12
square_number = []
for num in range(1, input + 1):
    square_number.append(num**2)

print(square_number) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]


numbers = [2, 12, 9, 8]
for num in range(1, 10 + 1):
    print(num)  #1 
                #2 
                #3 
                #4
                #5 
                #6 
                #7
                #8 
                #9


result = [num*num for num in numbers]
print(result) #[4, 144, 81, 64]

result = [num**2 for num in numbers if num >= 0]
print(result)

input = 13
while input > 0:
    