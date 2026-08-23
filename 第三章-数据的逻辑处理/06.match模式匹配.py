# match...case 模式匹配：工作日程安排
day = int(input("请输入星期几（1~7）:"))
match day:
    case 1:
        print("星期一：工作会议")
    case 2:
        print("星期二学习培训日")
    case 3:
        print("星期三：项目开发日")
    case 4:
        print("星期四：代码审查日")
    case 5:
        print("星期五：总结规划日")
    case 6 | 7:
        print("周末：休息日")
    case _: # 匹配其他所有情况
        print("输入错误")
print("------------------------------")

# 案例：基于match...case 实现一个简单的计算器，可以实现 + - * / 运算，用户输入需要运算的两个数以及运算符之后，可以进行计算。
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
operator = input("请输入运算符（+ - * /）：")
match operator:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("输入错误")
print("------------------------------")

# 练习：请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作（输出控制台）。
"""
    具体规则:
        玩家输入                      对应动作
        上/w/W                       角色向上移动
        下/s/S                       角色向下移动
        左/a/A                       角色向左移动
        右/d/D                       角色向右移动
        跳/""(空格)                   角色跳趺
        攻击／ⅰ／J                   角色发动攻击
        退出/esc /ESC                角色退出游戏
"""
direction = input("请输入指令：")
match direction:
    case "上" | "w" | "W":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左" | "a" | "A":
        print("角色向左移动")
    case "右" | "d" | "D":
        print("角色向右移动")
    case "跳" | "" | " ":
        print("角色跳趺")
    case "攻击" | "ⅰ" | "J":
        print("角色发动攻击")
    case "退出" | "esc" | "ESC":
        print("角色退出游戏")
    case _:
        print("输入错误")
