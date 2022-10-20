'''
Given an integer list nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''



# def duplicate_check(li):
#     iterations = 0
#     # iterate over all the numbers so we can perform check on them
#     for i in range(len(li)):
#         # compare the number that lives at this index with every other number in the list
#         # if we find a duplicate, return True
#         for j in range(i + 1, len(li)): # doing range(i + 1, len(li)) instead of if i == j: continue
#             iterations += 1
#             # avoid comparing the same number to itself
#             # if i == j:
#             #     continue # skip this iteration of the loop
#             # check if the value at i is the same as the value at j
#             if li[i] == li[j]:
#                 return True
#     print('iterations:', iterations)
#     return False


# ## # ## # ## # ## #
# Using a HASH TABLE to achieve 0(n)
def duplicate_check(li):
    iterations = 0
    # use a dictionary as a has table to store uniqu values
    hash_table = {}
    # loop over the numbers, check if they are in the hash table
    for num in li:
        iterations += 1
        # if a number is in the hash table -- return True
        if num in hash_table:
            return True
        # if a number isn't in the hash table -- add it to the hash table
        else:
            hash_table[num] = 'banana'
    print('iterations:', iterations)
    return False



print(duplicate_check([1,2,3,1])) # True
print(duplicate_check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # False
