#program to check if a given positive integer is a power of four.
def is_Power_of_four(n):
    while n and not (n & 0b11):
        n >>= 2
    return (n == 1)

print(is_Power_of_four(4))
print(is_Power_of_four(16))
print(is_Power_of_four(255))