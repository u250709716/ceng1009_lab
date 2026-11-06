import turtle


# def gitMark(x):
#     if x >= 90:
#         return "A"
#     elif x >= 80:
#         return "B"
#     elif x >= 70:
#         return "C"
#     elif x >= 60:
#         return "D"
#     else:
#         return "F"
#
#     return x
#
# marks = [99, 80, 78, 66, 95, 34, 60]
# for mark in marks:
#     print(gitMark(mark))
#
# h = [48, -117, 200, 240, 160, -260, 220]
#
# def color (h):
#     if h >=200:
#         return "red"
#     elif h >=100:
#         return "yellow"
#     else:
#         return "green"
#     return color
#
# def drawBar (t, h, gap):
#     if h >= 0:
#         y = h + gap
#     else:
#         y = h - gap
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(y)
#     t.write(" " + str(h))
#     t.fillcolor(color(h))
#     t.right(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(y)
#     t.left(90)
#     t.end_fill()
#
# def barChat(h):
#     maxh = int(max(h))
#     minh = int(min(h))
#     border = 10
#     bottom = min(minh, 0) - border
#     num = len(h)
#     wn = turtle.Screen()
#     tess = turtle.Turtle()
#     wn.bgcolor("light green")
#     right = 50 * num + border
#     top = maxh + 4 * border
#     wn.setworldcoordinates(-border, bottom, right, top)
#     tess.color("blue")
#     tess.pensize(3)
#     for height in h:
#         drawBar(tess, height, 10)
#
#     wn.exitonclick()
#
# barChat(h)

# import math
#
# def findHypo(a, b):
#     hypot = (a ** 2 + b ** 2) ** 0.5
#     return hypot
#
# def calcWithMath(a, b):
#     hypot = math.sqrt(a ** 2 + b ** 2)
#     return hypot
#
# print(findHypo(3, 4))
# print(calcWithMath(3, 4))