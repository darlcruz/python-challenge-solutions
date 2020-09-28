#program where you take any positive integer n, if n is even, divide it by 2 
# to get n / 2. If n is odd, multiply it 
# by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1.
def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(x)    
    return num_seq

print(collatz_sequence(12))

print(collatz_sequence(19))