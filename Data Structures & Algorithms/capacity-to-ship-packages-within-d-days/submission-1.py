class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)

        def can(mid: int) -> bool:
            d = 0
            w_count = 0 
            for w in weights:
                w_count += w
                if w_count == mid:
                    w_count = 0
                    d += 1
                elif w_count > mid:
                    w_count = w
                    d += 1
            if w_count > 0:
                d += 1 
            return d <= days

        while l < r:
            mid = (l+r) // 2
            if can(mid):
                r = mid
            else:
                l = mid + 1
        return l
