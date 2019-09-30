from turtle import *


def square(side_len):
    for i in range(4):
        forward(side_len)
        right(90)


# square(100)

for i in range(50):
    square(10 + i)
    right(5)


# from random import randint # from the random module import the function randint
# #like turtle it is a module, read ahead for use

# speed(0)

# bgcolor('black')

# x = 1
# #x = 10

# while x < 400:

#     r = randint(0,255) #makes variables r,g,b whose value is an integer,
#     g = randint(0,255) # which is between 0 and 255. It is random, and
#     b = randint(0,255) # changes every time the loop runs

#     colormode(255) # set the color mode to rgb


#     pencolor(r,g,b) # changes the color of the pen to the rgb coordinates
#                     # obtained by the variables r, g, b changing each time

#     fd(100 + x)
#     rt(90.911)


#     x = x+1

exitonclick()
