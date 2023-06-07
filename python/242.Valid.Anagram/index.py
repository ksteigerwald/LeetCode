class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        keys = sorted([letter for letter in s])
        vals = sorted([letter for letter in t])

        if len(keys) != len(vals):
            return False

        for i in range(len(keys)):
            if keys[i] != vals[i]:
                return False

        a = {key: 0 for key in keys }
        b = {key: 0 for key in vals }
        for k in keys:
            a[k] = a[k] + 1
            if b.get(k) is not None:
                b[k] = b[k] + 1
            else:
                return False
        return a == b

    # ChatGPT Imporvements
    def isAnagramTwo(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26  # Assuming lowercase English alphabet characters

        for char in s:
            count[ord(char) - ord('a')] += 1

        for char in t:
            count[ord(char) - ord('a')] -= 1
            if count[ord(char) - ord('a')] < 0:
                return False

        return True




s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("car", "rat"))
print(s.isAnagram("aacc", "ccac"))

print(s.isAnagramTwo("anagram", "nagaram"))
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""