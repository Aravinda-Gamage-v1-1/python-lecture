my_tuple_1 = ("apple", 8, "True", "apple", 5)
print(my_tuple_1[1]) #8
print(len(my_tuple_1)) #4
print(type(my_tuple_1)) #<class 'tuple'>


my_tuple_2 = ("rice")
print(type(my_tuple_2)) #<class 'str'>
my_tuple_2 = ("rice",)
print(type(my_tuple_2)) #<class 'tuple'>

print(my_tuple_1[-2]) #True

print(my_tuple_1[1:3]) #(8, 'True')
print(my_tuple_1[:4]) #('apple', 8, 'True', 'apple')
print(my_tuple_1[2:]) #('True', 'apple', 5)

print(my_tuple_1)
my_list_1 = list(my_tuple_1)
my_list_1[2] = 15
my_tuple_1 = tuple(my_list_1)
print(my_tuple_1) #('apple', 8, 15, 'apple', 5)

my_tuple_3 = ((1,2,3),("apple", "banana", "grapes"),(True, False)) #Nested tuple
print(my_tuple_3[1][1]) #banana
print(my_tuple_3[2][1]) #False

range_1 = range(1, 11, 2) 
print(range_1) #range(1, 11, 2)
print(type(range_1)) #<class 'range'>
print(range_1[1]) #3
print(len(range_1)) #5