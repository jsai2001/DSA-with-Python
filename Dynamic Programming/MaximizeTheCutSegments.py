'''
Time complexity : O(N), As we using a nested loop but outer loop only runs 3 times and inner loop runs N times so overall complexity is O(3*N), which is approximately O(N).
Space complexity : O(N) for dp array .
'''
def maximizeTheCuts(n,x,y,z):
        length = n
        cut_lengths = [x,y,z]
        max_cuts = [-1] * (length + 1)

        # Base case
        max_cuts[0] = 0

        # Loop through rod lengths
        for i in range(0, length + 1):
            # Consider the cut that gives the most segments
            if(max_cuts[i]==-1):
                continue
            #we will update dp[i] if a segment of x,y,z is possible.
            if(i+cut_lengths[0]<=length):
                max_cuts[i+cut_lengths[0]]=max(max_cuts[i+cut_lengths[0]],max_cuts[i]+1)
            if(i+cut_lengths[1]<=length):
                max_cuts[i+cut_lengths[1]]=max(max_cuts[i+cut_lengths[1]],max_cuts[i]+1)
            if(i+cut_lengths[2]<=length):
                max_cuts[i+cut_lengths[2]]=max(max_cuts[i+cut_lengths[2]],max_cuts[i]+1)
        
        #if no segment can be cut then we return 0.
        if(max_cuts[length]==-1):
            return 0
        
        #returning the result.
        return max_cuts[length]
print(maximizeTheCuts(3,1,2,3))