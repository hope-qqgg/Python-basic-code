class Car:
    def __init__(self,brand,model,color,owner):
        self.color = color # 颜色(公有属性)
        self.brand = brand # 品牌(公有属性)
        self.model = model # 型号(公有属性)
        self.__owner = owner # 拥有者(私有属性)

    def start(self): # 启动
        print(f"{self.brand} {self.model} 正在启动...")

    def run(self): # 行驶
        print(f"{self.__owner}:{self.brand} {self.model} 正在行驶...")
        self.__control_fuel()

    def stop(self): # 停止
        print(f"{self.brand} {self.model} 停止行驶...")

    def __control_fuel(self): # 私有方法
        print(f"{self.brand} {self.model} 控制油门...")

    def get_owner(self):
        return self.__owner[0] + "**"

    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料...")

# 燃油车
class FuelCar(Car):
    def charge(self):
        # 方法一：super().方法名()
        super().charge()
        # 方法二：类名.方法名(self)
        Car.charge(self)
        print(f"{self.brand} {self.model} 正在加油...")

# 电车
class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电...")


if __name__ == "__main__":
    c1 = FuelCar("BMW","X5","黑色","HOPE")
    c1.charge()
    c2 = ElectricCar("XiaoMi", "1", "黑色", "HOPE")
    c2.charge()