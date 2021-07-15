# Functions for sorting exercise

def cmp(a, b):
    return (a > b) - (a < b) 

def mySort(numbers):
    numbers = bubbleSort(numbers)
    return numbers

def bubbleSort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #################################

    # Selection Sort

    n = len(nums)
    if n<=1:
        return nums
    for i in range(n):
        smallest_val = nums[i]
        smallest_idx = i
        # find the smallest element
        for j in range(i,n):
            temp = nums[j]
            if temp <= smallest_val:
                smallest_idx = j
                smallest_val = temp
            # print(smallest_val)
        # swap it with nums[i]
        temp = nums[i]
        nums[i] = nums[smallest_idx]
        nums[smallest_idx] = temp
 
    
    #################################
    return nums