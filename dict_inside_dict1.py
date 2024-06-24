def keyword_index(docs):
    # implement this
    for index,each_string in enumerate(docs):
        for each_word in each_string.split():
            print(each_word)
            if final_result.get(each_word,0) ==0:
                inside_dict={index:1}
            else:
                inside_dict=inside_dict.upf


docs = ["Hello world", "world of python", "python is a snake"]

inside_dict = {}
final_dict = {}
d1=
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}