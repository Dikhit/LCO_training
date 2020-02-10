import turtle
import sys
import cv2
import numpy as np

black_screen = np.zeros((800,600))

loser = 3
loss_time = 0

window = turtle.Screen()
window.title("pong Game by katlic")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")

paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

# paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.09
ball.dy = 0.09

# Functions
def paddle_A_up():
    y = paddle_A.ycor()
    y += 10
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 10
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 10
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 10
    paddle_B.sety(y)

# keyboard binding
window.listen()
window.onkeypress(paddle_A_up,"w")
window.onkeypress(paddle_A_down, "s")

window.onkeypress(paddle_B_up,"Up")
window.onkeypress(paddle_B_down,"Down")

while True:
    window.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        loss_time += 1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        loss_time += 1

    # paddle vs ball
    if (ball.xcor() > 340) and (ball.ycor() < paddle_B.ycor() + 50) and (ball.ycor() > paddle_B.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() < -340) and (ball.ycor() < paddle_A.ycor() + 50) and (ball.ycor() > paddle_A.ycor() - 50):
        ball.dx *= -1
    if loss_time == loser:
        sys.exit(0)
