Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
   Hide Hint #1  
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
   Hide Hint #2  
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.


# this is not O(n logk) solution its a brootforce solution O(n**2)

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         

        if t==0 and len(nums) == len(set(nums)):
            return False
        
        n=len(nums)
        for i in range(len(nums)):
            for j in range(i+1,min(i+1+k,n)):
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False
                
        
        # time limit exceeded 
    
        #this can also be used to accepted    
         # if t==0 and len(nums) == len(set(nums)):
         #    return False

        # f=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(nums[i]-nums[j]) <= t and abs(i-j) <= k:
        #             f=1
        # if f == 1:
        #     return True
        # else:
        #     return False
