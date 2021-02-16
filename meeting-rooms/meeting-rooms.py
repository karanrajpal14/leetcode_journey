class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        can_attend = True
        meeting_list = []
        
        for interval in sorted(intervals, key=lambda x: x[0]):
            if meeting_list and interval[0] < meeting_list[-1][1]:
                can_attend = False
            else:
                meeting_list.append(interval)
        
        return can_attend