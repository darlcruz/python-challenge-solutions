#program to the push the first number to the end of a list.
def move_last(num_list):
    a = [num_list[0] for i in range(num_list.count(num_list[0]))]
    x = [ i for i in num_list if i != num_list[0]]
    x.extend(a)
    return(x)
l1 = [0,2,3,4,6,7,10]
l2 = [10,0,11,12,14,0,17]
print("Original List: ",l1)
print(move_last(l1))
print("Original List: ",l2)
print(move_last(l2))