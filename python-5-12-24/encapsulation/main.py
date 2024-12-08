# class MyClass:
#     def __init__(self):
#         self.var_1 = "some value"
#         self._var_1 = "protected attribute"
#         self.__var_1 = "private attribute"

# my_obj = MyClass()
# print(my_obj.var_1)
# print(my_obj._var_1)
# print(my_obj.__var_1)

# ===============================================================

# class MyClass:
#     def __init__(self):
#         self.var_1 = "some value"
#         self._var_1 = "protected attribute"
#         self.__var_1 = "private attribute"

#     def _protected_method(self):
#         print("protected method")

#     def __private_method(self):
#         print("private method")

# my_obj = MyClass()
# print(my_obj.var_1)
# print(my_obj._var_1)
# print(my_obj.__var_1)

# my_obj._protected_method()
# my_obj.__private_method()

# ===============================================================

# class MyClass:
#     def __init__(self):
#         self.__data = "some data"

#     def get_value(self):
#         return self.__data

#     def set_value(self, value):
#         self.__data = value

# my_obj = MyClass()
# print(my_obj.get_value())
# my_obj.set_value("update")
# print(my_obj.get_value)

# ===============================================================

# class MyClass:
#     def __init__(self):
#         self.__data = "some data"

#     def __check_my_values(self):
#         print("checking values")

#     def get_check(self):
#         self.__check_my_values()

# my_obj = MyClass()
# my_obj.get_check()

# ===============================================================

# class Animal:
#     def __init__(self):
#         self.data = "some data"

#     def __init__(self):
#         self.__maker_sound()

# class Dog(Animal):
#     def bark(self)L
#         self.__mak

# ===============================================================


#Write a python program to create quadraticEquation that represent a quadratic equation of the from aX
# The class shuld hava
# 1. Attributes
#       __a,__b and __c to store the core vision of the quadratic equation
#       Methods: a constructor to initialize the core verstion a and c
# 2. A private method__discriminamt() that calculate and a return the discrimiant (D = b2 = 4ac
# 3. A public method find_root() that, use the private discriminant method
# 4. Return the root of the quadratic equation (D>0) to distion real root, (D=0) one real root, (D<0) complex root


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def __discriminant(self):
        return self.__b**2 - 4*self.__a*self.__c
    
    def find_root(self):
        D = self.__discriminant()
        if D > 0:
            root_1 = (-self.__b + D**0.5)/(2*self.__a)
            root_2 = (-self.__b - D**0.5)/(2*self.__a)
            massage = "roots are:" , root_1 , " " , root_2
            return massage
        
        elif D == 0:
            root = -self.__b/(2*self.__a)
            massage = "One real root:", root
            return massage
        else:
            return "Equation has complex roots"
        
new_quadraticEquation = QuadraticEquation(1, -3, 2)
print(new_quadraticEquation.find_root())