Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
   Hide Hint #1  
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
   Hide Hint #2  
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            ele = nums[i]
            if ele != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                # print(nums)
                pos += 1
        
#         h,l=len(nums)-1,0
#         while l < h:
#             if nums[l] == 0:
#                 # print(nums)
#                 nums = nums[:l]+nums[l+1:]+[0]
#                 # print(nums)
#                 h -= 1
#             else:
#                 l+=1
#         print(nums)
#         # return nums
