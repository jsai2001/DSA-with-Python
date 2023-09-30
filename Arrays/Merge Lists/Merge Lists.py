def merge(intervals):
        intervals = sorted(intervals,key=lambda x:(x[0],x[1]))
        iterator = 0
        while(iterator+1<len(intervals)):
            if(intervals[iterator][1]>=intervals[iterator+1][0]):
                intervals[iterator][1]=max(intervals[iterator][1],intervals[iterator+1][1])
                intervals.pop(iterator+1)
            elif(intervals[iterator][1]<intervals[iterator+1][0]):
                iterator+=1
        return intervals
print(merge([[1,4],[4,5]]))