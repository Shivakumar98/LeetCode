Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        s=s.lower()
        for i in s:
            if i.isalnum():
                l.append(i)
        if l == l[::-1]:
            return True
        
