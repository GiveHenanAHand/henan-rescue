import jieba

file1 = open(r'data.csv', 'r', encoding='utf-8')

lines = file1.readlines()

true_information = []
fake_information = []

for idx, line in enumerate(lines):
    classes = line.split(',')[7].strip()
    validation = line.split(',')[9].strip()
    if classes.startswith("求救"):
        #print(idx)
        #print(classes)
        true_information.append(idx)
    elif classes.startswith("帮助"):
        #print(idx)
        #print(classes)
        true_information.append(idx)
    elif classes.startswith("其他"):
        #print(idx)
        #print(classes)
        true_information.append(idx)
    if validation == "否":
        #print(idx)
        #print(validation)
        fake_information.append(idx)

# raise Exception('!')
print(len(true_information))
print(len(fake_information))

file1.close()

file1 = open(r'data.csv', 'r', encoding='utf-8')

lines = file1.readlines()

true_words_dictionary = {}
fake_words_dictionary = {}

total_true = 0
total_false = 0

for idx, line in enumerate(lines):
    # if idx == 0:
    #     continue
    tmp_line = line.split(',')[5].strip()
    # print(idx-1)
    # print(tmp_line)
    # print(" ")
    if idx in true_information:
        seg_list = jieba.cut(tmp_line, cut_all=False, HMM=True)
        split_line = " ".join(seg_list).split()
        for words in split_line:
            for word in words:
                if u'\u4e00' <= word <= u'\u9fff':
                    total_true += 1
                    if true_words_dictionary.get(words) == None:
                        true_words_dictionary[words] = 1
                    else:
                        true_words_dictionary[words] += 1
                    # print(words)
                    break
    if idx in fake_information:
        seg_list = jieba.cut(tmp_line, cut_all=False, HMM=True)
        split_line = " ".join(seg_list).split()
        for words in split_line:
            for word in words:
                if u'\u4e00' <= word <= u'\u9fff':
                    total_false += 1
                    if fake_words_dictionary.get(words) == None:
                        fake_words_dictionary[words] = 1
                    else:
                        fake_words_dictionary[words] += 1
                    # print(words)
                    break
    # if idx == 10:
    #     print(true_words_dictionary)
    #     print(fake_words_dictionary)
    #     break

print(total_true)
print(total_false)

true_order = sorted(true_words_dictionary.items(), key=lambda x: x[1], reverse=True)
fake_order = sorted(fake_words_dictionary.items(), key=lambda x: x[1], reverse=True)

file2 = open(r'dict.txt', 'w', encoding='utf-8')

for true_tuple in true_order:
    name = true_tuple[0]
    number = true_tuple[1]
    signal = False
    for fake_tuple in fake_order:
        if name == fake_tuple[0]:
            signal = True
            ratio = (number/fake_tuple[1])/(total_true/total_false)
            if ratio>2:
                file2.write(name)
                file2.write("   ")
                file2.write(str(ratio))
                file2.write("\n")
                print(name, ratio)
            break
    if signal == False:
        # if number >= 3:
        #     file2.write(name)
        #     file2.write("   ")
        #     file2.write(str(number/(total_true/total_false)))
        #     file2.write("\n")
        #     print(name, number/(total_true/total_false))
        if number >= 3:
            file2.write(name)
            file2.write("   ")
            file2.write(str(number/2))
            file2.write("\n")
            print(name, number/2)

print("---Split line---")
for fake_tuple in fake_order:
    name = fake_tuple[0]
    number = fake_tuple[1]
    signal = False
    for true_tuple in true_order:
        if name == true_tuple[0]:
            signal = True
            ratio = (true_tuple[1]/number)/(total_true/total_false)
            if ratio<0.5:
                file2.write(name)
                file2.write("   ")
                file2.write(str(ratio))
                file2.write("\n")
                print(name, ratio)
            break
    if signal == False:
        # if number >= 3:
        #     file2.write(name)
        #     file2.write("   ")
        #     file2.write(str((1/number)/(total_true/total_false)))
        #     file2.write("\n")
        #     print(name, (1/number)/(total_true/total_false))
        if number >= 3:
            file2.write(name)
            file2.write("   ")
            file2.write(str(2/number))
            file2.write("\n")
            print(name, 2/number)



# print(true_words_dictionary)
# print(fake_words_dictionary)



file1.close()
file2.close()