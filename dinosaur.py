import turtle, time, random

screen = turtle.Screen()
screen.setup(height=500,width=800)
screen.title("Dinoo")
screen.bgcolor("white")
screen.bgpic("adnsu2.gif")
screen.tracer()

screen.register_shape('telebe.gif')
screen.register_shape('kesr.gif')

student = turtle.Turtle()
student.speed(0)
student.shape("telebe.gif")
student.color("green")
student.penup()
student.dy = 0
student.status = "Ready"
student.goto(-200, -170)

kesr = turtle.Turtle()
kesr.speed(0)
kesr.shape("kesr.gif")
kesr.color("green")
kesr.penup()
kesr.dx = -5
kesr.goto(200, -70)

write = turtle.Turtle()
write.color('red')
write.speed(0)
write.penup()
write.goto(0,150)
write.hideturtle()

gravity = -0.5

def jump():
    if student.status == "Ready":
        student.dy = 12
    student.status = "jumping"
    
screen.listen()
screen.onkey(jump,"space")

while True:
    time.sleep(0.01)
    
    if student.ycor() < -50:
        student.sety(-50)
        student.dy = 0
        student.status = "Ready"  
          
    if student.ycor() != -50 and student.status == "jumping":
        student.dy += gravity
    
    y = student.ycor()
    y = y + student.dy
    student.sety(y)
    
    x = kesr.xcor()
    x = x + kesr.dx
    kesr.setx(x)    
    
    if kesr.xcor() < -400:
        x = random.randint(400,600)
        kesr.setx(x)
        kesr.dx = kesr.dx * 1.005    
    
    if kesr.distance(student) < 30:
        write.write('KESILDINIZ !',align='center', font=('Courier',24,'bold',))
        time.sleep(2)
        break
    
    screen.update()