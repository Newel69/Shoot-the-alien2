import pgzrun
from random import randint

TITLE="Shoot_the_alien"
WIDTH=600
HEIGHT=400

alien=Actor("alien")
explosion=Actor("explosion")
explosion.visible=False

message = ""
score = 0

intro = True

def start_game():
    global intro, message, score
    intro = False
    score = 0
    message = ""
    position()

def draw():
    screen.clear()
    if intro:
        screen.fill("dark red")
        screen.draw.text("Welcome to THE one and only Alien Blaster(B.S).\n Catch as many aliens as possible.",(50,150), fontsize = 30, color = "white")
        screen.draw.text("Press SPACE to start",(200,200), fontsize = 25, color = "orange")
    else:
        screen.fill("red")
        alien.draw()
        if explosion.visible==True:
            explosion.draw()
        screen.draw.text(message, center=(200,200),fontsize = 30, color = "black")
        screen.draw.text("score: "+str(score),(20,20),fontsize = 25, color = "black")
def on_mouse_down(pos):
    global message,score
    if alien.collidepoint(pos):
        position()
        message = "Nice shot"
        score = score+1
    else:
        message = "Miss"
        score = score-1

def position():
    alien.x=randint(50, WIDTH -30)
    alien.y=randint(50, HEIGHT -30)

def update():
    pass
def on_key_down(key):
    if intro and key == keys.SPACE:
        start_game()
position()

pgzrun.go()