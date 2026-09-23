"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import operator

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=operator.attrgetter('start'))
        for i in range(len(intervals) - 1):
            nextInterval = intervals[i + 1]
            current = intervals[i]
            if current.start <= nextInterval.start and nextInterval.start < current.end:
                return False

        return True
