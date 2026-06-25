class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for i in sentences:
            current_word = len(i.split())  #convert into smaller list, ex: ["abc"] = ['a','b','c']
            if current_word > max_count:
                max_count = current_word
        return max_count