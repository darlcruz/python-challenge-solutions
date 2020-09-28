#program to assess if a file is closed or not.
 f = open('abc.txt','r')
print(f.closed)
f.close()
print(f.closed)