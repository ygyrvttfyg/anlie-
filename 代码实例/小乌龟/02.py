'''
项目:代码实例
文件名:02
制作人:"黄涛"
date:2022/2/19
'''
import pygame
import sys
# 初始化pygame
pygame.init()
# 游戏参数
size = width, height = 600, 600
speed = [1, 2]
sign = False
ratio = 1.0
# 创建窗口
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen.fill((0, 0, 0))
# 加载图像,优化大小
background = pygame.image.load('Background.png').convert()
background = pygame.transform.scale(background, [1024, 768])
o_roles = pygame.image.load('roles.png')
o_roles = pygame.transform.scale(o_roles, [100, 100])
roles = o_roles
# 获取图像的矩形位置
position = roles_rect = o_roles_rect = o_roles.get_rect()
# 设置循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        keys = pygame.key.get_pressed()
        # 全屏（a）
        if keys[pygame.K_a]:
            sign = not sign
            if sign:
                size = width, height = 1280, 800
                screen = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.HWSURFACE)
            else:
                screen = pygame.display.set_mode(size)
        # 用户调整窗口大小
        # 控制人物
        # (图片转字符画) 放大，缩小人物（=，-），空格恢复原始大小
        if keys[pygame.K_EQUALS] or keys[pygame.K_MINUS] or keys[pygame.K_SPACE]:
            if keys[pygame.K_EQUALS] and ratio < 2:
                ratio += 0.1
            elif keys[pygame.K_MINUS] and ratio > 0.5:
                ratio -= 0.1
            elif keys[pygame.K_SPACE]:
                ratio = 1.0
            roles = pygame.transform.smoothscale(o_roles,
                                                 (int(o_roles_rect.width * ratio),
                                                  int(o_roles_rect.height * ratio)))
        # (2)方向
        if keys[pygame.K_LEFT] and position.left > 0:
            # 左方向被按下
            speed[0] = -1
            # 翻转图像
            roles = pygame.transform.flip(roles, True, False)
        elif keys[pygame.K_RIGHT] and position.right < width:
            # 右方向被按下
            speed[0] = 1
            # 翻转图像
            roles = pygame.transform.flip(roles, True, False)
        elif keys[pygame.K_UP] and position.top > 0:
            # 上方向被按下
            speed[1] = -1
        elif keys[pygame.K_DOWN] and position.bottom < height:
            # 下方向被按下
            speed[1] = 1
    # 移动图像
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        # 翻转图像
        roles = pygame.transform.flip(roles, True, False)
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    # 更新图像
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(roles, position)
    # 更新界面
    pygame.display.flip()
