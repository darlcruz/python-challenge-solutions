#program to check if an integer is the power of another integer.
def is_Power(x, y):
   while (x%y == 0):
       x = x / y
   return x == 1
print(is_Power(16, 2))
print(is_Power(12, 2))
print(is_Power(81, 3))