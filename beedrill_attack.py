# BEEDRILL ATTACK!
import turtle
import math

#-------------------------------------------------------------------------------
# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Beedrill Attack!")
# Turn off screen updates for now
screen.tracer(0)
# Add in sprites (if available)
piks_file = 'Pikachu/piks.gif'
beedrill_file = 'Pikachu/bee.gif'

while True:
    try:
        screen.register_shape(piks_file)
        break
    except:
        break
while True:
    try:
        screen.register_shape(beedrill_file)
        break
    except:
        break

#-------------------------------------------------------------------------------
# Screen specs
left_border = -250
right_border = 250
bottom_border = -250
top_border = 250
center = 0
off_screen = (0, -500)
#-------------------------------------------------------------------------------
# Set up border turtle
border= turtle.Turtle()
# Fastest spped for setup
border.speed(0)
# Pick up border pen so it doesn't make a line while getting into position
border.penup()
border.pensize(5)

# Make a border for game
border.setpos(left_border, bottom_border)
border.pendown()
border.color("lightblue")
for x in range(4):
    border.forward(500)
    border.left(90)
border.penup()
border.setpos(off_screen)

#-------------------------------------------------------------------------------
# Set up pikachu
pika = turtle.Turtle()
pika.penup()
# Fastest speed for getting into place
pika.speed(0)
pika.left(90)
pika.setpos(center, (bottom_border + 20) )
try:
    pika.shape(piks_file)
except:
    pika.color("black")
    pika.shape("circle")
    pika.shapesize(1.25, 1.5, 3)
#-------------------------------------------------------------------------------
# Set up the thunderbolt Turtle
bolt = turtle.Turtle()
bolt.penup()
bolt.setpos(center, top_border)
# Turn bolt 90 counterclockwise so that it will move towards top of the grid
bolt.left(90)
bolt.hideturtle()
bolt.color("orange")
#-------------------------------------------------------------------------------
# Set up scoreboard Turtle
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.setpos(left_border, top_border)
score_board.write('Score: ', False, align="left", font='Ariel, 20')
#-------------------------------------------------------------------------------
# Set up beedrills
beedrill = []
# Place number of beedrill "turles" in a list
for beedrills in range(18):
	beedrill.append(turtle.Turtle())
# Set starting coordinates of 1st beedrill and then use a loop to set them all
x = left_border + 50
y = top_border - 50
for bee in beedrill:
    bee.penup()
    bee.speed(0)
    bee.setpos(x, y)
    try:
        bee.shape(beedrill_file)
    except:
        bee.shape("square")
        bee.color("red")
    bee.right(90)
    bee.speed(1)
    x += 50
# Set remaining beedrills in a new y-ccordinate row once one hits 225 x coordinate
    if x >= right_border:
        x = -200
        y -= 50
#-------------------------------------------------------------------------------
# Set up keyboard movements

# Set amount of pixels pikachu will move each time an arrow key is pressed
pika_movement = 15
above_pika = 20
bolt_state = "ready"
bee_number = 18
num = 0

def score():
    global bee_number
    global num
    bee_number -= 1
    num += 10
    score_board.clear()
    score_board.write(f'Score: {num}', False, align="left", font='Ariel, 20')
    return bee_number

def win_screen():
    screen = turtle.Screen()
    screen.clearscreen()
    screen.bgcolor("yellow")
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.write('You did it, Pikachu!', align="center", font='Ariel, 40')
    y = winner.ycor()
    winner.sety(y - 20)
    winner.write('(click to exit)', align="center", font='Ariel, 20')
    screen.exitonclick()

def lose_screen():
    screen = turtle.Screen()
    screen.clearscreen()
    screen.bgcolor("yellow")
    loser = turtle.Turtle()
    loser.penup()
    loser.hideturtle()
    loser.write('Maybe next time, Pikachu... :(', align="center", font='Ariel, 40')
    y = loser.ycor()
    loser.sety(y - 20)
    loser.write('(click to exit)', align="center", font='Ariel, 20')
    screen.exitonclick()

def fire_thunderbolt():
    global bolt_state
    if bolt_state == "ready":
        x = pika.xcor()
        y = pika.ycor() + above_pika
        bolt.setpos(x, y)
        bolt.showturtle()
        bolt_state = "not ready"

def move_left():
    x = pika.xcor()
    x -= pika_movement
# Set left boundary for pikachu at -225 x-coordinate
    if x <= left_border + pika_movement:
        x = left_border + pika_movement
# Move pikachu to x coordinate
    pika.setx(x)

def move_right():
    x = pika.xcor()
    x += pika_movement
# Set right boundary for pikachu at 225 x-coordinate
    if x >= right_border - pika_movement:
        x = right_border - pika_movement
# Move pikachu tow x coordinate
    pika.setx(x)

screen.listen()
screen.onkeypress(fire_thunderbolt, "space")
# Set move_left function to occur any time the left keyboard button is pressed
screen.onkeypress(move_left, "Left")
# Set move_right function to occur any time the right keyboard button is pressed
screen.onkeypress(move_right, "Right")
#-------------------------------------------------------------------------------
# Set amount of pixels the beedrils move each time
beemovement = .75
bolt_movement = 20
# Since the screen is a grid, the pythagorean theorem can be used to find the...
# distance between two turtle objects (and used to determine collisions)
def obj_distance(a, b):
    return math.sqrt( ((a.xcor() - b.xcor()) **2) + ((a.ycor() - b.ycor()) **2) )

# Turn on screen updates
# Begin main game loop

while True:
    screen.update()

    if bolt.ycor() >= top_border:
        bolt_state = "ready"
        bolt.hideturtle()

# Move bolt
    y= bolt.ycor()
    y += bolt_movement
    bolt.sety(y)

    for bee in beedrill:
        x = bee.xcor()
        x += beemovement
        bee.setx(x)

    # Set the loop to make all bees move down a y-coordinate row if one bee hits the
    # right side border and then begin moving left on the x-coordinate
        if bee.xcor() >= right_border - pika_movement:
            for bee in beedrill:
                y = bee.ycor()
                y -= 50
                bee.sety(y)
            beemovement *= -1
    # Set the loop to make all bees move down a y-coordinate row if one bee hits the
    # left side border and then begin moving right on the x-coordinate
        if bee.xcor() <= left_border + pika_movement:
            for bee in beedrill:
                y = bee.ycor()
                y -= 50
                bee.sety(y)
            beemovement *= -1


        if obj_distance(bolt, bee) <= 15:
            bee.setpos(off_screen)
            bees_left = score()
            if bees_left == 0:
                print('You Win!')
                win_screen()


        if obj_distance(bee, pika) <= 22:
            lose_screen()

    # Print "Game Over!" and quit game if a bee touches the bottom border
        if bee.ycor() == bottom_border:
            lose_screen()
