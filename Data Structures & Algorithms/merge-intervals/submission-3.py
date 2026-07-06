class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for interval in intervals:
            if  result[-1][1] >= interval[0]: #Overlapping
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result

        
        