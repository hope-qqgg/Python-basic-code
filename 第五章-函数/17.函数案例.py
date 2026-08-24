# 1.定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积=底*高／2）
def triangle_area(d,h):
    """
    根据传入的底和高计算三角形面积
    :param d: 三角形的底
    :param h: 三角形的高
    :return: 三角形面积
    """
    return round(d * h / 2,1)
print(f"底为 5，高为 10的三角形的面积为：{triangle_area(5,10)}") # 输出：底为 5，高为 10的三角形的面积为：25.0

# 2.定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
def vowel_len(letter_srt):
    """
    计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
    :param letter_srt: 传入的字符串
    :return: 传入的字符串中元音字母的个数
    """
    vowel_len = 0
    for i in letter_srt:
        if i in "aeiouAEIOU":
            vowel_len +=1
    return vowel_len
print(vowel_len("Hello-Python-world")) # 输出：4

# 3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
def processing_list(new_liet):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）
    :param new_liet: 班级学员高考成绩列表
    :return: 班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）
    """
    list_max = max(new_liet)
    list_min = min(new_liet)
    list_avg = round(sum(new_liet) / len(new_liet),1)
    print(f"最高分：{list_max}、\n最低分：{list_min}、\n平均分：{list_avg}")
    return list_max,list_min,list_avg
processing_list([690,588,700,300,343,490])