from random import randrange
from turtle import *
from freegames import vector

# Initialize the ball and speed vectors
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []  # List to store the targets

def tap(x, y):
    """
    Respond to screen tap.
    Set the ball's position and speed based on tap location,
    but only if the last ball is off-screen.
    """
    if ball.x < -198:
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25 * 2 #Se aumenta la velocidad
        speed.y = (y + 200) / 25 * 2 #Se aumenta la velocidad

def inside(xy):
    """
    Return True if xy coordinates are within the screen boundaries.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """
    Draw the targets and the ball on the screen.
    Targets are blue dots, and the ball is a red dot.
    """
    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    update()

def move():
    """
    Move the targets and the ball.
    Targets move horizontally across the screen.
    The ball's movement is affected by 'gravity' (speed.y decrement).
    Reset the ball's position if it goes off-screen.
    """
    # Randomly add new targets
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move existing targets
    for target in targets:
        target.x -= 1

    # Move the ball and apply gravity
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Check for collision with targets and remove hit targets
    dupe = targets.copy()
    targets.clear()
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Reset the ball if it goes off-screen
    if not inside(ball) and ball.x != -200:
        ball.x = -200
        ball.y = -200

    draw()
    ontimer(move, 50)

# Set up the screen, hide the turtle cursor, and start the game loop
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
