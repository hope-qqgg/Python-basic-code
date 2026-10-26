class Duck:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"Duck: {self.age} 岁 {self.name} 的正在游泳")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"Dog: {self.age} 岁 {self.name} 的正在游泳")

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"Pig: {self.age} 岁 {self.name} 的正在游泳")

def go_swimming(duck):
    duck.swimming()

# 测试
if __name__ == "__main__":
    go_swimming(Dog("旺财",4))
    go_swimming(Duck("唐老鸭",2))
    go_swimming(Pig("佩奇",1))