class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)  
        rank = {}  
        for i, num in enumerate(sorted_nums):
            if num not in rank:  
                rank[num] = i
        return [rank[num] for num in nums]
        