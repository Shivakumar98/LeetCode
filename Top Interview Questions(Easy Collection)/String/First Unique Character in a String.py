Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:    
        for i in range(0,len(s)):
            if s[i] not in  s[i+1:] and s[i] not in s[:i]:
                return i
        return -1
    
    
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         """
#         :type s: str
#         :rtype: int
#         """
#         # build hash map : character and how often it appears
#         count = collections.Counter(s)
        
#         # find the index
#         for idx, ch in enumerate(s):
#             if count[ch] == 1:
#                 return idx     
#         return -1
