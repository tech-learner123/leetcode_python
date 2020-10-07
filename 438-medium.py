class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
       # robin carb, no order need to consider.
        s_number = [ord(l) - ord('a') for l in s]
        p_number = [ord(l) - ord('a') for l in p]

        res_index = []
        target = sum(p_number)

        def check_string_match(source, target):
            return set(source) == set(target)

        for i in range(len(s) - len(p) + 1):
            if i != 0:
                h = h - s_number[i - 1] + s_number[i + len(p) -1]
            else:
                # inital the first sum
                h = sum(s_number[:len(p)])

            if h == target:
                if check_string_match(s[i: i+ len(p)], p):
                    res_index.append(i)
        return res_index
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        output = []
        # sliding window on the string s:
        for i in range(ns):
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        return output