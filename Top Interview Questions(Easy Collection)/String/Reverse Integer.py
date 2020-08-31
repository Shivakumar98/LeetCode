Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        negative = x < 0
        if negative:
            x *= -1
        reverse = 0
        while (x > 0):
            reverse = (reverse * 10) + x % 10
            x = x // 10
        if negative:
            reverse *= -1   
        if reverse >= 2**31 or reverse <=  -2**31:
            return 0
        return reverse



# class Solution:
#     def reverse(self, x: int) -> int:
#         r = 0
#         if x >= 2**31-1 or x <= -2**31: 
#             return 0
#         else:
#             s = str(x)
#             if x >= 0 :
#                 r = s[::-1]
#             else:
#                 r = "-" + s[1::-1]
#             r=int(r)    
#             if r >= 2**31-1 or r <= -2**31: 
#                 return 0
#             else: 
#                 return r
