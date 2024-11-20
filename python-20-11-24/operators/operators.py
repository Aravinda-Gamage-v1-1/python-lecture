#Arithmetic operators
y = 7 / 2
print(y) #3.5
y = 9 // 4
print(y) #2

y = 7 % 3
print(y) #1

#Assign operators
x = 5
x += 5
print(x) #10
x *= 5
print(x) #50

#Comparison operators
x = 5
y = 6
print(x == y) #False
print(x != y) #True

#Logical operators
x = 5
y = 6
print(x < 10 and y > 8)
print(x < 10 or y > 8)
print(not y > 8)

#Identity operators
x = 9
y = 9
print(x is y)
print(x is not y)

#Membership operators
my_list_1 = [8, 10, 12, 13, 15]
print(10 in my_list_1) #True
print(11 in my_list_1) #False

#Bitwise operators
x = 5
y = 10
print(x & y) #0
print(x | y) #15
print(x ^ y) #15
print(~x) #-6