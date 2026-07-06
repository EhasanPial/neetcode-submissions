class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            curS = intervals[i][0]
            curE = intervals[i][1]

            prevE = result[-1][1]

            if prevE >= curS: #Overlapping
                result[-1][1] = max(prevE, curE)
            else:
                result.append(intervals[i])

        return result

        
        