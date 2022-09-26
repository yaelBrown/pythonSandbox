"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
            print(x)
            if x < 2147483648:
                return x
            else: 
                return 0
        else: 
            x = int(str(abs(x))[::-1])*-1
            if x > -2147483648:
                return x
            else:
                return 0