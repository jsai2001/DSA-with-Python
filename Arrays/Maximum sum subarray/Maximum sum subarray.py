def maxSubArraySum(arr,N):
    curr_sum=0
    max_so_far=-10000000
    start=end=temp=0
    for i in range(len(arr)):
        curr_sum=curr_sum+arr[i]
        if(curr_sum>max_so_far):
            max_so_far=curr_sum
            start=temp
            end=i
        if(curr_sum<0):
            curr_sum=0
            temp=i+1
    return (arr[start:end+1],max_so_far)
subarray,maxsum=maxSubArraySum([-2,1,-3,4,-1,2,1,-5,4],9)
print("Maximum sum subarray: ",subarray)
print("Maximum sum: ",maxsum)