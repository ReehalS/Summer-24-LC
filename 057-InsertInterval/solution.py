#
# 67ms (92.22%), 19.84MB (55.37%)
#
# set newStart, newEnd to be first and last of the newInterval
# loop through intervals
# if interval end < newInterval start, append to results
# if interval start > newInterval end append interval to results
#       if the new interval has not already been added, append it before adding the new interval, set start = -1 (to not break the first if case)
# if none of these conditions satisfy, set the newStart to minimum of interval start and newStart,
#       and set newEnd to max of interval end, newEnd
# end case to check if this list is the last list to be appended to results
# return results


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval
        for interval in intervals:
            if(interval[1]<newStart):
                result.append(interval)
            elif(interval[0]>newEnd):
                if(newStart>=0):
                    result.append([newStart,newEnd])
                    newStart=-1
                result.append(interval)
            else:
                newStart = min(interval[0], newStart)
                newEnd = max(interval[1], newEnd)
        if(newStart>=0):
            result.append([newStart,newEnd])
        return result