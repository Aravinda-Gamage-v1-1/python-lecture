my_dict = {
    "name" : "Sugar",
    "price" : 250.00,
    "weight" : "1Kg"
}
print(my_dict) #{'name': 'Sugar', 'price': 250.00, 'weight': '1Kg'}
print(type(my_dict)) #<class 'dict'>

my_dict = {
    "name" : "Sugar",
    "price" : 250.00,
    "weight" : "1Kg",
    "price" : 270.00
}
print(my_dict) #{'name': 'Sugar', 'price': 270,00, 'weight': '1Kg'}

my_dict["price"] = 300.00
print(my_dict) #{'name': 'Sugar', 'price': 300.00, 'weight': '1Kg'}

#my_dict.get(key, default_value)
print(my_dict.get("price")) #300.00
print(my_dict.get("expire_date")) #None
print(my_dict.get("expire_date", "2025.02.23")) #2025.02.23

my_dict.update({"price" : 290.00, "weight" : "2Kg"})
print(my_dict) #{'name': 'Sugar', 'price': 290.0, 'weight': '2Kg'}

my_dict["color"] = "white"
print(my_dict) #{'name': 'Sugar', 'price': 290.0, 'weight': '2Kg', 'color': 'white'}

my_dict.pop("weight")
print(my_dict) #{'name': 'Sugar', 'price': 290.0, 'color': 'white'}

my_dict["weight"] = "1Kg"
del my_dict["weight"]
print(my_dict) #{'name': 'Sugar', 'price': 290.0, 'color': 'white'}
# del my_dict
# print(my_dict) #NameError: name 'my_dict' is not defined

print(len(my_dict)) #3

# my_dict.clear()
# print(my_dict) #{}

my_dict_1 = my_dict.copy()
print( my_dict_1)
