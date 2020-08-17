Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
#         1     0001
#         4     0100
#         16   10000
#         64 1000000
#          so 1 will be in even position when counted from right
        if num < 1: return False
        
        # checking if it consists only one one
        # 4 and 3 ==> 100 and 011 = 0
        if num & num-1 != 0: return False
        
        # reversing the bits
        n = bin(num)[::-1]
        i = n.index("1")
        # check even position
        return i%2 == 0
        
        
        
        # my solution
        # t=1
        # while t<=num:
        #     if t==num:
        #         return True
        #     t*=4
        
        
