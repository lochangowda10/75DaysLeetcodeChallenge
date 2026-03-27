class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        char = set()
        maximum = 0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[left])
                left += 1
            char.add(s[i])
            maximum = max(maximum,len(char))
        return maximum