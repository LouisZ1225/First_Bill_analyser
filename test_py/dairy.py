task = input("今天做了什么：")

print("今天的记录是：")
print(task)

# 下面代码用于画一个五角星
import turtle

screen = turtle.Screen()
screen.title("五角星")

pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)

for _ in range(5):
    pen.forward(100)
    pen.right(144)

turtle.done()