Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #optimal solution
        if len(s) != len(t):
            return False
        if len(s) != len(t):
            return False
        s=sorted(s)
        t=sorted(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True
           

      #first solution
        if len(s) != len(t):
            return False
        S,T={},{}
        for i in s:
            if i in S:
                S[i]+=1
            else:
                S[i]=1
        for i in t:
            if i in T:
                T[i]+=1
            else:
                T[i]=1
        for i in S.keys():
            if (i not in T) or S[i]!=T[i]:
                return False
        return True
        
