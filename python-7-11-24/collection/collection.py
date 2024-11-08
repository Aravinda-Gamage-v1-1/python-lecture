my_list1 = [10, 5, 8, 20, 25]
my_list2 = ["dog", "cat", "lion", "elephant"]
print(my_list1, type(my_list1)) #[10, 5, 8, 20, 25] <class 'list'>
print(my_list2, type(my_list2)) #['dog', 'cat', 'lion', 'elephant'] <class 'list'>
print(my_list1[4]) #25

my_list1 = [10, 5, "car", 8, 20, 25]
print(my_list1, type(my_list1)) #[10, 5, 'car', 8, 20, 25] <class 'list'>

my_list2[1] = 10
print(my_list2, type(my_list2)) #['dog', 10, 'lion', 'elephant'] <class 'list'>

#Python lists are ordered

#Python lists allow duplicate

#To determine how many items a list has, use the lan() function.
print(len(my_list2)) #4

print(my_list2[-1]) #elephant
print(my_list2[-3]) #10

print(my_list2[1:4], type(my_list2[1:4])) #[10, 'lion', 'elephant'] <class 'list'>
print(my_list2[:3], type(my_list2[:3])) #['dog', 10, 'lion'] <class 'list'>
print(my_list2[2:], type(my_list2[2:])) #['lion', 'elephant'] <class 'list'>


my_list1[1:3] = ["parrot", 17.0]
print(my_list1) #[10, 'parrot', 17.0, 8, 20, 25]

my_list1.insert(2, "Rat") #add a value
print(my_list1) #[10, 'parrot', 'Rat', 17.0, 8, 20, 25]

my_list1.append("carrot") #add a value
print(my_list1) #[10, 'parrot', 'Rat', 17.0, 8, 20, 25, 'carrot']

my_list1.extend(my_list2) #add a list to another list
print(my_list1) #[10, 'parrot', 'Rat', 17.0, 8, 20, 25, 'carrot', 'dog', 10, 'lion', 'elephant']

my_list1.pop(2) #remove value
print(my_list1) #[10, 'parrot', 17.0, 8, 20, 25, 'carrot', 'dog', 10, 'lion', 'elephant']

del my_list1[2] #remove value
print(my_list1) #[10, 'parrot', 8, 20, 25, 'carrot', 'dog', 10, 'lion', 'elephant']

my_list1.clear() #clear list
print(my_list1) #[]

# del my_list1 #delete list
# print(my_list1) #name 'my_list1' is not defined

my_list3 = ["grapes", "apple", "orange", "banana"]

my_list3.sort() #sorting a list
print(my_list3) #['apple', 'banana', 'grapes', 'orange']

my_list3 = ["Grapes", "apple", "orange", "banana"]

my_list3.sort() #this sort function is case sensitive sorting
print(my_list3) #['Grapes', 'apple', 'banana', 'orange']

my_list3.sort(key = str.lower) #this is not case sensitive sorting
print(my_list3) #['apple', 'banana', 'Grapes', 'orange']

my_list4 = [5, 3, 10, 25, 8]
my_list4.sort() #by default sorting in ascending order
print(my_list4) #[3, 5, 8, 10, 25]

my_list4.sort(reverse=True) #sorting in descending order
print(my_list4) #[25, 10, 8, 5, 3]



my_list5 = [12, 10, 13, 4, 1, 5]
my_list6 = [6, 1, 7, 8, 10]

my_list5.extend(my_list6)
print(my_list5)
my_list5.sort()
print(my_list5)
print("Medium", my_list5[int((len(my_list5)+1)/2)-1]) #position of medium
print("Q1", my_list5[int((len(my_list5)+1)/4)-1]) #position of Q1
print("Q3", my_list5[int((len(my_list5)+1)*3/4)-1]) #position of Q3