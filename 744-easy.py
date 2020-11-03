class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #         minimum_dis = 27
        #         mini_letter = ''
        #         for letter in letters:
        #             distance = ord(letter) - ord(target)
        #             if distance < 0:
        #                 distance = 26-abs(distance)

        #             # print(distance)
        #             if distance < minimum_dis and letter != target:
        #                 minimum_dis = distance
        #                 mini_letter = letter
        #         return mini_letter
        # approach 2
        # for c in letters:
        #     if c > target:
        #         return c
        # return letters[0]

        # approach 3
        index = bisect.bisect(letters, target)
        print(index)
        return letters[index % len(letters)]