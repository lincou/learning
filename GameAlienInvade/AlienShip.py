# 在游戏《外星人入侵》中，玩家控制一艘最初出现在屏幕底部中央的飞船。玩
# 家可以使用箭头键左右移动飞船，还可使用空格键射击。游戏开始时，一群外
# 星人出现在天空中，并向屏幕下方移动。玩家的任务是射杀这些外星人。玩家
# 将所有外星人都消灭干净后，将出现一群新的外星人，其移动速度更快。只要
# 有外星人撞到玩家的飞船或到达屏幕底部，玩家就损失一艘飞船。玩家损失三
# 艘飞船后，游戏结束

#第一步，将创建一艘飞船，它可左右移动，并且能在用户按空格键时开火。
import sys 
import pygame 
from settings import Settings
from ship import Ship


class AlienInvasion: 
    """管理游戏资源和行为的类""" 
    def __init__(self): 
        """初始化游戏并创建游戏资源。""" 
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion") 
        self.ship = Ship(self)
        

         #设置背景色。 
        self.bg_color = self.settings.bg_color
    def run_game(self): 
        """开始游戏的主循环""" 
        while True:
             # 监视键盘和鼠标事件。
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            # 绘制背景颜色。
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            # 让最近绘制的屏幕可见。
            pygame.display.flip()

if __name__ == '__main__': 
      # 创建游戏实例并运行游戏。 
      ai = AlienInvasion() 
      ai.run_game() 