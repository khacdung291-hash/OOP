import math
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
class Circle:
    def __init__(self, center, radius):
        self.center, self.radius = center, radius
class Rectangle:
    def __init__(self, w, h, corner):
        self.width, self.height, self.corner = w, h, corner
circle = Circle(Point(150, 100), 75)
def point_in_circle(c, p):
    return (p.x - c.center.x)**2 + (p.y - c.center.y)**2 <= c.radius**2
def rect_in_circle(c, r):
    pts = [
        r.corner,
        Point(r.corner.x + r.width, r.corner.y),
        Point(r.corner.x, r.corner.y + r.height),
        Point(r.corner.x + r.width, r.corner.y + r.height)
    ]
    return all(point_in_circle(c, p) for p in pts)
def rect_circle_overlap(c, r):
    x = min(max(c.center.x, r.corner.x), r.corner.x + r.width)
    y = min(max(c.center.y, r.corner.y), r.corner.y + r.height)
    return (c.center.x - x)**2 + (c.center.y - y)**2 <= c.radius**2