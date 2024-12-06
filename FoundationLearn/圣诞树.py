import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 设定常量
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # 黑色背景
PARTICLE_COLOR = (255, 255, 0)  # 粒子的颜色（黄色）
PARTICLE_COUNT = 300  # 粒子的数量

# 定义粒子类
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)  # 粒子的大小
        self.lifetime = random.randint(30, 60)  # 粒子的生存时间
        self.brightness = random.randint(100, 255)  # 亮度

    def update(self):
        # 粒子随着时间逐渐消失
        self.lifetime -= 1
        self.brightness = max(0, self.brightness - 4)  # 逐渐减小亮度

    def is_alive(self):
        return self.lifetime > 0

    def draw(self, surface):
        if self.is_alive():
            color = (PARTICLE_COLOR[0], PARTICLE_COLOR[1], self.brightness)
            pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size)

def generate_tree_particles():
    particles = []
    # 生成树的形状
    for i in range(PARTICLE_COUNT):
        # 随机位置生成粒子
        x = random.randint(325, 475)
        # 根据Y轴位置的不同，可以生成树的形状
        y = random.randint(200, 400 - (x - 400) // 3)  # 控制Y位置
        particles.append(Particle(x, y))
    return particles

# 主循环
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("闪光粒子圣诞树特效")
    clock = pygame.time.Clock()

    particles = generate_tree_particles()  # 生成圣诞树的粒子

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 更新粒子
        for particle in particles:
            particle.update()
        
        # 清楚已消亡的粒子
        particles = [particle for particle in particles if particle.is_alive()]

        # 刷新画面
        screen.fill(BACKGROUND_COLOR)

        # 绘制圣诞树粒子
        for particle in particles:
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
