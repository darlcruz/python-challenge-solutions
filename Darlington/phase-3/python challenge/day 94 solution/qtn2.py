#program to find majority element in a list.
def majority_element(num_list):
        idx, ctr = 0, 1
        
        for i in range(1, len(num_list)):
            if num_list[idx] == num_list[i]:
                ctr += 1
            else:
                ctr -= 1
                if ctr == 0:
                    idx = i
                    ctr = 1
        
        return num_list[idx]

print(majority_element([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))

print(majority_element([1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6]))