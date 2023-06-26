# import colorgram
# colors = colorgram.extract('download.jpg', 40)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t
import random

color_list = [(235, 232, 227), (230, 233, 239), (239, 231, 235), (227, 236, 230), (198, 162, 101), (63, 90, 126),
              (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85),
              (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22),
              (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96),
              (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27), (45, 73, 76),
              (219, 177, 170), (24, 43, 43), (49, 88, 21)]

t.colormode(255)
tim = t.Turtle()

tim.setheading(225)
tim.penup()
tim.fd(250)
tim.setheading(0)
no_of_dots = 100


for dot_count in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
    tim.setheading(0)
