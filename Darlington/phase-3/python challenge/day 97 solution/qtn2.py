#program to find the difference between the sum of the squares of the first two hundred natural 
# numbers and the square of the sum.
r = range(1, 201)
a = sum(r)
print (a * a - sum(i*i for i in r))