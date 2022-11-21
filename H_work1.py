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
    shape_num = 1
    tt.screensize(600,600)
    for i in range(shape_num):
        # draw(5)
        draw1(5)
        tt.penup()
        tt.forward(150)
        tt.pendown()
    tt.exitonclick()
