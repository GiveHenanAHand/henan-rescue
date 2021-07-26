import jieba

file1 = open(r'data.csv', 'r', encoding='utf-8')
file2 = open(r'dict.txt', 'r', encoding='utf-8')

dict_word_calculate = {}

lines = file2.readlines()
for line in lines:
    name = line.strip().split()[0]
    number = float(line.strip().split()[1])
    dict_word_calculate[name] = number
# print(dict_word_calculate)

lines = file1.readlines()

for idx, line in enumerate(lines):
    if idx == 0:
        continue
    tmp_line = line.split(',')[5]

    word_list = []

    seg_list = jieba.cut(tmp_line, cut_all=False, HMM=True)
    split_line = " ".join(seg_list).split()
    # print(split_line)
    for words in split_line:
        for word in words:
            if u'\u4e00' <= word <= u'\u9fff':
                word_list.append(words)
                break

    # print(word_list)
    result = 1
    for words in word_list:
        if dict_word_calculate.get(words) != None:
            # print(words)
            # print(dict_word_calculate.get(words))
            # print(result)
            result = result * dict_word_calculate.get(words)

    if result < 1:
        print(idx+1)
        print(line.split(',')[5])

    # print(result)
    # if idx == 1:
    #     break

file1.close()
file2.close()
