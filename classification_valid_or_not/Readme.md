## 环境依赖

基于python3.8，然后需要装一个中文分词工具jieba。

```
pip install jieba
```

## 训练得到dict.txt

运行classification.py。基于词频统计做的分类，使用了最新的标注数据，然后把有效信息的高频词和无效信息的高频词分别提取出来，并将高频词出现的频率之比写入dict.txt。dict.txt中每个词对应的值越高，说明其越有可能出现在有效信息中。

## 应用

运行for_test.py，屏幕输出无效信息及在data.csv中对应的行数。