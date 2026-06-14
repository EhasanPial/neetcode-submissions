class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [-1] * len(temperatures)

        for index, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = index-i

            stack.append(index)

        while stack:
            i = stack.pop()
            result[i] = 0 

        return result

        