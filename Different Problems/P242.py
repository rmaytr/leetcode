class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)):
            return True
        return False
