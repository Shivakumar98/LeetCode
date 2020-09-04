Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)



class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if len(s) <= 1:
            return False
        if len(set(s)) == 1:
            print(set(s))
            return True
        f=0
        for i in range(1,len(s)):
            # set(s[:i+1]) == set(s[i+1:])
            if s[:i+1] in s[i+1:]:
                k=len(s) // len(s[:i+1])
                if  s[:i+1]*k == s:
                    # print(s,k,s[:i+1])
                    f=1
        if f:
            return True
        else:
            return False
