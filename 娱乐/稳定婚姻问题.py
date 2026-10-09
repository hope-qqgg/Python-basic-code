# Gale-Shapley 算法
# 这个算法极其聪明，核心策略是：男生主动出击，女生择优录取（渣男/渣女策略）。
# 1. 求婚阶段：所有单身男生，按照自己心里的排名，依次向女生表白。
# 2. 择优阶段：女生面对表白，分两种情况：
#    · 如果单身：暂时接受。
#    · 如果有对象：对比新表白者和现男友，谁排名高就选谁。如果选了新欢，旧爱就被甩了，变成单身汉，继续去表白别人。
# 3. 循环往复：直到所有男生都脱单（或表白完所有女生），算法结束。

def stable_marriage(men_pref, women_pref):
    """
    men_pref: 男生偏好字典，例如 {'A': ['a', 'b', 'c'], ...}
    women_pref: 女生偏好字典，例如 {'a': ['A', 'B', 'C'], ...}
    """
    n = len(men_pref)

    # 记录当前女生和谁在一起
    engaged = {}  # {'女生': '男生'}

    # 记录每个男生表白到了第几个女生（指针）
    next_choice = {man: 0 for man in men_pref}

    # 单身男生队列
    free_men = list(men_pref.keys())

    while free_men:
        man = free_men.pop(0)  # 取一个单身汉

        # 如果他还没向所有女生表白完
        if next_choice[man] < n:
            woman = men_pref[man][next_choice[man]]
            next_choice[man] += 1

            if woman not in engaged:
                # 女生单身，直接接受
                engaged[woman] = man
            else:
                # 女生有对象，比较谁更好
                current_man = engaged[woman]
                # 如果女生更喜欢新来的男生
                if women_pref[woman].index(man) < women_pref[woman].index(current_man):
                    # 换人，甩掉现男友
                    engaged[woman] = man
                    free_men.append(current_man)  # 现男友变回单身
                else:
                    # 女生拒绝新男生，新男生继续单身
                    free_men.append(man)

    # 反转字典，方便输出男生配了谁
    result = {man: woman for woman, man in engaged.items()}
    return result


# 测试数据
men_pref = {
    '男1': ['女A', '女B', '女C'],
    '男2': ['女B', '女A', '女C'],
    '男3': ['女A', '女B', '女C']
}

women_pref = {
    '女A': ['男2', '男1', '男3'],
    '女B': ['男1', '男2', '男3'],
    '女C': ['男1', '男2', '男3']
}

print(stable_marriage(men_pref, women_pref))