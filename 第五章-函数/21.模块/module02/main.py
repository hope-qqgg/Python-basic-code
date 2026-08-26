# # 导入自定义模块
# import my_fun
#
# # 使用模块中的功能
# print(my_fun.PI)
# print(my_fun.NAME)
#
# my_fun.log_separator1()
# my_fun.log_separator2()
# my_fun.log_separator3()
# my_fun.log_separator4()

# 导入自定义模块中的功能
# from my_fun import log_separator1,log_separator3,PI,NAME
from my_fun import *

# 使用模块中的功能
print(PI)
print(NAME)

log_separator1()
log_separator2()
log_separator3()
log_separator4()