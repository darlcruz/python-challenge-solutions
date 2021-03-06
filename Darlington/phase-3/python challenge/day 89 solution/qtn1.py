#program to find the single element in a list where every element appears three times except for one.
def single_number(arr):
    ones, twos = 0, 0
    for x in arr:
        ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x)
    assert twos == 0
    return ones
arr1 = [5, 3, 4, 3, 5, 5, 3]
arr2 = [-1, 1, 1, -1, -1, 1, 0]
print(single_number(arr1))
print(single_number(arr2))