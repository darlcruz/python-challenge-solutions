#program to find the largest palindrome made from the product of two 4-digit numbers
n = 0
for a in range(9999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)