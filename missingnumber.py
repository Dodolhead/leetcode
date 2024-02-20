class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        b = 0
        nums.sort()

        for y in range(0,len(nums)+1):
            if b == len(nums):
                b -= 1
            if nums[b] != 0:
                if y == nums[b]:
                    b += 1
                elif y != nums[b]:
                    return y
                    break
            elif nums[b] == 0:
                b += 1
                y -= 1

