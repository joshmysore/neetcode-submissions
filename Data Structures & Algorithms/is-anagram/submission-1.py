class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both strings?
        # check if the same

        return sorted(s) == sorted(t)