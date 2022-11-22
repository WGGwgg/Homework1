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

if __name__ == '__main__':
    shape_num = 5
    tt.screensize(1200,600)
    for i in range(shape_num):
        # draw(i+3)
        draw1(i+3)
        tt.penup()
        tt.forward(150)
        tt.pendown()
    tt.exitonclick()
