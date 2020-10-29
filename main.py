# library
import pgzrun  
import random  

# window size
WIDTH = 350   # width
HEIGHT = 600  # height

# background
background = Actor('foellinger')  # import image

# bird
bird = Actor('corn')  # import image
bird.x = 50           # x coordinate of bird
bird.y = HEIGHT/2     # y coordinate of bird

# top bar
bar_up = Actor('bar_up')    # import image
bar_up.x = 300              # top bar x coordinate
bar_up.y = 0                # top bar y coordinate

# bottom bar
bar_down = Actor('bar_down')    # import image
bar_down.x = 300                # bottom bar x coordinate
bar_down.y = 600                # bottom bar y coordinate

# score
score = 0     

# speed
speed = 1     

# draw scene
def draw():   
    background.draw()  # background
    bar_up.draw()         # top bar
    bar_down.draw()         # bottom bar
    bird.draw()        # bird
    screen.draw.text(str(score), (30, 30),
                     fontsize=50, color='green')

def update():  # update scene
    global score,speed

    # bird fall
    bird.y = bird.y + 2  # bird falls defaultly by increasing y coordinate

    # move bar to left
    bar_up.x = bar_up.x - speed   
    bar_down.x = bar_down.x - speed   

    # when bar move out of the screen, make it reappears at right.
    if bar_up.x < 0:

        # generate bar randomly
        bar_up.x = WIDTH
        bar_down.x = WIDTH
        bar_up.y = random.randint(-200, 200)

        # fix the space between top and bottom bars
        bar_down.y = 600 + bar_up.y   

        # update score
        score = score + 1    # increase score
        if (score % 5 == 0): # as long as score 5 more points; game speed increases
            speed = speed + 1

    # bird hit the bar; Game over.
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) or bird.y < 0 or bird.y > HEIGHT:

        # reset all parameters
        score = 0
        speed = 1
        bird.x = 50            
        bird.y = HEIGHT/2      
        bar_up.x = WIDTH       
        bar_up.y = 0           
        bar_down.x = WIDTH     
        bar_down.y = 600       

# when mouse click; bird flaps
def on_mouse_down():  # 
    bird.y = bird.y - 100  

pgzrun.go()   # game start