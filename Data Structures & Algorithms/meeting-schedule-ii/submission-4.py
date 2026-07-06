class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        rooms = []  # store end time of each room

        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)

        return len(rooms)