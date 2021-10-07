import pygame
import random
import turtle as T
import time
from turtle import mainloop, hideturtle

# 设置游戏屏幕大小 这是一个常量
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('from一个小哥哥')

file = r'哒哒哒哒.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()



# 画心
def draw_heart(size, color_):
    T.speed(0)
    T.colormode(255)
    T.color(color_)
    T.pensize(2)
    T.pendown()
    T.setheading(150)
    T.begin_fill()
    T.fd(size)
    T.circle(size * -3.745, 45)
    T.circle(size * -1.431, 165)
    T.left(120)
    T.circle(size * -1.431, 165)
    T.circle(size * -3.745, 45)
    T.fd(size)
    T.end_fill()


# 随机颜色，大小，位置画心
def draw():
	# 随机颜色
    colors1 = random.randint(0, 255)
    colors2 = random.randint(0, 255)
    colors3 = random.randint(0, 255)
    T.penup()
    # 随机位置
    x = random.randint(-400, 400)
    y = random.randint(-200, 200)
    T.goto(x, y)
    # 随机大小
    size = random.randint(10, 15)
    draw_heart(size, (colors1, colors2, colors3))


# 屏幕一函数
def screen1():
    hideturtle()
    T.setup(900, 500)
    # 更改心出现的个数
    for i in range(40):
        draw()
    T.penup()
    T.goto(-200, 0)
    T.color('Black')
    T.write('李雅璐xxxx！', font=('宋体', 60, 'normal'))
    #mainloop()

# 标题
def title(text, screen, scale, color=(255, 0, 0)):
    font = pygame.font.SysFont('SimHei', WIDTH//(len(text)*2))
    textRender = font.render(text, True, color)

    # # 获取此图片的矩形框
    # textRect = textRender.get_rect()
    # textRect.midtop = (WIDTH/scale[0], HEIGHT/scale[1])
    # screen.blit(textRender, textRect)

    # 初始化文字的坐标
    screen.blit(textRender, (WIDTH/scale[0], HEIGHT/scale[1]))


# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.SysFont('SimHei', 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    textRect.center = ((x+w/2), (y+h/2))
    screen.blit(textRender, textRect)

# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, 620), random.randint(20, 460)
    return x, y

# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('SimHei', WIDTH//(len(text) + 10))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH/2, HEIGHT/1.6)
    screen.blit(textRender, textRect)
    img = pygame.image.load("./image/3.png")
    imgRect = img.get_rect()
    imgRect.midtop = int(WIDTH / 1.9), HEIGHT // 20
    screen.blit(img, imgRect)

    pygame.display.update()
    while True:
      pygame.init()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
def Tree(branch, t):
    time.sleep(0.05)
    if branch > 3:
        if branch >= 8 and branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 2)
        else:
            t.color('sienna')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def screen3():
        t = T.Turtle()

        w = T.Screen()
        t.hideturtle()  # 隐藏画笔
        t.getscreen().tracer(5, 0)
        w.screensize(bg='wheat')
        t.left(90)
        t.up()
        t.backward(150)
        t.down()
        t.color('sienna')

        printer = T.Turtle()
        printer.hideturtle()
        printer.penup()
        printer.back(250)
#printer.write("七夕快乐!\n\n", align="right", font=("楷体", 16, "bold"))
#printer.write("           from 你的宝贝", align="center", font=("楷体", 12, "normal"))



        Tree(60, t)

        Petal(200, t)
        time.sleep(2)
        printer.write("我不去想身后会不会袭来寒风冷雨\n\n\n\n\n\n\n", align="center", font=("楷体", 16, "bold"))
        time.sleep(2)
        printer.write("既然目标是地平线\n\n\n\n\n\n", align="center", font=("楷体", 16, "bold"))
        time.sleep(2)
        printer.write("留给世界的只能是背影\n\n\n\n\n", align="center", font=("楷体", 16, "bold"))
        time.sleep(2)
        printer.write("我不去想未来是平坦还是泥泞\n\n\n", align="center", font=("楷体", 16, "bold"))
        time.sleep(2)
        printer.write("只要热爱生命\n\n", align="center", font=("楷体", 16, "bold"))
        time.sleep(2)
        printer.write("一切，都在意料之中\n", align="center", font=("楷体", 16, "bold"))
        w.exitonclick()
        t.mainloop()


def main():
    screen1()
    time.sleep(3)
    pygame.init()
    clock = pygame.time.Clock()
    unlike_pos_x = 330
    unlike_pos_y = 300
    unlike_pos_width = 80
    unlike_pos_height = 40
    unlike_color = (0, 191, 255)
    like_pos_x = 160
    like_pos_y = 300
    like_pos_width = 80
    like_pos_height = 40
    like_color = (0, 191, 255)
    running = True
    while running:
    # 填充窗口
        screen.fill((255, 255, 255))
        img = pygame.image.load("./image/2.png")
        imgRect = img.get_rect()
        imgRect.midtop = int(WIDTH / 1.2 ), HEIGHT // 7
        screen.blit(img, imgRect)
    # 获取坐标
        pos = pygame.mouse.get_pos()
        if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
           while True:
             unlike_pos_x, unlike_pos_y = get_random_pos()
             if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
                 continue
             break
        
        title('好久不见,这学期末', screen, scale=[5, 8])
        title('郑重地向你发出邀请，来哈尔滨玩吧', screen, scale=[5, 4])
        button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
        button('算了吧', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen)

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              pygame.display.flip()
              pygame.display.update()
              clock.tick(60)

        if pos[0] < like_pos_x + like_pos_width + 5 and pos[0] > like_pos_x - 5 and pos[1] < like_pos_y + like_pos_height + 5 and pos[1] > like_pos_y - 5:

            #show_like_interface('我就知道小姐姐你也喜欢我~', screen, color=(255, 0, 0))
            #pygame.quit()
            T.clear()
            T.reset()
            screen3()
            mainloop()
        else:
             pygame.display.flip()
             pygame.display.update()
             clock.tick(60)
        
            

       # pygame.display.flip()
        #pygame.display.update()
        #clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    main()
    input("please input any key to exit!")
