class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)

        while k_min < k_max:
            k = (k_min + k_max) // 2
            h_needed = 0

            for pile in piles:
                # h_needed = ceil(pile / k)
                h_needed += (pile + k - 1) // k

            if h_needed > h:
                k_min = k + 1
            else:
                k_max = k

        return k_min
