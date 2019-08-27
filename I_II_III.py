#读取文件
f = open("C:/Users/01/Desktop/aaa.txt", "r", encoding='UTF-8')                           #设置文件对象
data = f.readlines()                                                         #直接将文件中按行读到list里，效果与方法2一样
f.close()                                           #关闭文件
print(data)


#统计词数

s = str(data)
ls = s.split(" ")
print('一共有', len(ls), '个单词！')


#统计词频
def count_words(s, n):
    s_list = list(s.split(" "))
    s_count = {a: s_list.count(a) for a in s_list}
    s_sorted = sorted(s_count.items(), key=lambda x: x[1], reverse=True)
    top_n = s_sorted[:n]
    print('其中不重复的单词有：', len(top_n), '个！')
    return top_n

print("句子中从高到低的词频顺序是：{}".format(count_words(str(data), len(ls))))