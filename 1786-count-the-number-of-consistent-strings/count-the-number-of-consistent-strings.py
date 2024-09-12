class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # k = set(allowed)
        c = 0 
        for word in words:
            if all( i in allowed for i in  word):
                c += 1
        return c
                
        