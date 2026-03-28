class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxf = 0
        max_len = 0 
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            maxf = max(maxf,count[s[i]])
            while (i-left+1)-maxf > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len,i-left+1)
        return max_len
        