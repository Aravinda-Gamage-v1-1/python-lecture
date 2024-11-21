num_list = [109, 60, 45, 72, 14]
num_list.sort() 
print(num_list) #[14, 45, 60, 72, 109]
num_list.sort(reverse=True)
print(num_list) #[109, 72, 60, 45, 14]

num_list = ["dog"]

my_list_1 = [1, 3, 5, 3, 9]
my_list_2 = my_list_1.copy()
print(my_list_2) #[1, 3, 5, 3, 9]

my_list_1 = [8, 10, 12, 9, 11, 15, 16, 4]
print(my_list_1[1:6]) #[10, 12, 9, 11, 15]
print(my_list_1[1:6:2]) #[10, 9, 15]

#Unpacking
my_list_1 = [10, 12, 7]
x, y, z = my_list_1
print(x, y, z) #[10, 9, 15]