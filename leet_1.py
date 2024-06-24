def new_fn(list_of_values):
    len_of_list = len(list_of_values)
    list_of_values1=list_of_values
    diff = -1
    cnt=0
    new_list=list_of_values
    list_of_values_for_i=new_list
    new_list =  []
    new_big_list = [[] for _ in range(1)]
    new_big_list[0]= list_of_values
    while diff !=0:
        cnt+=1
        new_list = []
        for i in range(0,len(list_of_values_for_i)-1):
            new_list.append(list_of_values_for_i[i+1]-list_of_values_for_i[i])
        new_big_list.append(new_list)
        list_of_values_for_i=new_list
        new_list = []
        if list_of_values_for_i[1]==0:
            diff=0
    for i in range(len(new_big_list) - 2, 0, -1):
        new_big_list[i - 1].append(
            new_big_list[i - 1][len(new_big_list[i - 1]) - 1] + new_big_list[i][len(new_big_list[i]) - 1])
    return new_big_list

# Calling the function seperately for three inputs and then adding last values together
list1=[0,3,6,9,12,15]
list2=[1,3,6,10,15,21]
list3=[10,13,16,21,30,45]
list1_nextval=new_fn(list1)
list2_nextval=new_fn(list2)
list3_nextval=new_fn(list3)
total_of_three = list1_nextval[0][-1] + list2_nextval[0][-1] + list3_nextval[0][-1]
print("Total is ",str(list1_nextval[0][-1] + list2_nextval[0][-1] + list3_nextval[0][-1]))
if total_of_three == 114:
    print("You rocked it")