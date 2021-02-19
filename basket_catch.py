import pygame as pg
import sys
import random
import time
#checking basket basket_positions
def basket_positions():
    global basket_x,basket_y,screen_width,screen_height,basket_width,basket_height
    if basket_x <= 0:
        basket_x = 0
    elif basket_x >= screen_width-basket_width:
        basket_x = screen_width-basket_width
    if basket_y <= 0:
        basket_y = 0
    if basket_y >= screen_height-basket_height:
        basket_y = screen_height-basket_height
def get_fruits():
    global screen_ls,fruit_time,ls,score
    if fruit_time == 200:
        fruit_ls.append(random.choice(ls))
        screen_ls.append(apple.get_rect(topleft=(random.randrange(40,screen_width-40,128),0)))
        fruit_time = 0
    else:
        fruit_time += 1
    for x in screen_ls:
        if score >= 100:
            x.y += 2
        elif score >=200:
            x.y += 3
        else:
            x.y += 1
        if x.y >= 650:
            fruit_ls.pop(0)
            screen_ls.remove(x)
            score -= 1
    for s in range(len(screen_ls)):
        screen.blit(fruit_ls[s],screen_ls[s])
def collision_bomb_basket(text):
    global score,score_color
    score_text_main = text.format(str(score))
    scoretext = pg.font.Font("freesansbold.ttf",30)
    textsurface = scoretext.render(score_text_main,True,score_color)
    textrect = textsurface.get_rect()
    textrect.center = ((int(screen_width/2)),(int(screen_height/2)))
    screen.fill((255,255,255))
    screen.blit(textsurface,textrect)
    pg.display.update()
    screen_ls.clear()
    fruit_ls.clear()
    time.sleep(3)
    game_runs()
def collision_fruits_basket():
    global screen_ls,basket,basket_x,basket_y,score,fruit_ls
    basket_rect = basket.get_rect(x=basket_x,y=basket_y)
    for x in screen_ls:
        if x.colliderect(basket_rect):
            z = screen_ls.index(x)
            if fruit_ls[z] == bomb:
                text = "oops! your crashed. Yours Score {} "
                collision_bomb_basket(text)
            else:
                screen_ls.remove(x)
                fruit_ls.pop(z)
                score += 1
def screen_score_text():
    global score,score_color
    score_text = "score : "+str(score)
    scoretext = pg.font.Font("freesansbold.ttf",20)
    textsurface = scoretext.render(score_text,True,score_color)
    textrect = textsurface.get_rect()
    #textrect.center = ((int(screen_width/2)),(int(screen_height/2)))
    textrect.center = (830,30)
    screen.blit(textsurface,textrect)
    pg.display.update()
def game_runs():
    global basket_x,basket_y,basket_x_change,basket_y_change,basket
    score = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    basket_x -= basket_x_change
                if event.key == pg.K_RIGHT:
                    basket_x += basket_x_change
                if event.key == pg.K_UP:
                    basket_y -= basket_y_change
                if event.key == pg.K_DOWN:
                    basket_y += basket_y_change


        screen.fill((255,255,255))
        basket_positions()
        get_fruits()
        collision_fruits_basket()
        screen.blit(basket,(basket_x,basket_y))
        screen_score_text()
        pg.display.update()


pg.init()
screen_width = 1148-256
screen_height = 680
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("ballon catch")
#background loading
#background = pg.image.load("kitchen.png")
#basket loading
basket = pg.image.load("basket.png")
basket_x = 520
basket_y = 550
basket_x_change = 128
basket_y_change = 50
basket_width = 128
basket_height = 100
#imgae loading
apple = pg.image.load("apple.png")
grape = pg.image.load("grapes.png")
orange = pg.image.load("orange.png")
pineapple = pg.image.load("pineapple.png")
bomb = pg.image.load("bomb.png")
ls = [apple,grape,orange,pineapple,bomb]
score_color=((1,1,1))
#screen_ls
screen_ls = []
fruit_ls = []
fruit_time = 0
score = 0
game_runs()
