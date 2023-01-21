class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals)

        for i in range(len(sorted_intervals)-1):
            if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                return False

        return True
