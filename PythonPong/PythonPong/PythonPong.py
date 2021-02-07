import turtle

tortuga = turtle.Screen()

tortuga.title("Pong!")
tortuga.bgcolor("black")
tortuga.setup(width=800, height=600)
tortuga.tracer(0)

#################################### player A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

#################################### player B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#################################### ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#################################### points
points = turtle.Turtle()
points.speed(0)
points.color("White")
points.penup()
points.hideturtle()
points.goto(0,260)
scoreA = 0
scoreb = 0
points.write("{}  |  {}".format(scoreA,scoreb), align="center", font=("courier",30,"normal"))

def moveUpA():
    y = paddleA.ycor()
    y += 30
    paddleA.sety(y)

def moveDownA():
    y = paddleA.ycor()
    y -= 30
    paddleA.sety(y)

def moveUpB():
    y = paddleB.ycor()
    y += 30
    paddleB.sety(y)

def moveDownB():
    y = paddleB.ycor()
    y -= 30
    paddleB.sety(y)

##################################### keyboard
tortuga.listen()
tortuga.onkeypress(moveUpA, "w")
tortuga.onkeypress(moveDownA, "s")
tortuga.onkeypress(moveUpB, "8")
tortuga.onkeypress(moveDownB, "5")

while True:
    tortuga.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #limits
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    # goal
    elif ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        points.clear()
        points.write("{}  |  {}".format(scoreA,scoreb), align="center", font=("courier",30,"normal"))

    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreb += 1
        points.clear()
        points.write("{}  |  {}".format(scoreA,scoreb), align="center", font=("courier",30,"normal"))

    # paddle limits
    if paddleB.ycor() > 260:
        paddleB.sety(260)
    elif paddleB.ycor() < -260:
        paddleB.sety(-260)
    if paddleA.ycor() > 260:
        paddleA.sety(260)
    elif paddleA.ycor() < -260:
        paddleA.sety(-260)

    # paddle hitbox
    if (350 > ball.xcor() > 340) and (paddleB.ycor() - 60 < ball.ycor() < paddleB.ycor() + 60):
        ball.setx(340)
        ball.dx *= -1
    elif (-350 < ball.xcor() < -340) and (paddleA.ycor() - 60 < ball.ycor() < paddleA.ycor() + 60):
        ball.dx *= -1
        ball.setx(-340)