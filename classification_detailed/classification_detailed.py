import jieba

file1 = open(r'data.csv', 'r', encoding='utf-8')

lines = file1.readlines()

true_information_need_help = []
true_information_offer_help = []
true_information_other = []

for idx, line in enumerate(lines):
    classes = line.split(',')[7].strip()
    if classes.startswith("求救"):
        #print(idx)
        #print(classes)
        true_information_need_help.append(idx)
    elif classes.startswith("帮助"):
        #print(idx)
        #print(classes)
        true_information_offer_help.append(idx)
    elif classes.startswith("其他"):
        #print(idx)
        #print(classes)
        true_information_other.append(idx)

print(len(true_information_need_help))
print(len(true_information_offer_help))
print(len(true_information_other))

file1.close()

file1 = open(r'data.csv', 'r', encoding='utf-8')

lines = file1.readlines()

true_information_need_help_dict = {}
true_information_offer_help_dict = {}
true_information_other_dict = {}

total_need_help = 0
total_offer_help = 0
total_other = 0

for idx, line in enumerate(lines):
    # if idx == 0:
    #     continue
    tmp_line = line.split(',')[5].strip()
    # print(idx-1)
    # print(tmp_line)
    # print(" ")
    if idx in true_information_need_help:
        seg_list = jieba.cut(tmp_line, cut_all=False, HMM=True)
        split_line = " ".join(seg_list).split()
        for words in split_line:
            for word in words:
                if u'\u4e00' <= word <= u'\u9fff':
                    total_need_help += 1
                    if true_information_need_help_dict.get(words) == None:
                        true_information_need_help_dict[words] = 1
                    else:
                        true_information_need_help_dict[words] += 1
                    # print(words)
                    break

    if idx in true_information_offer_help:
        seg_list = jieba.cut(tmp_line, cut_all=False, HMM=True)
        split_line = " ".join(seg_list).split()
        for words in split_line:
            for word in words:
                if u'\u4e00' <= word <= u'\u9fff':
                    total_offer_help += 1
                    if true_information_offer_help_dict.get(words) == None:
                        true_information_offer_help_dict[words] = 1
                    else:
                        true_information_offer_help_dict[words] += 1
                    # print(words)
                    break

    if idx in true_information_other:
        seg_list = jieba.cut(tmp_line, cut_all=False, HMM=True)
        split_line = " ".join(seg_list).split()
        for words in split_line:
            for word in words:
                if u'\u4e00' <= word <= u'\u9fff':
                    total_other += 1
                    if true_information_other_dict.get(words) == None:
                        true_information_other_dict[words] = 1
                    else:
                        true_information_other_dict[words] += 1
                    # print(words)
                    break

    # if idx == 10:
    #     print(true_words_dictionary)
    #     print(fake_words_dictionary)
    #     break

print(total_need_help)
print(total_offer_help)
print(total_other)

true_information_need_help_dict = sorted(true_information_need_help_dict.items(), key=lambda x: x[1], reverse=True)
true_information_offer_help_dict = sorted(true_information_offer_help_dict.items(), key=lambda x: x[1], reverse=True)
true_information_other_dict = sorted(true_information_other_dict.items(), key=lambda x: x[1], reverse=True)

file2 = open(r'Need_help_dict.txt', 'w', encoding='utf-8')
file3 = open(r'Offer_help_dict.txt', 'w', encoding='utf-8')
file4 = open(r'Other_dict.txt', 'w', encoding='utf-8')

for need_help_tuple in true_information_need_help_dict:
    name = need_help_tuple[0]
    number = need_help_tuple[1]
    ratio = number/total_need_help*1000
    # print(ratio)
    file2.write(name)
    file2.write("   ")
    file2.write(str(ratio))
    file2.write("\n")

for offer_help_tuple in true_information_offer_help_dict:
    name = offer_help_tuple[0]
    number = offer_help_tuple[1]
    ratio = number/total_offer_help*1000
    # print(ratio)
    file3.write(name)
    file3.write("   ")
    file3.write(str(ratio))
    file3.write("\n")

for other_tuple in true_information_other_dict:
    name = other_tuple[0]
    number = other_tuple[1]
    ratio = number/total_other*1000
    #print(ratio)
    file4.write(name)
    file4.write("   ")
    file4.write(str(ratio))
    file4.write("\n")

file1.close()
file2.close()
file3.close()
file4.close()