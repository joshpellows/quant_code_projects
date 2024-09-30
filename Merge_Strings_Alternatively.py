class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        if len(word1) <= len(word2):
            for i in range(len(word1)):
                merged += word1[i]
                merged += word2[i]
            for i in range(len(word1),len(word2)):
                merged += word2[i]
            return merged
        else:
            for i in range(len(word2)):
                merged += word1[i]
                merged += word2[i]
            for i in range(len(word2), len(word1)):
                merged += word1[i]
            return merged