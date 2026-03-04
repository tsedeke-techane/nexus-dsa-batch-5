class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 

        x_rev = 0
        n = x
        while n != 0:
            remainder = n % 10
            x_rev = x_rev * 10 + remainder
            n = n // 10

        if x == x_rev:
            return True
        else:
            return False