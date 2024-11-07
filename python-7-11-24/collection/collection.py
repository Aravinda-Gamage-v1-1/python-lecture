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
print(my_list2[:3], type(my_list2[:3])) #[10, 'lion', 'elephant'] <class 'list'>