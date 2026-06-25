class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)
        if len(sentence) < 26:
            return False
        return len(s) == 26