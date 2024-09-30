class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        index = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                index = i
                break
            elif abs(nums [i]) < abs(nums[index]):
                index = i

        if nums[index]<0:
            for i in range(len(nums)):
                if nums[i] == abs(nums[index]):
                    index = i
        return nums[index]
