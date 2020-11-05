import turtle


class Pong:
    def __init__(self):


        # Make a window
        self.wn = turtle.Screen()

        # The background color
        self.wn.bgcolor("black")

        # The title of the window
        self.wn.title("PONG GAME ")

        # The window size
        self.wn.setup(width=800, height=600)

        #  Stop the window from updating , we need to manual update it . (Speeds up our games quite a bit )
        self.wn.tracer(0)

        self.creat_paddel_a()
        self.creat_paddel_b()
        self.creat_ball()

        Assign_Keys(paddel_1=self.paddel_a, paddel_2=self.paddel_b, wn= self.wn,ball= self.b)



    def creat_paddel_a(self):

        # Controls the turtle module to let you draw all over
        self.paddel_a = turtle.Turtle()

        # Speed of animation (sets it to the maximum possible speed)
        self.paddel_a.speed(0)

        # Making a square
        self.paddel_a.shape("square")

        # The color of the square
        self.paddel_a.color("white")

        # This makes the turtle not draw a line when moving the square to a new coordinates
        self.paddel_a.penup()

        # Placing the square to a new coordinate (left side of the window )
        self.paddel_a.goto(-350, 0)

        # Stretches the square out (stretch_len => horizontal , stretch_wid => vertical)
        # 1 == 20 , 5 == 100
        self.paddel_a.shapesize(stretch_len=1, stretch_wid=5)

    def creat_paddel_b(self):

        # Controls the turtle module to let you draw all over
        self.paddel_b = turtle.Turtle()

        # Speed of animation (sets it to the maximum possible speed)
        self.paddel_b.speed(0)

        # Making a square
        self.paddel_b.shape("square")

        # The color of the square
        self.paddel_b.color("white")

        # This makes the turtle not draw a line when moving the square to a new coordinates
        self.paddel_b.penup()

        # Placing the square to a new coordinate (left side of the window )
        self.paddel_b.goto(350, 0)

        # Stretches the square out (stretch_len => horizontal , stretch_wid => vertical)
        self.paddel_b.shapesize(stretch_len=1, stretch_wid=5)

    def creat_ball(self):

        # Makes the ball and puts it in the middle of the screen

        self.b = turtle.Turtle()
        self.b.color("white")
        self.b.shape("circle")
        self.b.speed(0)
        self.b.penup()
        self.b.goto(0, 0)


class Assign_Keys:
    # Making the squares movable and the ball move

    def __init__(self, paddel_1 , paddel_2, wn, ball):

        self.paddel_a = paddel_1
        self.paddel_b = paddel_2
        self.wn = wn

        self.ball = ball

        self.listen()
        Movement(ball= ball , paddel_a=paddel_1, paddel_b=paddel_2, wn= self.wn)

    # Make the paddel_a move up
    def paddel_a_up(self):

        # get the coordinates of paddel_a
        y = self.paddel_a.ycor()

        # make the paddel_a move +20 if it's pressed
        y += 20

        # Sets the new y_coordinates to paddel_a
        self.paddel_a.sety(y)

    # keep doing it for the other function definitions
    def paddel_a_down(self):

        y = self.paddel_a.ycor()

        # y -= 20 to move paddel_a downwards
        y -= 20
        self.paddel_a.sety(y)

    def paddel_b_up(self):

        y = self.paddel_b.ycor()
        y += 20
        self.paddel_b.sety(y)

    def paddel_b_down(self):
        y = self.paddel_b.ycor()
        y -= 20
        self.paddel_b.sety(y)

    def listen(self):

        # Listens for any keyboard inputs
        self.wn.listen()

        # if "w" is pressed on the keyboard it calls the function definition paddel_a_up() (moving it up by +20)
        self.wn.onkeypress(lambda :self.paddel_a_up(), "w")

        # if "s" is pressed on the keyboard it calls the function definition paddel_a_down() (moving it down by -20)
        self.wn.onkeypress(lambda :self.paddel_a_down(), "s")

        # if "up arrow" is pressed on the keyboard it calls the function definition paddel_b_up() (moving it up by +20)
        self.wn.onkeypress(lambda :self.paddel_b_up(), "Up")

        # if "down arrow" is pressed on the keyboard it calls the function definition paddel_b_down() (moving it down by -20)
        self.wn.onkeypress(lambda :self.paddel_b_down(), "Down")

class Movement:
    def __init__(self, wn, ball, paddel_a, paddel_b ):
        self.wn = wn

        self.paddel_a = paddel_a
        self.paddel_b = paddel_b
        self.ball = ball

        self.pen = turtle.Turtle()

        self.ball.dx = 0.7
        self.ball.dy = 0.7

        self.player_1 = 0
        self.player_2 = 0

        self.move_the_objects()

    def move_the_objects(self):

        while True:
            self.wn.update()

            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            self.border_wall()
            self.padding_bounce()


    def lose(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,260)
        self.pen.write(f'Player A: {self.player_1}  Player B: {self.player_2}', align="center", font=("Courier", 24, "normal"))

    def border_wall(self):

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            self.player_1 += 1

            self.pen.clear()

            self.lose()

        if self.ball.xcor() < -390:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            self.player_2 += 1

            self.pen.clear()

            self.lose()

    def padding_bounce(self):

        if self.ball.xcor() == 340 and self.ball.ycor() < self.paddel_b.ycor() + 40 and self.ball.ycor() > self.paddel_b.ycor() -40 :
            self.ball.dx *= -1

        if self.ball.xcor() == -340 and self.ball.ycor() < self.paddel_a.ycor() +40 and self.ball.ycor() > self.paddel_a.ycor() -40:
            self.ball.dx *= -1




Pong()