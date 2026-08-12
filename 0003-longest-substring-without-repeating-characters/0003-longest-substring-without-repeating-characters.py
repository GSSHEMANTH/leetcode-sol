class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=set()
        left=0
        maxlen=0
        for right in range (len(s)):
            while s[right] in a:
                a.remove(s[left])
                left+=1
            a.add(s[right])
            maxlen=max(maxlen,right-left+1)
        return maxlen