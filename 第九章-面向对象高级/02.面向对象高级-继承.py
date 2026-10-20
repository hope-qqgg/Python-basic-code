"""
    继承：描述的是两个类之间的关系，子类继承父类，就可以继承父类中的属性和方法（非私有）
"""
class Car: # 所有类的父类默认都是object
    def __init__(self,brand,model,color,owner):
        self.color = color # 颜色(公有属性)
        self.brand = brand # 品牌(公有属性)
        self.model = model # 型号(公有属性)
        self.__owner = owner # 拥有者(私有属性)

    def start(self): # 启动
        print(f"{self.brand} {self.model}正在启动...")

    def run(self): # 行驶
        print(f"{self.__owner}:{self.brand} {self.model}正在行驶...")
        self.__control_fuel()

    def stop(self): # 停止
        print(f"{self.brand} {self.model}停止行驶...")

    def __control_fuel(self): # 私有方法
        print(f"{self.brand} {self.model}控制油门...")

    def get_owner(self):
        return self.__owner[0] + "**"

# 燃油车
class FuelCar(Car):
    pass

# 电车
class ElectricCar(Car):
    pass

if __name__ == "__main__":
    c1 = FuelCar("BMW","X5","黑色","HOPE")
    print(c1.brand)
    print(c1.model)
    print(c1.color)
    c1.start()
    c1.run()
    c1.stop()
    c1.get_owner()
