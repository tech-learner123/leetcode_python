class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse_mapping = {}
        # corner cases: not same length
        if len(s) != len(t):
            return False
        for s1, t1 in zip(s, t):
            if s1 in mapping and mapping[s1] != t1:
                return False
            elif t1 in reverse_mapping and reverse_mapping[t1] != s1:
                return False

            mapping[s1] = t1
            reverse_mapping[t1] = s1
        return True
