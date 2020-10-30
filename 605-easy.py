class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] != 1:
                # corner case:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
        return False if n > 0 else True

