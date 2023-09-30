# The sorted function used in the first line has a time complexity of O(n log n), where n is the number of intervals.
# The while loop iterates over each interval and has a time complexity of O(n).
# The if statement inside the loop has a time complexity of O(1).
# The max function inside the if statement has a time complexity of O(1).
# The pop function inside the if statement has a time complexity of O(n).
# Overall, the time complexity of the given code snippet is O(n log n).

# Time Complexity : O(nlogn) , due to sorting operation
# Space Complexity : O(1) , intervals variable is given by the GFG , we are using the same memory ,
#                    Python interpreter , doesn't create any new space in here
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