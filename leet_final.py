def new_fn(list_of_values):
    len_of_list = len(list_of_values)
    list_of_values1=list_of_values
    diff = -1
    new_list=list_of_values
    list_of_values_for_i=new_list
    new_list =  []
    new_big_list = [[] for _ in range(1)]
    new_big_list[0]= list_of_values
    while diff !=0:
        new_list = []
        for i in range(0,len(list_of_values_for_i)-1):
            new_list.append(list_of_values_for_i[i+1]-list_of_values_for_i[i])
        new_big_list.append(new_list)
        list_of_values_for_i=new_list
        all_same = all(element == new_big_list[-1][0] for element in new_big_list[-1][1:])
        if all_same:
            new_big_list[-1].insert(0,new_big_list[-1][0] )
            diff = 0
            for i in range(len(new_big_list) - 1, 0, -1):
                new_big_list[i - 1].append(
                new_big_list[i - 1][len(new_big_list[i - 1]) - 1] + new_big_list[i][len(new_big_list[i]) - 1])
            for i in range(len(new_big_list) - 1, 0, -1):
                new_big_list[i-1].insert(0,
                        new_big_list[i-1][0] - new_big_list[i][0])

            print(new_big_list)
            return new_big_list


with open('leet_test.txt', 'r') as file:
    # Loop through each line in the file
    sum=0
    sum_first=0
    comma_separated_list=[]
    for line in file:
        stripped_line = line.strip()
        space_separated_values = stripped_line.split()
        int_values = [int(value) for value in space_separated_values]
        x = new_fn(int_values)
        sum=sum + x[0][-1]
        sum_first=sum_first+x[0][0]
    print("sum is ",sum)
    print("sum_first",sum_first)
