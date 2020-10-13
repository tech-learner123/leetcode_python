
class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq != other.freq:
            # smaller frequency, large frequency,
            return lt(self.freq, other.freq) # self.freq < other.freq
        else:
            # opposite sort
            # min heap ascending order (self frequ other freq)
            # if frequency are the same, large word, small word
            return lt(other.word, self.word) # other.word < self.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        words_with_count = collections.Counter(words)

        min_heap = list()
        for word, count in words_with_count.items():
            print(word, count)
            heapq.heappush(min_heap, FreqWord(count, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            print([(w.word, w.freq) for w in min_heap])
        # large, small
        return [heapq.heappop(min_heap).word for _ in range(k)][::-1]



