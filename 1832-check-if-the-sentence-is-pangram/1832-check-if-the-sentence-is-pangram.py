class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)        # set converts string into unique char
        if len(sentence) < 26:
            return False
        return len(s) == 26