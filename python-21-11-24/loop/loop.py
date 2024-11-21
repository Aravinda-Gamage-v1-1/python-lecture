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
input1 = 12
square_number = []
for num in range(1, input1 + 1):
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
print(result) #[4, 144, 81, 64]


input1 = 10
square_number = []
temp_square = 1
count = 1
while temp_square <= input1:
    square_number.append(temp_square)
    count += 1
    temp_square = count * count

print(square_number) #[1, 4, 9]


my_list = [8, 9, 3, 0, 12, 15]
for item in my_list:
    if item == 0:
        break
    else:
        print(item) #8
                    #9
                    #3


my_list = [8, 9, 3, 0, 12, 15]
for item in my_list:
    if item == 0:
        continue
    else:
        print(item) #8
                    #9
                    #3
                    #12
                    #15


while True:
    num = int(input("Input number: "))
    if num != 0:
        print(num**2)   
    else:
        break


person = {
    "name" : "John",
    "age" : 25,
    "gender" : "Male"
}

for key, value in person.items():
    print(key, value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)