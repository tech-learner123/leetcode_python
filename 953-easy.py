class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {w: i for i, w in enumerate(order)}

        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
            length = min(len(word1), len(word2))
            # think: if the first letter is smaller then break to the upper for loop
            for index2 in range(length):
                if order_dict[word1[index2]] < order_dict[word2[index2]]:
                    break
                elif order_dict[word1[index2]] > order_dict[word2[index2]]:
                    return False
            # corner case: when apple > app
            if word1[:length] == word2[:length] and len(word1) > len(word2):
                return False
        return True