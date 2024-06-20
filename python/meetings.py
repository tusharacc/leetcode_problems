def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: (x[0],x[1]))
    prev_start = 0
    prev_end = 0
    for s,e in intervals:
        if prev_end <= s:
            prev_start = s
            prev_end = e
        else:
            return 0
    
    return 1



if __name__ == '__main__':
    can_attend_all_meetings([[1,5],[1,4],[2,3]])