import turtle

wn = turtle.Screen()
wn.title("pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# bar 1
bar1 = turtle.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("white")
bar1.penup()
bar1.shapesize(stretch_wid=5, stretch_len=1)
bar1.goto(-350, 0)

# bar 2
bar2 = turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("white")
bar2.penup()
bar2.shapesize(stretch_wid=5, stretch_len=1)
bar2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# functions
def bar1_up():
    y = bar1.ycor()
    y += 20
    bar1.sety(y)

def bar1_down():
    y = bar1.ycor()
    y -= 20
    bar1.sety(y)

def bar2_up():
    y = bar2.ycor()
    y += 20
    bar2.sety(y)

def bar2_down():
    y = bar2.ycor()
    y -= 20
    bar2.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(bar1_up, "w")
wn.onkeypress(bar1_down, "s")
wn.onkeypress(bar2_up, "Up")
wn.onkeypress(bar2_down, "Down")

# main loop
while True:
    wn.update()

    # ball movement and properties
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    #bars and ball collision
    if (ball.xcor() > 340 and ball.xcor() <  350) and (ball.ycor() < bar2.ycor() + 50 and ball.ycor() > bar2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() >  -350) and (ball.ycor() < bar1.ycor() + 50 and ball.ycor() > bar1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

    # score
    player_1 = 0
    player_2 = 0
    if (ball.xcor() < -340 and ball.xcor() >  -350) and (ball.ycor() < bar1.ycor() + 50 and ball.ycor() > bar1.ycor() -50):
        player_2 = player_2 + 1
    if ball.xcor() > 340 and ball.xcor() <  350 and (ball.ycor() < bar2.ycor() + 50 and ball.ycor() > bar2.ycor() -50):
        player_1 = player_1 + 1
    
    print (player_1 and player_2)

    

