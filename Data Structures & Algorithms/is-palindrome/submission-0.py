class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = []
        for c in s:
            if c.isalnum():
                original.append(c.lower())

        
        reversed = []
        for p in range(len(original)-1,-1,-1):
            reversed.append(original[p])
        if reversed == original:
            return True
        else:
            return False