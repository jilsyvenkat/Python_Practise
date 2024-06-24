import re
def find_possibility(input_list):
    red_max_cnt = 12
    green_max_cnt = 13
    blue_max_cnt = 14
    greent_cnt = 0
    blue_cnt = 0
    red_cnt = 0
    print("input members", input_list)
    members = (input_list.split(';'))
    print("members",members)
    print(len(members))

    for i in range(0,len(members)-1,1) :
        possible_flag = True
        # color_members = members[i-1].split(',')
        print("color_members",members)
        for i in members:
            print(i)
            member = i.split(' ')
            print(member)
            # member = member.lstrip()
            # color_and_member = member[i-1].split(' ')

            if member[1] == 'green' and int(member[0]) > green_max_cnt:
                print("green value higher than max")
                return False
            elif member[1] == 'blue' and int(member[0]) > blue_max_cnt:
                print("blue value higher than max")
                return False
            elif member[1] == 'red' and int(member[0]) > red_max_cnt:
                print("red value higher than max")
                return False

        return possible_flag

with open('day2_test_data.txt', 'r') as file:
    # Loop through each line in the file
    t_line = []
    comma_separated_list=[]
    cnt = 0
    for line in file:
        possible_flag = False
        cnt += 1
        print("cnt",cnt)
        stripped_line = (line.strip()).split(': ')
        possible_flag = find_possibility(stripped_line[1])
        stripped_line[0] = cnt
        if possible_flag:
            print("stripped_line",stripped_line[0])
            t_line.append(int(stripped_line[0]))
    print(t_line)
    print(sum(t_line))