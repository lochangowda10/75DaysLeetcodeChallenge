class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct = 0
        sl = len(s)
        tl = len(t)
        if sl == tl:
            for i in range(sl):
                if s[i] in t:
                    ct += 1
                    t = t.replace(s[i],"",1)
            if ct >= sl:
                return True
        return False