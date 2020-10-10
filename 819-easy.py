from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
         banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            #1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue

            #2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []

        return ans

        """
        # hashmap, need to pay attention to the punctuation
        frequency = defaultdict(int)
        banned = set(banned)
        word = ''
        max_count = 0
        ans = ''
        for index, l in enumerate(paragraph):
            if l.isalpha():
                word += l.lower()
                if index != len(paragraph) - 1:
                    continue
            if len(word) > 0:
                if word not in banned:
                    frequency[word] += 1
                if frequency[word] > max_count:
                    max_count = frequency[word]
                    ans = word
                word = ''
        return ans
