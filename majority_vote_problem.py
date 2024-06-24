def elect_board_member(votes):
    # implement this
    count_dict = {}
    # print("len(votes):",len(votes))
    for vote in votes:
        # print("vote",vote)
        count_dict[vote] = count_dict.get(vote,0) + 1
        # print("count_dict[vote]",count_dict[vote])
        # print("len(votes)// 3",len(votes) / 3)
        if count_dict[vote] >= len(votes) / 3:
            # print("vote",vote)
            return vote
    return -1

print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1