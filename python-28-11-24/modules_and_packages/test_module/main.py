# import my_module as mm
# from my_module import add, subtract
from my_module import * # This is not good
import math as m

print(add(3,5))
print(subtract(6,4))

print(m.pi)

num = 5
fact_value = m.factorial(num)
print(fact_value)
