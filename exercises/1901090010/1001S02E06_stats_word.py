import re
#(1)定义一个名为 stats_text_en 的函数
def stats_text_en(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    #(3)统计参数中每个英文单词出现的次数
    # 1.替换掉所有的符号
    word_str = text.replace(','," ").replace('.'," ").replace('!'," ").replace('*'," ").replace('--'," ")
    # 2.按照空格将所有的单词分割开
    word_list = word_str.split()
    # 3.对单词进行去重操作，作为字典的key
    word_one = set(word_list)
    # 4.构建一个词频字典
    dict = {}
    for word in word_one:
        dict[word] = word_list.count(word)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list


#(1)定义一个名为 stats_text_en 的函数
def stats_text_cn(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.替换掉所有的符号
    d = text.replace(',','').replace('-',' ').replace('.','').replace(':','').replace('《','').replace(';','').replace('"','').replace('!','').replace('?','').replace('》',' ').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','').replace("'",'')
    # 2.将上文中的字符串，用正则运算剔除所有英文字母单词，数字
    d = re.sub("[A-Za-z0-9]", "", d)
    print(d)

    # 3.将字符串中的汉字去重，作为字典的key  
    d_list = list(d)
    print(d_list)
    d_index = set(d_list)
    # 4.构造词频字典
    dict = {}
    for i in d_index:
        dict[i] = d_list.count(i)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list 


if __name__ == "__main__":
    # 测试统计英文单词词频的函数
    text = '''
    Fall Day (by J. B. Leishman)
 
Lord, it is time. This was a very big summer.
Lay your shadows over the sundial,
and let the winds loose on the fields.
Command the last fruits to be full;
give them two more sunny days,
urge them on to fulfillment and throw
the last sweetness into the heavy wine.
Who has no house now, will never build one.
Whoever is alone now, will long remain so,
Will watch, read, write long letters
and will wander in the streets, here and there
restlessly, when the leaves blow.
    '''
    # 测试不是字符串的情况
    test_num = 1
    # 测试正常情况
    array = stats_text_en(text)
    print(array)

 # 测试统计中文词频的函数
    text = '''
    English : Fall Day by J. B. Leishman
Lord, it is time. This was a very big summer.
Lay your shadows over the sundial,
and let the winds loose on the fields.
Command the last fruits to be full;
give them two more sunny days,
urge them on to fulfillment and throw
the last sweetness into the heavy wine.
Who has no house now, will never build one.
Whoever is alone now, will long remain so,
Will watch, read, write long letters
and will wander in the streets, here and there
restlessly, when the leaves blow.
中译一：《秋日》 冯至
1905-1993。著名诗人、翻译家。
主啊！是时候了。夏日曾经很盛大。
把你的阴影落在日规上，
让秋风刮过田野。
让最后的果实长得丰满，
再给它们两天南方的气候，
迫使它们成熟，
把最后的甘甜酿入浓酒。
谁这时没有房屋，就不必建筑，
谁这时孤独，就永远孤独，
就醒着，读着，写着长信，
在林荫道上来回
不安地游荡，当着落叶纷飞。
    '''
    # 对统计中文词频函数进行测试
    array = stats_text_cn(text)
    print(array)