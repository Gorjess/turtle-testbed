# **********************************
# * Author: Cap Turtle
# * Date: 11/14/2022 2:16 PM
# * Description:
# **********************************

import time
import turtle
import random

"""
See more details at: https://alienryderflex.com/polygon/
//  Globals which should be set before calling this function:
//
//  int    polyCorners  =  how many corners the polygon has (no repeats)
//  float  polyX[]      =  horizontal coordinates of corners
//  float  polyY[]      =  vertical coordinates of corners
//  float  x, y         =  point to be tested
//
//  (Globals are used in this example for purposes of speed.  Change as
//  desired.)
//
//  The function will return YES if the point x,y is inside the polygon, or
//  NO if it is not.  If the point is exactly on the edge of the polygon,
//  then the function may return YES or NO.
//
//  Note that division by zero is avoided because the division is protected
//  by the "if" clause which surrounds it.

bool pointInPolygon() {

  int   i, j=polyCorners-1 ;
  bool  oddNodes=NO      ;

  for (i=0; i<polyCorners; i++) {
    if (polyY[i]<y && polyY[j]>=y
    ||  polyY[j]<y && polyY[i]>=y) {
      if (polyX[i]+(y-polyY[i])/(polyY[j]-polyY[i])*(polyX[j]-polyX[i])<x) {
        oddNodes=!oddNodes; }}
    j=i; }

  return oddNodes; }
"""


class Polygon:
    def __init__(self, vertices):
        self._vertices = vertices

    def vertices(self):
        return self._vertices

    def pick_edge_point(self, n):
        """
        随机获取一个边上的点
        :param n:
        :return:
        """
        vts = self._vertices
        length = len(vts)
        i, j = 0, length - 1
        picked = 0
        ps = []
        while picked < n:
            if i == length:
                i = 0
                j = length - 1

            random.seed(time.time_ns())
            factor = random.random()
            vec = vts[j][0] - vts[i][0], vts[j][1] - vts[i][1]
            ps.append((vec[0] * factor + vts[i][0], vec[1] * factor + vts[i][1]))
            picked += 1
            j = i
            i += 1
        random.shuffle(ps)
        return ps


def _new_rect(x, y, w, h):
    """
    创建一个矩形
    :param x:
    :param y:
    :param w: width
    :param h: height
    :return:
    """
    return [
        (x, y),
        (x+w, y),
        (x+w, y+h),
        (x, y+h)
    ]


def _randomly_dist_points(n):
    """
    返回一组随机分布的点
    :param n:
    :return:
    """
    random.seed(time.time_ns())

    def rand():
        return random.randint(0, 200)

    points = [None] * n
    for i in range(n):
        points[i] = (
            rand(), rand()
        )
    return points


def _new_poly(n):
    """
    创建一个具有 n 个顶点的多边形
    :param n: 顶点数
    :return: 顶点数组
    """
    return _randomly_dist_points(n)


def point_inside_polygon(point, vertices):
    """
    校验 point 是否在由 vertices 所组成的多边形中
    :param point:
    :param vertices:
    :return:
    """
    n = len(vertices)
    if n < 3:
        return False

    xs, zs = [], []
    for x, z in vertices:
        xs.append(x)
        zs.append(z)

    x, z = point[0], point[1]
    j = n - 1
    odd = False

    for i in range(n):
        if zs[i] < z <= zs[j] or zs[j] < z <= zs[i]:
            if xs[i] + (z - zs[i]) * (xs[j] - xs[i]) / (zs[j] - zs[i]) < x:
                odd = not odd
        j = i

    return odd


def draw():
    turtle.setup(800, 600)
    t = turtle.Turtle()
    t.hideturtle()

    def point(x, y):
        t.setpos(x, y)

    def point_dot(x, y):
        t.penup()
        point(x, y)
        t.dot()
        t.pendown()

    t.color('green')
    poly = _new_rect(0, 0, 200, 200)
    for v in poly:
        point(v[0], v[1])
    t.pendown()
    t.home()

    t.color('red')
    p = (100, 100)
    point_dot(p[0], p[1])

    check = point_inside_polygon(p, poly)

    t.penup()
    t.setpos(-100, -100)

    if check:
        t.write("INSIDE", font=("Arial", 16, "normal"))
    else:
        t.write('OUTSIDE', font=("Arial", 16, "normal"))

    turtle.done()


if __name__ == '__main__':
    draw()
