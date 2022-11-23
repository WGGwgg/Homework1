import turtle as tt

def draw(num):
    theta = 360/num
    for i in range(num):
        tt.forward(50)
        tt.left(theta)

def draw1(num):
    theta = 180 / num
    for i in range(num):
        tt.forward(50)
        tt.right(180-theta)

def plot(shape_num):
    tt.screensize(1200, 600)
    tt.penup()
    tt.goto(-400,150)
    tt.pendown()
    for i in shape_num:
        draw(i)
        tt.penup()
        tt.forward(200)
        tt.pendown()
    tt.penup()
    tt.goto(-400,-150)
    tt.pendown()
    for i in shape_num:
        draw1(i)
        tt.penup()
        tt.forward(200)
        tt.pendown()
    tt.exitonclick()

if __name__ == '__main__':
    plot([3,5,7,9])
