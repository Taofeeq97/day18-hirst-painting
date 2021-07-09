#import colorgram
#rgb_colours=[]
#colours = colorgram.extract('SpotPainting04.jpg', 30)
#for color in colours:
#    r=color.rgb.r
#    g = color.rgb.g
#   b = color.rgb.b
#    new_colour=(r,g,b)
#   rgb_colours.append(new_colour)
#print(rgb_colours)
import random
import turtle as turtle_module
turtle_module.colormode(255)
tao=turtle_module.Turtle()
tao.speed("fastest")
tao.penup()
tao.hideturtle()
colour_list=[(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]


tao.setheading(225)
tao.forward(300)
tao.setheading(0)
num_of_dot=100

for dots in range(1, num_of_dot+1):
    tao.forward(50)
    tao.dot(20, random.choice(colour_list))
    if dots%10==0:
        tao.setheading(98)
        tao.forward(50)
        tao.setheading(180)
        tao.forward(500)
        tao.setheading(0)



screen=turtle_module.Screen()
screen.exitonclick()