from pygame import *

#сcreate a game window
window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
#set the scene background
background = transform.scale(image.load('fon.jpg'), (700, 500))

#create 2 sprites and place them on the stage
sprite1 = transform.scale(
    image.load('spritee.png'),
    (110, 130)
)
x_s1, y_s1 = 2, 150

sprite2 = transform.scale(
    image.load('spritee.png'),
    (110, 130)
)
x_s2, y_s2 = 600, 150

#set the fps
clock = time.Clock()
FPS = 60

#Creating a game cycle
game = True
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

#create the button press event
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y_s2 > 5:
        y_s2 -= 10
    if keys_pressed[K_DOWN] and y_s2 < 400:
        y_s2 += 10
    if keys_pressed[K_s] and y_s1 < 400:
        y_s1 += 10
    if keys_pressed[K_w] and y_s1 > 5:
        y_s1 -= 10


#show the background and sprites on the window
    window.blit(background, (0,0))
    window.blit(sprite1, (x_s1, y_s1))
    window.blit(sprite2, (x_s2, y_s2))

    display.update()
    clock.tick(FPS)