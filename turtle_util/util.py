""" ************ Dancing Bunny ************
* Created by: Cap Turtle
* DateTime: 2022/11/14 16:52 
* Desc:
*************************************** """

import turtle


class TurtleUtil:
    def __init__(self, hide=True):
        turtle.setup(800, 600)
        self._t = turtle.Turtle()
        if hide:
            self._t.hideturtle()
        self._t.speed('fastest')

    def draw_point(self, color='red', point=None, size=None):
        self._t.penup()
        if point:
            self._t.setpos(point[0], point[1])
        self._t.dot(size, color)

    def mark_home(self):
        cur_pos = self._t.pos()
        self._t.home()
        self.draw_point()
        self._t.setpos(cur_pos)

    def draw_polygon(self, vertices, color='green'):
        self._t.color(color)
        self._t.penup()
        for x, y in vertices:
            self._t.setpos(x, y)
            self._t.pendown()
        self._t.setpos(vertices[0][0], vertices[0][1])

    def draw_circle(self, center, radius, color='orange'):
        self._t.color(color)
        self._t.penup()
        self._t.setpos(center[0], center[1]-radius)
        self._t.pendown()
        self._t.circle(radius)

    @staticmethod
    def done():
        turtle.done()
