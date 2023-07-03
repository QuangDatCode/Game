import pygame
import math
from pygame.locals import *

# Khởi tạo Pygame
pygame.init()
# Màu sắc
WHITE = (255, 255, 255)
# Kích thước cửa sổ
window_width, window_height = 1024 , 666
window = pygame.display.set_mode((window_width, window_height))
back = pygame.image.load('./Back.jpg')
pygame.display.set_caption('DEMMO')
clock = pygame.time.Clock();
text = pygame.font.Font(None, 50);
text = text.render('My Game',False, 'Black');
#silme1
slime1 =  pygame.image.load('./slime.png')
slime2 =  pygame.image.load('./slimequaydau.png')
# slimenhay = pygame.mixer.Sound("./slimenhay.mp3")
#nhanvat
cat1 = pygame.image.load('./Cat.png')
cat2 = pygame.image.load('./Catquay.png')
#bien 
a = 0 ;
b = 275;
x = 500;
y = 450;
ok1 = False;
ok2 = False;
ok3 = False;
ok4 = True;
# Vòng lặp chính của game

def catjum():
    global b
    b-=100
def catdown():
    global b
    if (b <= 275):
        b+=5 
def catleft():
    global a
    a-=5;
def catright():
    global a
    a+=5;   
running = True;
ok = True;
while running:
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
     
    window.blit(back,(0,0))
    window.blit(text,(50,0))
    #slime nhay
    if (x == 0): ok3 = True;
    if (x == 900): ok3 = False;
    if (ok3): x+=2;
    else : x-=2;
    if (y == 450 ): 
        ok1 = True;
        ok2 = False;
        # slimenhay.play();
    if (y == 400):
        ok1 = False;
        ok2 = True;
    if (ok1): y-=2.5;
    if (ok2): y+=2.5; 
    if (ok3): window.blit(slime2,(x,y)) 
    else:  window.blit(slime1 ,(x,y))
    keys = pygame.key.get_pressed();
    if (keys[pygame.K_w] ): 
        if (b >= 275 or (b >= 185 and ok4 == False) ): 
            catjum();    
    elif (keys[pygame.K_d]): catright(); ok = True;
    elif (keys[pygame.K_a]): catleft(); ok = False;
    elif (keys[pygame.K_s]): catdown()
    if (a >= 250 and a <= 450 and b <= 180):  ok4 = False;
    else: ok4 = True
    if (b <= 275 and ok4):
        b+=2    
    # nhan vat 
    if(ok == False): window.blit(cat1 , (a,b) )  ;
    else:  window.blit(cat2 , (a,b) )  ;
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
