import turtle

# Screen setup
wind = turtle.Screen()
wind.title("Ping Pong By Talah")
wind.setup(width=800, height=600)
wind.bgcolor("black")
wind.tracer(0)

# Player 1
paddle1 = turtle.Turtle()
paddle1.color("blue")
paddle1.penup()
paddle1.shape("square")
paddle1.shapesize(stretch_len=1, stretch_wid=5)
paddle1.goto(-350, 0)
paddle1.speed(0)

# Player 2
paddle2 = turtle.Turtle()
paddle2.color("red")
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(stretch_len=1, stretch_wid=5)
paddle2.goto(350, 0)
paddle2.speed(0)

# Ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.goto(0, 0)

ball.dx = 0.5
ball.dy = 0.5


# Player 1 movement
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


# Player 2 movement
def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# Keyboard controls
wind.listen()

wind.onkeypress(paddle1_up, "w")
wind.onkeypress(paddle1_down, "s")

wind.onkeypress(paddle2_up, "Up")
wind.onkeypress(paddle2_down, "Down")


# Game loop
def game_loop():
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right boundaries
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Collision with player 2
    if (
        ball.xcor() > 340
        and ball.xcor() < 350
        and ball.ycor() < paddle2.ycor() + 40
        and ball.ycor() > paddle2.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1

    # Collision with player 1
    if (
        ball.xcor() < -340
        and ball.xcor() > -350
        and ball.ycor() > paddle1.ycor() - 40
        and ball.ycor() < paddle1.ycor() + 40
    ):
        ball.setx(-340)
        ball.dx *= -1

    # Run the game loop again
    wind.ontimer(game_loop, 10)


# Start the game
game_loop()
wind.mainloop()