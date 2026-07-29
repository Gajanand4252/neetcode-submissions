class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = "".join(ch for ch in s if ch.isalnum())
        res = ""
        for ch in range(len(str1)-1, -1, -1):
            res = res + str1[ch]
        if res.lower() == str1.lower():
            return True
        else:
            return False
        print(res)