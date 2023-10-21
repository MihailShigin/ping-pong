from pygame import *

#create a game window
window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
#set the scene background
background = transform.scale(image.load('fon.jpg'), (700, 500))

#speed
speed_x = 4
speed_y = 4


#set the fps
clock = time.Clock()
FPS = 60

#create 2 sprites and place them on the stage
class GameSpriite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player_1(GameSpriite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)

        self.image = transform.scale(self.image, (12, 80))


    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 5
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5


class Player_2(GameSpriite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)

        self.image = transform.scale(self.image, (12, 80))

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 5



class Ball(GameSpriite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)




player_1 = Player_1('poloskir.png', 50,
                30, 150)


player_2 = Player_2('poloskiii.png', 50,
                620, 150)


ball = Ball('balls.png', 5,
                300, 150)



#sprite1 = transform.scale(
#    image.load('spritee.png'),
#    (110, 130)
#)
#x_s1, y_s1 = 2, 150

#sprite2 = transform.scale(
#    image.load('spritee.png'),
 #   (110, 130)
#)
#x_s2, y_s2 = 600, 150

#sprite3 = transform.scale(
#    image.load('balls.png'),
#    (130, 130)
#)
#x_s3, y_s3 = 300, 150



#Creating a game cycle
game = True
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(ball, player_2):
        speed_x *= -1

    if sprite.collide_rect(ball, player_1):
        speed_x *= -1

#create the button press event
    #keys_pressed = key.get_pressed()
    #if keys_pressed[K_UP] and y_s2 > 5:
    #    y_s2 -= 10
    #if keys_pressed[K_DOWN] and y_s2 < 400:
    #    y_s2 += 10
    #if keys_pressed[K_s] and y_s1 < 400:
    #    y_s1 += 10
    #if keys_pressed[K_w] and y_s1 > 5:
    #    y_s1 -= 10



#show the background and sprites on the window
    #window.blit(background, (0,0))
    #window.blit(player_1, (x_s1, y_s1))
    #window.blit(player_2, (x_s2, y_s2))
    #window.blit(ball, (x_s3, y_s3))

    if ball.rect.y < 5 or ball.rect.y > 400:
        speed_y *= -1
        

    if ball.rect.x < 0:
        print('BLUE Winner')

    if ball.rect.x > 680:
        print('RED Winner')

    #if ball.rect.y < 0 or ball.rect.y > 400:
    #    ball.rect.y *= -1

    player_1.reset()
    player_1.update()
    player_2.reset()
    player_2.update()
    ball.reset()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    display.update()
    clock.tick(FPS)