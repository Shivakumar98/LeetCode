Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A=sorted(A,reverse=True)
        A=list(permutations(A))
        # print(A)
        for i in A:
            h=i[0]*10+i[1]
            m=i[2]*10+i[3]
            if h<=23 and m<=59:
                return str(i[0])+str(i[1])+':'+str(i[2])+str(i[3])
        return ''
