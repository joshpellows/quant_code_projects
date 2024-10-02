from peewee import Source


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        answer = []
        i =0
        while i < len(nums):
            start = nums[i]
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i+=1
            if start != nums[i]:
                answer.append(str(start)+ "->"+ str(nums[i]) )
            else:
                answer.append(str(nums[i]))

            i+=1
        return answer
