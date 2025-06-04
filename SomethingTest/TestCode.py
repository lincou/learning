class Ship:
    def __init__(self, game):
        self.game = game  # Ship 类的实例保存对 Game 类实例的引用
        self.position = (0, 0)  # 假设船的初始位置是 (0, 0)

class Game:
    def __init__(self):
        self.ship = Ship(self)  # 创建一个 Ship 对象，并将当前 Game 对象传递给 Ship 的构造方法