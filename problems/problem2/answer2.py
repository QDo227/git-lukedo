class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        for i in range(len(nums)-1, -1, -1):
            complement = target - nums[i]
            if complement in nums:
                index2 = nums.index(complement)
                index1 = i
        temp_list = [index1, index2]
        temp_list.sort()
        return temp_list

