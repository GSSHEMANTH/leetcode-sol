class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for i in nums:
            ans.append(i)
        conc=nums+ans
        return conc
        