class Solution(object):
    '''
    All these implementations can be tested in https://leetcode.com/problems/sort-an-array/
    '''
########### bubble sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        for j in range(0, len(nums) - 1):
            for i in range(0, len(nums) - j -1):
                if nums[i] > nums[i+1]:
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp
        return nums


########### python build-in sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        return nums

    
########### insert sort
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        for i in range(1, len(nums)):  # new "cards"
            for j in range(i, 0, -1):  # going back from sorted "cards"
                if nums[j - 1] > nums[j]:
                    temp = nums[j - 1]
                    nums[j - 1] = nums[j]
                    nums[j] = temp
                else:
                    break
        return nums



############ selection sort
    def sortArray(self, nums):
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
        return nums


########### quick sort
    def shuffle(self, nums):
        import random
        random.shuffle(nums)

    def partition(self, nums):
        if len(nums) <= 1:
            return nums, 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                temp = nums[0]
                nums[0] = nums[1]
                nums[1] = temp
                return nums, 1
            else:
                return nums, 0

        k = 0
        i = 1
        j = len(nums) - 1
        while i <= j:
            while i < len(nums) and nums[i] <= nums[k]:
                i += 1
            while j > 0 and nums[j] >= nums[k]:
                j -= 1
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        temp = nums[k]
        nums[k] = nums[j]
        nums[j] = temp
        return nums, j

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        self.shuffle(nums)
        nums, j = self.partition(nums)
        left_part = self.sortArray(nums[0:j])
        center_part = nums[j]
        right_part = self.sortArray(nums[j + 1:len(nums) + 1])
        nums = []
        nums.extend(left_part)
        nums.append(center_part)
        nums.extend(right_part)
        return nums

############ Merge Sort
    def merge(self, a, b):
        result = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        if i < len(a):
            while i < len(a):
                result.append(a[i])
                i += 1
        if j < len(b):
            while j < len(b):
                result.append(b[j])
                j += 1
        return result
    
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        mid = int(round(len(nums)/2))
        left_part = self.sortArray(nums[0:mid])
        right_part = self.sortArray(nums[mid: len(nums)+1])
        return self.merge(left_part, right_part)
