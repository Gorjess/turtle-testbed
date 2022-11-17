# **********************************
# * Author: Cap Turtle
# * Date: 11/17/2022 4:41 PM
# * Description: 
# **********************************
import math
import random
import time
from turtle_util.util import TurtleUtil


class Circle:
    def __init__(self, center, radius):
        self._center = center
        self._radius = radius

    def center(self):
        return self._center

    def radius(self):
        return self._radius

    def points_within(self, n):
        points = []
        for i in range(n):
            random.seed(time.time_ns())
            r = self._radius * math.sqrt(random.random())
            theta = random.random() * 2 * math.pi
            p = (self._center[0] + r * math.cos(theta), self._center[1] + r * math.sin(theta))
            points.append(p)
            time.sleep(0.01)
        return points


if __name__ == '__main__':
    t = TurtleUtil()
    c = Circle([0, 0], 100)
    t.draw_circle(c.center(), c.radius())
    t.draw_point(point=c.center(), color='grey')
    ps = c.points_within(3)
    for x, y in ps:
        t.draw_point(point=(x, y))

    t.done()
