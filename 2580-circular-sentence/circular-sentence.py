class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        # Check circularity between consecutive words
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check if the last word's last character matches the first word's first character
        return words[-1][-1] == words[0][0]