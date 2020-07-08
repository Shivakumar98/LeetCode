Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

   Hide Hint #1  
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
   Hide Hint #2  
For the two-sum problem, if we fix one of the numbers, say

x

, we have to scan the entire array to find the next number

y

which is

value - x

where value is the input parameter. Can we change our array somehow so that this search becomes faster?
   Hide Hint #3  
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length-2): #[8]
            if nums[i]>0: break #[7]
            if i>0 and nums[i]==nums[i-1]: continue #[1]

            l, r = i+1, length-1 #[2]
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0: #[3]
                    l+=1
                elif total>0: #[4]
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1
        return res
        

        
#                  Worked but timelimit exceeded
        # s=sorted(nums)
        # print(s)
        
        # l=[]
        # n=len(s)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if s[i]+s[j]+s[k]==0 and [s[i],s[j],s[k]] not in l:
        #                 l.append([s[i],s[j],s[k]])
        # return l  
