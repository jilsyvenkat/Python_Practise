from typing import List


# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    S.sort()
    print(S)
    how_many_more_can_be_allocated = 0
    new_list = []
    first_seat = S[0]
    last_seat = S[-1]
    print(first_seat)
    print(last_seat)
    # Solve seats between 1 and first_seat
    social_distance = K + 1
    for i in range(first_seat-K-1 , 1, -K-1):
        print("In First Loop")
        print(i)
        seat_no = i
        print("New Seat:", seat_no)
        if seat_no >= 1 and seat_no<=first_seat-1 and seat_no not in S and seat_no not in new_list:
            new_list.append(seat_no)
    print("New list after first loop : ", new_list)
    # Solve seats between first_seat and next and next in loop
    previous_set=9999
    for i in range(0, len(S) - 1):
        start_seat_no = S[i]
        next_seat = S[i + 1]
        print("start_seat_no:", start_seat_no)
        print("next_seat:", next_seat)
        for j in range(next_seat-K-1, start_seat_no+1, -K-1):
            seat_no = j
            print("seat_no",j)
            if seat_no >= start_seat_no + K and seat_no <= next_seat-K and seat_no not in S and seat_no not in new_list:
                new_list.append(seat_no-1)
                previous_set = seat_no-1
    print("New list after second loop : ", new_list)
    # Solve seats between last_set and N
    for i in range(N , S[-1], -K-1):
        print(i)
        seat_no = i
        print("New Seat:", seat_no)
        if seat_no >= S[-1] + K+1 and seat_no <= N and seat_no not in S and seat_no not in new_list:
            new_list.append(seat_no)
    print("New list after third loop : ", new_list)
    how_many_more_can_be_allocated = len(new_list)
    print(how_many_more_can_be_allocated)
    return how_many_more_can_be_allocated


getMaxAdditionalDinersCount(15,2,3,[11,6,14])
# getMaxAdditionalDinersCount(10, 1, 2, [2, 6])
