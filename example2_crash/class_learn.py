class Dog():
    """狗的类"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """下蹲动作"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """打滚"""
        print(self.name.title() + " rolled over")


if __name__ == "__main__":
    my_dog = Dog('gugu', 5)
    your_dog = Dog('gege', 2)
    my_dog.sit()
    your_dog.roll_over()
    print(my_dog.name.title())
