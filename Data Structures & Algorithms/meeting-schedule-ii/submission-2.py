class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        rooms = []  # store end time of each room

        for interval in intervals:
            reused = False

            for i in range(len(rooms)):
                if rooms[i] <= interval.start:
                    rooms[i] = interval.end
                    reused = True
                    break

            if not reused:
                rooms.append(interval.end)

        return len(rooms)