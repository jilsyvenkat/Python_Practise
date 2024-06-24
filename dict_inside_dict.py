def keyword_index(docs):
    # implement this
    final_result = {}
    fr_jj = {}

    for index1, each_doc in enumerate(docs):

        print(each_doc.split())
        each_word_list = each_doc.split()
        cnt = 0
        for each_word_index in range(len(each_word_list)):
            print("each_word_list[each_word_index]",each_word_list[each_word_index])
            print("each_word_index", each_word_index)
            if final_result.get(each_word_list[each_word_index]) != None :
                print(f"{each_word_list[each_word_index]} alerady found", each_word_list[each_word_index])
                cnt +=1
                final_result[each_word_list[each_word_index]][index1] = cnt
            else:
                final_result[each_word_list[each_word_index]] = {index1:1}
    return final_result


docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(
    docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}