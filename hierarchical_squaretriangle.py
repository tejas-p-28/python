class Area:
    def __init__(self, shape):
        print("welcome to the world of {} !!".format(shape))

class Triangle(Area):
    def __init__(self):
        super().__init__('Triangles')
    def area(self,h,b):
        print("area of triangle:",0.5*h*b)

class Square(Area):
    def __init__(self):
        super().__init__("Squares")
    def area(Self,s):
        print("area of square:",s*s)
if __name__ == "__main__":
    sq = Square()
    sq.area(6)
    tri = Triangle()
    tri.area(10,20)