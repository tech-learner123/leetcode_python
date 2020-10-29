class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # the idea is to iteratively divide the last number in the factor combo into smaller numbers
        # [12] ---divide 12 by 2---> [2, 6]  ---divide 6 by 2---> [2, 2, 3] ---3 cannot divide 2 so done---
        # [12] ---divide 12 by 3---> [3, 4] (---divide 4 by 2---> [3, 2, 2])*
        # to fix the issue of duplicates (* above) we pass the starting number for the factor search
        #  so if you've divided by 2, next try dividing by 2 or higher (hence 2, 2, 3)
        #  but if you now divide by 3, start the next division at 3
        # why stop when i*i=num? because any number K>sqrt(num) will have num/K<K which is duplicative

        def dfs(num, i, cur, ret):
            while i * i <= num:
                if num % i == 0:
                    div = num / i
                    ret.append(cur + [i, div])
                    # only feed into the first part of the product e.g.2 * 6  here is [] + 2 ; 2* 2* 3 -> 2 + [2] and let the program to process the 3
                    dfs(div, i, cur + [i], ret)
                i += 1
            return ret

        return dfs(n, 2, [], [])

    """
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n/i],
                factor(n/i, i, combi+[i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])
    """