""" ************ Dancing Bunny ************
* Created by: Cap Turtle
* DateTime: 2022/11/14 16:52 
* Desc:
*************************************** """

import turtle


class TurtleUtil:
    def __init__(self):
        turtle.setup(800, 600)
        self._t = turtle.Turtle()

    def draw_point(self, color='red', point=None):
        self._t.penup()
        if point:
            self._t.setpos(point[0], point[1])
        self._t.dot(None, 'red')

    def mark_home(self):
        cur_pos = self._t.pos()
        self._t.home()
        self.draw_point()
        self._t.setpos(cur_pos)

    def draw_shape(self, vertices, color='green'):
        self._t.penup()
        for x, y in vertices:
            self._t.setpos(x, y)
            self._t.pendown()
        self._t.setpos(vertices[0][0], vertices[0][1])

    @staticmethod
    def done():
        turtle.done()
