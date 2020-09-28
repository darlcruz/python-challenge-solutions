# program to compute the sum of all the multiples of 3 or 5 below 500.
n = 0
for i in range(1,500):
     if not i % 5 or not i % 3:
         n = n + i
print(n)