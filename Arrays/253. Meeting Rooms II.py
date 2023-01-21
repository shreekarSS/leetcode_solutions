import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals)

        freerooms = []


        heapq.heappush(freerooms,intervals[0][1])

        for k in intervals[1:]:
            if freerooms[0] <= k[1]:
                heapq.heappop(freerooms)
            heapq.heappush(freerooms,k[1])

        return len(freerooms)
