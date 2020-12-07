# coding=utf-8

import pygame
from pygame.locals import * 
from random import randint

pygame.init()
fenetre = pygame.display.set_mode((600,600))
shape = [] # current shape displayed on the screen
shapes = [[[3,-1],[4,-1],[5,-1],[6,-1]],# the seven shapes of tetris
          [[3,0],[4,0],[4,-1],[5,0]],
          [[3,-1],[4,0],[4,-1],[5,0]],
          [[3,0],[4,0],[4,-1],[5,-1]],
          [[3,-1],[3,0],[4,0],[5,0]],
          [[3,0],[5,0],[4,0],[5,-1]],
          [[3,-1],[3,0],[4,-1],[4,0]]]
keys = [0,0,0] # the 3 basics movements of a shape down, left and right
base = [] # the setteled pieces
omen = [] # the next piece that is going to be generated
colors = [(247,19,247),(247,187,19),(19,240,247),(239,119,163),(175,119,239),(32,169,78)] # colors of the pieces 
race = (128,0,0) # current color of the piece on the screen
game = 0 # 0 -> playing the game, 1 -> lost the game
new_game_image = pygame.image.load("new_game.png") # logo to start a nex game
clicked = 0 # 1 if the user clicked to start a new game
button = [(200,200,200),(255,0,0)] #
points = 0 # 10 for each completed line
myfont = pygame.font.SysFont('FangSong', 30)
myotherfont = pygame.font.SysFont('FangSong', 30)
next_piece = [] # the shape that is going to be generated next
next_race = [] # the color of the shape that is going to be generated next
level = 1 # the level, for each level the speed is augmented by 50 milliseconds
up_button = 0 # if the user clicked the plus level button
down_button = 0 # if the user clicked the minus level button
pause = 0 # if the user clicked the pause button
blevel = 0 # the level before the user clicked pause
highscore = 0
pygame.display.set_icon(pygame.image.load("tetris_logo.png"))
pygame.display.set_caption("平庸的俄罗斯方块")
sad_face = 0
sad_shape = [[2,3],[2,4],[2,10],[2,11],[3,3],[3,4],[3,10],[3,11],[5,6],[5,7],[5,8],[6,6],[6,7],[6,8],[9,5],[9,6],[9,7],[9,8],[9,9]]
start = 0
def draw_face():
    global sad_shape
    global fenetre
    global sad_face
    for i in sad_shape:
        if sad_face == 1:
            pygame.draw.rect(fenetre,(0,255,0),[30*i[1]+2,30*i[0]+2,26,26])
        else:
            pygame.draw.rect(fenetre,(255,255,255),[30*i[1]+2,30*i[0]+2,26,26])
def menufy(shape): # function to transform the next shape to appear to a shape in the menu
    menufied = []
    for i in shape:
        menufied.append([i[0]-3,i[1]+2])
    return menufied

def menu(): # function to show the menu on the right
    global clicked 
    global points
    global next_piece
    global next_race
    global level
    global up_button
    global down_button
    global pause
    global highscore
    next_shape = [] # variable of the next shape that is going to be generated
    pygame.draw.rect(fenetre, (128,128,128), [450,0,150,600]) # the gray rectangle of the menu
    textsurface = myfont.render("New", False, (0,0,0)) # "New Game text 
    fenetre.blit(textsurface, (490, 8))
    textsurface = myfont.render("Game", False, (0,0,0))
    fenetre.blit(textsurface, (480, 24))
    textsurface = myfont.render(":", False, (0,0,0))
    fenetre.blit(textsurface, (480, 24))
    pygame.draw.circle(fenetre, (200,200,200), [570,30], 20) # New Game clickable button 
    if clicked == 1:
        pygame.draw.circle(fenetre, (255,0,0), [570,30], 20) # if the New Game button is clicked it turns red
    fenetre.blit(new_game_image, (560,18)) # New Game logo
    textsurface = myfont.render("分数 : "+str(points), False, (0,0,0))# Points displayed
    fenetre.blit(textsurface, (480, 55)) 
    textsurface = myfont.render("下一块 ", False, (0,0,0))
    fenetre.blit(textsurface, (475, 87))
    pygame.draw.lines(fenetre, (255,0,0), False, [(460,125),(580,125),(580,245),(460,245),(460,125)],2) # The next 7 lines are to display the grid
    pygame.draw.line(fenetre, (255,0,0),[490,125],[490,245],2)
    pygame.draw.line(fenetre, (255,0,0),[520,125],[520,245],2)
    pygame.draw.line(fenetre, (255,0,0),[550,125],[550,245],2)
    pygame.draw.line(fenetre, (255,0,0),[460,155],[580,155],2)
    pygame.draw.line(fenetre, (255,0,0),[460,185],[580,185],2)
    pygame.draw.line(fenetre, (255,0,0),[460,215],[580,215],2)
    next_shape = menufy(next_piece) # turn the positions of shape in the shapes list (line 11) into position in the grid drawn above 
    for i in next_shape:
        pygame.draw.rect(fenetre,next_race,[462+30*i[0],127+i[1]*30,28,28])
    textsurface = myfont.render("等级 : "+str(level), False, (0,0,0)) # display level
    fenetre.blit(textsurface, (460, 280))
    pygame.draw.circle(fenetre, (200,200,200), [570,280], 20) # draw up button
    if up_button == 1:
        pygame.draw.circle(fenetre, (255,0,0), [570,280], 20) # if up button clicked turn button red
    pygame.draw.circle(fenetre, (200,200,200), [570,375], 20) # draw pause-continue button
    if pause == 0:
        textsurface = myfont.render("暂停 : ", False, (0,0,0)) # if game on write "pause :"
        fenetre.blit(textsurface, (460, 360))
        pygame.draw.polygon(fenetre, (0,0,0), [[563,360],[563,390],[583,375]]) # draw pause symbol (triangle)
    else:
        textsurface = myfont.render("继续 : ", False, (0,0,0)) # if game paused write "continue :"
        fenetre.blit(textsurface, (453, 360))
        pygame.draw.rect(fenetre, (0,0,0), [557,360,10,30]) # this line and the next are to draw the continue symbol (two parallel rects)
        pygame.draw.rect(fenetre, (0,0,0), [573,360,10,30])
    pygame.draw.circle(fenetre, (200,200,200), [570,325], 20) # draw down button
    textsurface = myfont.render("最高分 : ", False, (0,0,0)) # the next 4 lines are to display the highscore during session
    fenetre.blit(textsurface, (455, 420))
    textsurface = myfont.render(str(highscore), False, (0,0,0))
    fenetre.blit(textsurface, (475, 445))
    if down_button: 
        pygame.draw.circle(fenetre, (255,0,0), [570,325], 20) # if down button clicked it turns red
    pygame.draw.lines(fenetre, (0,0,0), False, [[560,290],[570,265],[580,290]],2) # draw up symbol
    pygame.draw.lines(fenetre, (0,0,0), False, [[560,315],[570,340],[580,315]],2) # draw down symbol
    pygame.draw.rect(fenetre, (255,0,0), [450,535,150,80]) # The next 7 lines are to draw the banner at the bottom of the menu
    textsurface = myotherfont.render("平庸的俄罗斯方块 v1.0", False, (0,0,0))
    fenetre.blit(textsurface, (455, 540))
    textsurface = myotherfont.render("制造 By", False, (0,0,0))
    fenetre.blit(textsurface, (485, 560))
    textsurface = myotherfont.render("TAK HU", False, (0,0,0))
    fenetre.blit(textsurface, (475, 580))

def out_bound(hape): # This function is used during rotations, it checks if rotated shape is not in screen
    for i in hape:
        if (i[0]<0) or (i[0]>14):
            return True
    return False

def translate(hape, move):
    new_move = []
    for i in hape:
        if i[0]<15 and i[0]>-1:
            new_move.append([i[0]+move,i[1]])
        else:
            return hape
    return new_move

def within(hape, basis):
    for i in hape:
        if i in basis:
            return True
    return False

def makeit(): # generate current and next shape and their colors
    global shape
    global shapes
    global colors
    global race
    global base
    global clicked
    global next_piece
    global next_race
    global points
    global highscore
    for i in base:
        if i[1] == 0:
            if highscore < points:
                highscore = points
            animation()
            return True
    shape = next_piece
    race = next_race
    next_piece = shapes[randint(0,len(shapes)-1)]
    next_race = colors[randint(0,len(colors)-1)]
    clicked = 0
    return False
    
def checkit(): # if line in base is completed, it turns green for 0.1 seconds and is removed
    global base
    global points
    global level
    checker = 0
    bases = []
    for i in range(0,20):
        for j in range(0,15):
            if [j,i] not in base:
                checker = 1
                break
        if checker == 0:
            bases.append(i)
            points = points + 10
            if points%100 == 0:
                if level<8:
                    level = level +1
        checker = 0
    return bases

def predict():
    global base
    global shape
    global omen
    if shape == []:
        return []
    omen = []
    for i in shape:
        omen.append([i[0],i[1]])
    old_omen = []
    arrived = False
    while not arrived:
        old_omen = omen
        for i in omen:
            i[1] = i[1] + 1
            if i[1] >= 19 or [i[0],i[1]+1] in base:
                arrived = 1
    if omen == shape:
        omen = []
    return omen 
    
def removeit(lines): # remove lines, see function checkit
    global base
    new_base = []
    for i in base:
        if i[1] not in lines:
            new_base.append(i)
    for j in new_base:
        for k in lines:
            if j[1]<k:
                j[1] = j[1] + 1
    return new_base

def in_base(hape): # function used during rotation, if rotated shape is in base
    global base
    for i in hape:
        if i in base:
            return True
    return False

def at_floor(hape): # if moving shape hit the bottom of the screen
    for i in hape:
        if i[1] == 19:
            return True
    return False

def get_topleft_limit(): 
    global shape
    l = 14
    t = 19
    for i in shape:
        if i[0] < l:
            l = i[0]
        if i[1] < t:
            t = i[1]
    return [l,t]

def most_left_top(hape):
    l = hape[0][0]
    t = hape[0][1]
    for i in hape:
        if i[0] < l:
            l = i[0]
        if i[1] < t:
            t = i[1]
    return [l,t]

def left_top():
    global shape 
    l = shape[0][0]
    t = 19
    for i in shape:
        if i[0] < l:
            l = i[0]
    for i in shape:
        if i[0] == l:
            if i[1] < t:
                t = i[1]
    return [l,t]

def get_diff(lt):
    global shape
    shape_diff = []
    for i in shape:
        shape_diff.append([lt[0]-i[0],lt[1]-i[1]])
    return shape_diff
    
def init_transform(gd): # base transformation for rotations 
    const = 0
    for i in gd:
        i[0] = i[0] * -1
        const = i[0]
        i[0] = i[1]
        i[1] = const
    return gd 

def back_screen(hape):
        r = 0
        d = 0
        new_hape = hape
        for i in hape:
            if i[0]>r:
                r = i[0]
            if i[1]>d:
                d = i[1]
        if r>14:
            new_hape = []
            for i in hape:
                new_hape.append([i[0]+(14-r),i[1]])
        if d>19:
            new_hape = []
            for i in hape:
                new_hape.append([i[0],i[1]+(19-d)])
        return new_hape
            
    
def transform(tl, it): # center function for rotation, the 8 functions above are all used within this function 
    global shape
    global base
    final_shape = []
    ml = []
    for i in it:
        final_shape.append([tl[0]+i[0],tl[1]+i[1]])
    ml = most_left_top(final_shape)
    lefttop = get_topleft_limit()
    for j in final_shape:
        j[0] = j[0] + (lefttop[0] - ml[0])
        j[1] = j[1] + (lefttop[1] - ml[1])
    siko = back_screen(final_shape)
    if within(siko,base):
        siko = translate(siko,1)
        if within(siko,base):
            siko = translate(siko,-1)
            if within(siko,base):
                siko = shape        
    return siko

def move_d():
    global shape
    global base
    global init
    global game
    global points
    new = []
    for i in shape:
        if i[1] == 19:
            for i in shape:
                base.append(i)
            if not makeit():
                draw_wall()
                draw_base()
                draw_shape()
                pygame.display.flip()
                return
            return
    for i in shape:
        new.append([i[0],i[1]+1])
    if in_base(new):
        for i in shape:
            base.append(i)
        if not makeit():
            draw_wall()
            draw_base()
            draw_shape()
            pygame.display.flip()
    else:
        shape = new
    lines = []
    lines = checkit()
    if lines != []:
        draw_shape()
        drawit(lines)
        pygame.time.wait(300)
        base = removeit(lines)
        draw_wall()
        draw_base()
        draw_shape()
        pygame.time.wait(300)
def move_r():
    global shape
    new = []
    for i in shape:
        if i[0] == 14:
            return
    for i in shape:
        new.append([i[0] + 1,i[1]])
    if not in_base(new):
        shape = new

def move_l():
    global shape
    new = []
    for i in shape:
        if i[0] == 0:
            return
    for i in shape:
        new.append([i[0] - 1,i[1]])
    if not in_base(new):
        shape = new
def draw_shape():
    global shape
    for i in shape:
        pygame.draw.rect(fenetre, race, [30*i[0]+2,30*i[1]+2, 26, 26])
    pygame.display.flip()
def draw_wall():
    menu()
    future_base = predict()
    for i in range(0,15):
        for j in range(0,20):
            pygame.draw.rect(fenetre, (128,128,128), [30*i,30*j, 30,30])
            if [i,j] in future_base:
                pygame.draw.rect(fenetre, (0,255,0), [30*i,30*j, 30,30])
            pygame.draw.rect(fenetre, (255,255,255), [30*i+2,30*j+2, 26,26])
def drawit(lines):
    for i in lines:
        for j in range(0,15):
            pygame.draw.rect(fenetre, (0,255,0), [30*j+2,30*i+2, 26,26])
    pygame.display.flip()
def draw_base():
    for i in base:
        pygame.draw.rect(fenetre, (0,0,255), [30*i[0]+2,30*i[1]+2, 26, 26])
def animation():
    global base
    global omen
    global game
    global keys
    global shape
    keys = [0,0,0]
    base = []
    omen = []
    game = 1
    draw_wall()
    for j in range(0,20):
        for i in range(0,15):
            pygame.draw.rect(fenetre, (128,128,128), [30*i, 30*(19-j), 30, 30])
            pygame.draw.rect(fenetre, (255,0,0), [30*i+2, 30*(19-j)+2, 26, 26])
        pygame.display.flip()
        pygame.time.wait(200)
    shape = []
continuer = 0
draw_wall()
draw_shape()
pygame.display.flip()
pygame.time.set_timer(USEREVENT+1, 400)
pygame.time.set_timer(USEREVENT+2, 350)
pygame.time.set_timer(USEREVENT+3, 300)
pygame.time.set_timer(USEREVENT+4, 250)
pygame.time.set_timer(USEREVENT+5, 200)
pygame.time.set_timer(USEREVENT+6, 150)
pygame.time.set_timer(USEREVENT+7, 100)
pygame.time.set_timer(USEREVENT, 50)
next_piece = shapes[randint(0,len(shapes)-1)]
next_race = colors[randint(0,len(colors)-1)]
makeit()
while continuer == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 1
        if event.type == KEYDOWN and game == 0 and pause == 0:
            if event.key == K_RIGHT:
                keys[0] = 1
            if event.key == K_LEFT:
                keys[1] = 1
            if event.key == K_DOWN:
                keys[2] = 1
            if event.key == K_UP:
                shape = transform(left_top(),init_transform(get_diff(left_top())))
                draw_wall()
                draw_base()
                draw_shape()
        if event.type == KEYUP and game == 0:
            keys = [0,0,0]
        if event.type == MOUSEBUTTONDOWN :
            if (event.pos[0]<590 and event.pos[0]>550) and (event.pos[1]<50 and event.pos[1]>10):
                    if highscore < points:
                        highscore = points
                    game = 0
                    base = []
                    points = 0
                    level = 1
                    clicked = 1
            if (event.pos[0]<590 and event.pos[0]>550) and (event.pos[1]<300 and event.pos[1]>260) and pause == 0:
                up_button = 1
                if level < 8:
                    level = level + 1
            if (event.pos[0]<590 and event.pos[0]>550) and (event.pos[1]<345 and event.pos[1]>305) and pause == 0:
                down_button = 1
                if level > 1:
                    level = level - 1
            if (event.pos[0]<590 and event.pos[0]>550) and (event.pos[1]<395 and event.pos[1]>355) and game == 0:
                if pause == 0:
                    pause = 1
                    blevel = level
                    level = 0
                else:
                    pause = 0
                    level = blevel
                draw_wall()    
                draw_shape()
                draw_base()
                pygame.display.flip()
        if event.type == MOUSEBUTTONUP:
            if clicked == 1:
                clicked = 0
                makeit()
            if up_button == 1:
                up_button = 0
            if down_button == 1:
                down_button = 0
        if game == 1:
            if event.type == USEREVENT+1:
                    sad_face = (sad_face+1)%2
                    draw_face()
        if game == 0:
            if event.type == USEREVENT+1 and game == 0 and level == 1:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT+2 and game == 0 and level == 2:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT+3 and game == 0 and level == 3:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT+4 and game == 0 and level == 4:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT+5 and game == 0 and level == 5:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT+6 and game == 0 and level == 6:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT+7 and game == 0 and level == 7:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
            if event.type == USEREVENT and game == 0 and level == 8:
                draw_wall()
                draw_base()
                move_d()
                draw_shape()
    if keys[0] == 1 and game == 0:
        pygame.time.wait(100)
        draw_wall()
        draw_base()
        move_r()
        draw_shape()
    if keys[1] == 1 and game == 0:
        pygame.time.wait(100)
        draw_wall()
        draw_base()
        move_l()
        draw_shape()
    if keys[2] == 1 and game == 0:
        pygame.time.wait(100)
        draw_wall()
        draw_base()
        move_d()
        draw_shape()
    pygame.display.flip()