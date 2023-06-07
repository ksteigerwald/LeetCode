class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort the letters of the word

            if sorted_word not in groups:
                groups[sorted_word] = [word]
            else:
                groups[sorted_word].append(word)

        return list(groups.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
print(s.groupAnagrams(["", ""]))
print(s.groupAnagrams(["a", "b", "c", "d"]))
print(s.groupAnagrams(["eat", "tea", "ate", "melon", "lemonade"]))
print(s.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))