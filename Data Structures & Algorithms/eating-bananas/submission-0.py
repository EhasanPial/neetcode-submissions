class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #lower bound code
        # why BS?
        # we have to find k such that 1 <= k <= max(pile)
        # k = 1 2 3 4 5 6 7 8  9
        #     F F F F T T T T that
        #min_k=       *

        def can(mid: int) -> bool:

            total_hrs = 0
            for i in piles:
                total_hrs += (i+mid-1) // mid # ceil in python
            return total_hrs <= h


        piles.sort()
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r) // 2

            if can(mid): # <=
                r = mid # works
            else:
                l = mid + 1

        return l
