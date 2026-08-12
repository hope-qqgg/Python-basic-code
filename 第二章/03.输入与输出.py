# 获取键盘上输入的数据 --- input(...)
name = input("请输入你的名字：")
age = input("请输入你的年龄：")
print(f"{name}你好，你的年龄是{age}。")
print("------------------------------\n")

# 需求：需求：小智的银行卡中有10000元，现在到ATM进行取钱操作，请根据输入的金额执行取钱操作，取钱完毕后，展示其银行卡余额。
balance = 10000
password = input("请输入你的密码：")
money = int(input("请输入你要取的钱数："))
balance = balance - money
print(f"取钱完毕，你的银行卡余额是{balance}元。")
print("------------------------------\n")

# 需求：根据用户输入的两个数字，计算两个数之和，并将其输出到控制台。
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
sum = num1 + num2
print(f"两个数字之和是{sum}。")

