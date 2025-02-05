class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        temp=x
        reversed=0
        while(temp>0):
            reversed=reversed*10+temp%10
            temp/=10
        return (reversed==x)
        
