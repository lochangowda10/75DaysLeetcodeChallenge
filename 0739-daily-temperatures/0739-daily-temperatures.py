class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_days = []
        n = len(temperatures)
        result = [0]*n

        for i in range(n):

            while waiting_days and temperatures[i] > temperatures[waiting_days[-1]]:
                prev_day = waiting_days.pop()
                result[prev_day] = i - prev_day
            waiting_days.append(i)

        return result
        