class Solution(object):
    def addBinary(self, a, b):
       a_dec=int(a,2)
       b_dec=int(b,2)
       sum=a_dec + b_dec
       result="{:b}".format(sum)
       return result        