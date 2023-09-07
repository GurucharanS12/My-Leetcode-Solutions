class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=x
        r=0
        while(x>0):
            dig=x%10
            r=r*10+dig
            x=x//10
        if (x<0):
            return False
        else:
            if (t==r):
                return True
            else:
                return False
