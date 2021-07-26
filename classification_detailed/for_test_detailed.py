import jieba

file1 = open(r'data.csv', 'r', encoding='utf-8')
file2 = open(r'Need_help_dict.txt', 'r', encoding='utf-8')
file3 = open(r'Offer_help_dict.txt', 'r', encoding='utf-8')
file4 = open(r'Other_dict.txt', 'r', encoding='utf-8')

true_information_need_help_dict = {}
true_information_offer_help_dict = {}
true_information_other_dict = {}

lines = file2.readlines()
for line in lines:
    name = line.strip().split()[0]
    number = float(line.strip().split()[1])
    true_information_need_help_dict[name] = number

lines = file3.readlines()
for line in lines:
    name = line.strip().split()[0]
    number = float(line.strip().split()[1])
    true_information_offer_help_dict[name] = number

lines = file4.readlines()
for line in lines:
    name = line.strip().split()[0]
    number = float(line.strip().split()[1])
    true_information_other_dict[name] = number

lines = file1.readlines()

for idx, line in enumerate(lines):
    if idx == 0:
        continue

    classes = line.split(',')[7].strip()
    if classes.startswith("求救") or classes.startswith("帮助") or classes.startswith("其他"):
        # print(classes)
        pass
    else:
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
    need_help_result = 1
    offer_help_result = 1
    other_result = 1

    for words in word_list:
        if true_information_need_help_dict.get(words) != None:
            # print(words)
            # print(dict_word_calculate.get(words))
            # print(result)
            need_help_result = need_help_result * true_information_need_help_dict.get(words)
        else:
            need_help_result = need_help_result * 0.07

        if true_information_offer_help_dict.get(words) != None:
            # print(words)
            # print(dict_word_calculate.get(words))
            # print(result)
            offer_help_result = offer_help_result * true_information_offer_help_dict.get(words)
        else:
            offer_help_result = offer_help_result * 0.2

        if true_information_other_dict.get(words) != None:
            # print(words)
            # print(dict_word_calculate.get(words))
            # print(result)
            other_result = other_result * true_information_other_dict.get(words)
        else:
            other_result = other_result * 0.2

    if need_help_result > offer_help_result:
        if need_help_result > other_result:
            result = "求救"
        else:
            result = "其他"
    else:
        if offer_help_result > other_result:
            result = "帮助"
        else:
            result = "其他"

    print(idx+1)
    print(line.split(',')[5])
    print("分类结果：", result)
    print("")

file1.close()
file2.close()
file3.close()
file4.close()
