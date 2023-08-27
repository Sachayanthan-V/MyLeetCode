class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = '' 
        length = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(length):
            s += word1[i]
            s += word2[i]
        if length < len(word1):
            s += word1[length:]
        if length < len(word2):
            s += word2[length:]
        return s