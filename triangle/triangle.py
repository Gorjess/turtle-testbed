""" ************ Dancing Bunny ************
* Created by: Cap Turtle
* DateTime: 2022/11/14 16:19 
* Desc:
*************************************** """
import random
import time

from turtle_util.util import TurtleUtil


class Triangle:
    def __init__(self, vertices):
        self._vertices = vertices

    def vertices(self):
        return self._vertices

    def pick_point(self):
        """
        随机获取一个内部位置
        :return:
        """
        random.seed(time.time_ns())
        f1 = random.random()
        f2 = random.random()

        origin = self._vertices[0]
        offset_x, offset_y = origin[0], origin[1]

        v1 = ((self._vertices[1][0] - self._vertices[0][0]) * f1, (self._vertices[1][1] - self._vertices[0][1]) * f1)
        f2_ = (1 - f1) * f2
        v2 = ((self._vertices[2][0] - self._vertices[0][0]) * f2_, (self._vertices[2][1] - self._vertices[0][1]) * f2_)
        return v1[0] + v2[0] + offset_x, v1[1] + v2[1] + offset_y


if __name__ == '__main__':
    t = TurtleUtil()
    t.mark_home()
    tg = Triangle([
        (50, 50),
        (350, 50),
        (200, 250)
    ])
    t.draw_shape(tg.vertices(), color='green')
    t.draw_point(color='orange', point=tg.pick_point())

    t.done()
