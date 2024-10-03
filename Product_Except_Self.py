from itertools import product


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        c = 0
        prod = 1
        res = [0] * n
        # Calculate product of all non-zero elements and count zeros
        for num in nums:
            if num == 0:
                c += 1
            else:
                prod *= num
        # Generate the result array
        for i in range(n):
            if c > 1:
                res[i] = 0
            elif c == 1:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // nums[i]
        return res


print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))
print(Solution().productExceptSelf([0,0]))