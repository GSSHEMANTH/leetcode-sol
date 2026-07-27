class Solution(object):
    def removeDuplicates(self, nums):
        a = set(nums)
        b = sorted(a)

        for i in range(len(b)):
            nums[i] = b[i]

        return len(b)