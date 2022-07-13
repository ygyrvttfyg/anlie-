'''
项目:代码实例
文件名:ball
制作人:"黄涛"
date:2022/2/12
'''
import pygame
# 初始化pygame模块
pygame.init()
# 定义窗口的大小
width,height = 900,600
# 初始化一个画布
screen=pygame.display.set_mode((width,height))
# 读取乒乓球图片大小，并优化格式
ball = pygame.image.load('OIP-C.jpg').convert_alpha()
ball = pygame.transform.scale(ball, [50, 50])

clock = pygame.time.Clock()
# 定义循环条件
running = True
position = ball.get_rect(x=50, y=100)
speed = [2, 2]
# 制作球拍
plate = pygame.Surface([100, 20])
plate.fill([255, 0, 0])
plate_position = plate.get_rect(x=400, y=500)
# 音效
fail_sound = pygame.mixer.Sound('fail.mp3')
kill_sound = pygame.mixer.Sound('successed.mp3')
file = 'D:/666666/代码实例/乒乓球/bgm.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
# 积分
count = 0
# playing代表在游戏中
# lose代表输掉了比赛
status = 'playing'
# 循环
while running:
    # 将画布填充为黑色
    screen.fill([0, 255, 0])
    # 循环处理接受到的事件,包括键盘，鼠标，窗口等等事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # 显示得分
    font = pygame.font.SysFont('simhei', 36)
    text = font.render(f"击杀：{count}", 1, (255, 255, 255))
    screen.blit(text, text.get_rect(x=10, y=10))

    if status == 'playing':
        if keys[pygame.K_LEFT] and plate_position.left > 0:
            # 左方向被按下
            plate_position.x -= 10
        elif keys[pygame.K_RIGHT] and plate_position.right < width:
            # 右方向被按下
            plate_position.x += 10
        if plate_position.colliderect(position):
            # 如果球拍碰到了乒乓球
            speed[1] *= -1
            count += 1
            kill_sound.play()
        if position.bottom > height:
            status = 'lose'

        # position.x += speed[0]  #x轴的移动
        # position.y += speed[图片转字符画] # y轴的移动
        position = position.move(speed)

        if position.right > width or position.left < 0:
            speed[0] *= -1
        if position.bottom > height or position.top < 0:
            speed[1] *= -1
    elif status == 'lose':
        text = font.render(f'你已被雷总击杀', 1, (255, 255, 255))
        screen.blit(text,text.get_rect(center=screen.get_rect().center))
        fail_sound.play()
    # 绘制乒乓球图片
    screen.blit(ball, position)
    # 绘制球拍
    screen.blit(plate, plate_position)
    # 更新屏幕
    pygame.display.update()
    # 控制乒乓球运动最大速度
    clock.tick(100)


