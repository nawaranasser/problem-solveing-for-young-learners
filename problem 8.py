"""
You are given an integer n representing the number of rooms numbered from 0 to n - 1.
Additionally, you are given a 2D integer array meetings[][] where meetings[i] = [start i, end i] indicates that a
meeting is scheduled during the half-closed time interval [start i, end i). All start_i values are unique.

Meeting Allocation Rules:

When a meeting starts, assign it to the available room with the smallest number.
If no rooms are free, delay the meeting until the earliest room becomes available.
The delayed meeting retains its original duration.
When a room becomes free, assign it to the delayed meeting with the earliest original start time.
Determine the room number that hosts the most meetings. If multiple rooms have the same highest number of meetings,
 return the smallest room number among them.

Examples:

Input: n = 2, meetings[][] = [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]
Output: 1
Explanation: Time 0: Both rooms available. [0,6] starts in room 0.
Time 2: Room 0 busy until 6. Room 1 available. [2,3] starts in room 1.
Time 3: Room 1 frees up. [3,7] starts in room 1.
Time 4: Both rooms busy. [4,8] is delayed.
Time 6: Room 0 frees up. Delayed [4,8] starts in room 0 [6,10).
Time 6: [6,8] arrives but both rooms busy. It’s delayed.
Time 7: Room 1 frees up. Delayed [6,8] starts in room 1 [7,9).
Meeting counts: [2, 3]
"""

import heapq

def most_booked(n, meet):
    # Step 1: Sort meetings by start time
    meet.sort()

    # Step 2: Initialize available rooms (min-heap)
    available_rooms = list(range(n))
    heapq.heapify(available_rooms)

    # Step 3: Initialize ongoing meetings (min-heap of (end_time, room_number))
    ongoing_meetings = []

    # Step 4: Count meetings per room
    room_meeting_count = [0] * n

    # Step 5: Loop through sorted meetings
    for start, end in meet:

        # Free up rooms whose meetings ended before current meeting start
        while ongoing_meetings and ongoing_meetings[0][0] <= start:
            finished_time, finished_room = heapq.heappop(ongoing_meetings)
            heapq.heappush(available_rooms, finished_room)

        # If a room is available, assign the meeting
        if available_rooms:
            room = heapq.heappop(available_rooms)
            heapq.heappush(ongoing_meetings, (end, room))
        else:
            # No room available → delay the meeting to the soonest free time
            finished_time, room = heapq.heappop(ongoing_meetings)
            new_end = finished_time + (end - start)
            heapq.heappush(ongoing_meetings, (new_end, room))

        # Count the meeting
        room_meeting_count[room] += 1

    # Step 6: Return the room with most meetings (smallest index if tie)
    max_meetings = max(room_meeting_count)
    for i in range(n):
        if room_meeting_count[i] == max_meetings:
            return i







print(most_booked(4, [[0, 8], [1, 4], [3, 4], [2, 3]]))  # Output: 1










