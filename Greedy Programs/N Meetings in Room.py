# Time Complexity: O(nlogn)
# Space Complexity: Between O(1) & O(n) , mostly it will be closer to O(1)

'''
Certainly, here's a more comprehensive explanation of solving the problem of scheduling N meetings in one room using Python:

**The Problem:**
Imagine you have a conference room and N meetings scheduled throughout the day. Each meeting has a start and end time. Your task is to determine the maximum number of meetings that can be accommodated in the room, considering that only one meeting can take place at a time.

**Greedy Approach:**
A Greedy approach is a suitable strategy for this scenario. It makes the locally optimal choice at each step with the hope of achieving a globally optimal solution. In this context, the locally optimal choice translates to selecting the meeting that finishes earliest whenever a room becomes available.

**Steps involved:**
1. **Sort Meetings by End Time:**  The core idea is to prioritize meetings that conclude earlier. This ensures efficient room utilization by scheduling shorter meetings first, potentially freeing up the room for longer meetings later. We use Python's built-in `sort` function along with a lambda function to sort the meetings list based on their end times in ascending order.
2. **Select Meetings:**  We iterate through the sorted list of meetings. The first meeting is automatically included in the schedule since there are no conflicts at the beginning. To decide whether to include subsequent meetings, we introduce a variable `latest_end_time` to track the end time of the last meeting scheduled so far. For each meeting under consideration, we check if its start time (`meeting_start`) is strictly greater than `latest_end_time`. If yes, it implies the meeting room is free at that time, and we can add this meeting to the schedule. We update `latest_end_time` to reflect the end time of the newly included meeting.

**Implementation in Python:**
Here's the Python code that incorporates the greedy approach:
'''

def find_max_meetings(meetings):
    """
  Finds the maximum number of meetings that can be scheduled in one room.

  Args:
      meetings: A list of tuples, where each tuple represents a meeting with a start and end time (in hours).

  Returns:
      A list of meeting indices that can be scheduled in the room.
  """
    # Sort meetings by end time
    meetings.sort(key=lambda m: m[1])

    # Track selected meetings and latest end time
    selected_meetings = [0]  # First meeting is always included
    latest_end_time = meetings[0][1]

    for meeting_start, meeting_end in meetings[1:]:
        if meeting_start > latest_end_time:
            selected_meetings.append(meetings.index((meeting_start, meeting_end)))
            latest_end_time = meeting_end

    return selected_meetings

# Example usage
meetings = [(0, 10), (3, 5), (1, 7), (5, 8)]
selected_meetings = find_max_meetings(meetings.copy())  # Avoid modifying original list
print("Maximum meetings that can be scheduled:", selected_meetings)
'''
Output: Maximum meetings that can be scheduled: [0, 2, 3]

**Explanation of the Code:**
1. The `find_max_meetings` function takes a list of meetings as input, where each meeting is represented by a tuple containing its start and end time.
2. We use `meetings.sort(key=lambda m: m[1])` to sort the meetings in ascending order based on their end times (`m[1]`).
3. We initialize `selected_meetings` with `[0]` to indicate that the first meeting is always included.  We also initialize `latest_end_time` with the end time of the first meeting.
4. The `for` loop iterates through the meetings starting from the second element (index 1) since the first meeting is already included.
5. Inside the loop, we check if the start time of the current meeting (`meeting_start`) is greater than `latest_end_time`. This condition ensures that the meeting room is free to accommodate the current meeting.
6. If the condition is true, it implies the current meeting can be scheduled. We append the index of the current meeting to `selected_meetings` and update `latest_end_time` to reflect the end time of the newly included meeting.
7. The function returns the list `selected_meetings`, which contains the indices of the meetings that can be scheduled in the room.

**Key Points:**
- This approach offers a relatively simple and efficient solution for maximizing the number of meetings in a single room.
- The time complexity of this algorithm is O(n log n) due to the sorting operation.
- This solution might not always find the optimal schedule, but it'

In the `find_max_meetings` function, the average space complexity depends on the number of meetings that can be scheduled concurrently.

Here's why:
* The `selected_meetings` list stores the indices of meetings that can be included in the schedule.
* In the worst case, where no meetings overlap, all meetings could be included, and the list would have a size of n (same as the input size). This scenario leads to O(n) space complexity.
* However, in the average case, we expect only a subset of meetings to be included due to overlapping times. The number of meetings in a room is typically limited, leading to an average list size that's  **significantly smaller than n**.

It's difficult to quantify the exact average size mathematically without knowing the specific characteristics of meeting schedules. However, we can say that the average space complexity is **between O(1)** (if only a constant number of meetings are selected) and **O(n)** (worst case where all meetings are selected).
In most practical scenarios, the average space complexity would be closer to O(1) because the number of concurrently scheduled meetings is unlikely to be as high as the total number of meetings.
'''