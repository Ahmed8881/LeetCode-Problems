class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0  # The only element is the peak
        
        i = 0
        for j in range(1, len(nums) - 1):
            if nums[j] > nums[i] and nums[j] > nums[j + 1]:
                return j
            i += 1  # Move i forward
        
        # Handle edge cases when peak is at the start or end
        if nums[0] > nums[1]:  # First element is the peak
            return 0
        return len(nums) - 1  # Last element is the peak
