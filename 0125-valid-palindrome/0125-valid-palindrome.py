class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.replace(" ","")
        a = a.replace(":","")
        a = a.replace(",","")
        a = a.replace(".","")
        a = a.replace("-","")
        a = a.replace("_","")
        a = a.replace("+","")
        a = a.replace("/","")
        a = a.replace("@","")
        a = a.replace("!","")
        a = a.replace("#","")
        a = a.replace("%","")
        a = a.replace("&","")
        a = a.replace("*","")
        a = a.replace("(","")
        a = a.replace(")","")
        a = a.replace("[","")
        a = a.replace("]","")
        a = a.replace("{","")
        a = a.replace("}","")
        a = a.replace("'","")
        a = a.replace(";","")
        a = a.replace("\ ","")
        a = a.replace("?","")
        a = a.replace("|","")
        a = a.replace("^","")
        a = a.replace("''","")
        a = a.replace("\"","")
        a = a.replace("\.","")
        a = a.replace("\\","")
        a = a.replace("`","")
        b = a.lower()
        b1 = b[::-1]
        if b==b1 :
            return True
        else :
            return False