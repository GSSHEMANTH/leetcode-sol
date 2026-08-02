class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        current = 1
        longest = 1

        for i in range(len(nums) - 1):

            if nums[i] + 1 == nums[i + 1]:
                current+=1

            elif nums[i] == nums[i + 1]:
                continue

            else:
                longest = max(longest, current)
                current = 1
        longest = max(longest, current)

        return longest