class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        if sentence1 == sentence2:
            return True
        # instead of replacing the word,
        # Two words w1 and w2 are similar if and only if w1 == w2, (w1, w2) was a pair, or (w2, w1) was a pair.
        pairset = set(map(tuple, similarPairs))
        # {('skills', 'talent'), ('drama', 'acting'), ('great', 'fine')}

        return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset for w1, w2 in zip(sentence1, sentence2))