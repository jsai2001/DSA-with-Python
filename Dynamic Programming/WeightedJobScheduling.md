# Weighted Job Scheduling

- Time Complexity: \(O(N \log N)\)

- Space Complexity: \(O(N)\)

## Problem Statement

Given \(N\) jobs, each represented by the following three elements:
1. Start Time (\(s_i\))
2. Finish Time (\(f_i\))
3. Profit (\(p_i\))

We aim to find the maximum profit subset of jobs such that no two jobs in the subset overlap.

## Approach

### Step 1: Sort the Jobs

First, we need to sort the jobs based on their finish times. This allows us to efficiently determine the compatibility of jobs.

### Step 2: Define the DP Table

We will use a dynamic programming approach where we define `dp[i]` as the maximum profit obtainable by considering the first \(i\) jobs.

### Step 3: Find the Latest Non-Conflicting Job

For each job \(i\), we need to find the latest job \(j\) (where \(j < i\)) that does not conflict with job \(i\). This can be efficiently found using binary search.

### Step 4: Populate the DP Table

For each job \(i\), we have two choices:
1. Exclude the current job \(i\) and take the profit up to \(i-1\) (i.e., `dp[i-1]`).
2. Include the current job \(i\) and add its profit to the maximum profit of all jobs that do not overlap with \(i\).

Thus, the recurrence relation is:
\[ dp[i] = \max(dp[i-1], p_i + dp[L(i)]) \]
where \(L(i)\) is the index of the latest non-conflicting job with job \(i\).

### Step 5: Result

The answer will be in `dp[N]`, which contains the maximum profit considering all jobs.

## Algorithm

```python
def find_latest_non_conflicting(jobs, i):
    low, high = 0, i - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[i][0]:
            if jobs[mid + 1][1] <= jobs[i][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def max_profit(jobs):
    # Sort jobs according to finish time
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    
    # Initialize DP table
    dp = [0] * n
    dp[0] = jobs[0][2]
    
    # Fill the DP table
    for i in range(1, n):
        # Include the current job
        profit_incl = jobs[i][2]
        l = find_latest_non_conflicting(jobs, i)
        if l != -1:
            profit_incl += dp[l]
        
        # Exclude the current job
        profit_excl = dp[i - 1]
        
        # Take maximum of including and excluding the current job
        dp[i] = max(profit_incl, profit_excl)
    
    return dp[n - 1]

# Example usage
jobs = [
    (1, 3, 5),   # Job 1: start=1, finish=3, profit=5
    (2, 5, 6),   # Job 2: start=2, finish=5, profit=6
    (4, 6, 5),   # Job 3: start=4, finish=6, profit=5
    (6, 7, 4),   # Job 4: start=6, finish=7, profit=4
    (5, 8, 11),  # Job 5: start=5, finish=8, profit=11
    (7, 9, 2)    # Job 6: start=7, finish=9, profit=2
]

print(max_profit(jobs))  # Output: 17
```

## Explanation

1. **Sorting**: We sort the jobs based on their finish times to ensure we can easily find the latest non-conflicting job.
2. **Dynamic Programming Table (`dp`)**: 
   - `dp[i]` stores the maximum profit by considering the first \(i\) jobs.
   - Initialize `dp[0]` with the profit of the first job since it's the only job considered.
3. **Finding Non-Conflicting Job**:
   - For each job \(i\), we use a helper function `find_latest_non_conflicting` to determine the latest job that does not conflict with job \(i\). This is efficiently done using binary search.
4. **Filling the DP Table**:
   - For each job \(i\), we compute the profit if we include or exclude the job and store the maximum of these two choices in `dp[i]`.

## Time Complexity

1. **Sorting**: \(O(N \log N)\)
2. **DP Table Filling**:
   - Each entry requires finding the latest non-conflicting job, which takes \(O(\log N)\) due to binary search.
   - Hence, filling the table takes \(O(N \log N)\).

Overall time complexity: \(O(N \log N)\)

## Space Complexity

The space complexity is \(O(N)\) for the `dp` array.

Thus, this approach efficiently finds the maximum profit subset of non-overlapping jobs using dynamic programming with a time complexity of \(O(N \log N)\) and a space complexity of \(O(N)\).

Let's revisit the binary search implementation for finding the latest non-conflicting job. We need to ensure that the binary search is correctly identifying the largest index \( j \) where the finish time of job \( j \) is less than or equal to the start time of job \( i \).

Here's a corrected version of the function with a more precise condition handling:

```python
def find_latest_non_conflicting(jobs, i):
    low, high = 0, i - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[i][0]:
            if mid + 1 < len(jobs) and jobs[mid + 1][1] <= jobs[i][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def max_profit(jobs):
    # Sort jobs according to finish time
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    
    # Initialize DP table
    dp = [0] * n
    dp[0] = jobs[0][2]
    
    # Fill the DP table
    for i in range(1, n):
        # Include the current job
        profit_incl = jobs[i][2]
        l = find_latest_non_conflicting(jobs, i)
        if l != -1:
            profit_incl += dp[l]
        
        # Exclude the current job
        profit_excl = dp[i - 1]
        
        # Take maximum of including and excluding the current job
        dp[i] = max(profit_incl, profit_excl)
    
    return dp[n - 1]

# Example usage
jobs = [
    (1, 3, 5),   # Job 1: start=1, finish=3, profit=5
    (2, 5, 6),   # Job 2: start=2, finish=5, profit=6
    (4, 6, 5),   # Job 3: start=4, finish=6, profit=5
    (6, 7, 4),   # Job 4: start=6, finish=7, profit=4
    (5, 8, 11),  # Job 5: start=5, finish=8, profit=11
    (7, 9, 2)    # Job 6: start=7, finish=9, profit=2
]

print(max_profit(jobs))  # Output: 17
```

### Explanation of Changes:

1. **Binary Search Condition**:
   - If the current `mid` job's finish time is less than or equal to the current job's start time (`jobs[mid][1] <= jobs[i][0]`), check if the next job also satisfies this condition.
   - If the next job (`mid + 1`) also does not conflict, move `low` to `mid + 1` to continue searching in the upper half.
   - If the next job does conflict, return the current `mid` as it is the latest non-conflicting job.

### Corrected Binary Search Implementation

This binary search will correctly identify the latest job that doesn't conflict with the current job, ensuring our DP table is populated accurately.

### Time and Space Complexity

The time and space complexity remain the same:
- **Time Complexity**: \(O(N \log N)\) due to sorting and binary search operations.
- **Space Complexity**: \(O(N)\) for storing the DP table.