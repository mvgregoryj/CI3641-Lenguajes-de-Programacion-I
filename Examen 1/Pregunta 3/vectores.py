class Vector(object):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vector2):
        if type(vector2) == Vector:
            return Vector(self.x + vector2.x, self.y + vector2.y, self.z + vector2.z)
        elif type(vector2 == int or vector2 == float):
            return Vector(self.x + vector2, self.y + vector2, self.z + vector2)


    def __sub__(self, vector2):
        if type(vector2) == Vector:
            return Vector(self.x - vector2.x, self.y - vector2.y, self.z - vector2.z)
        elif type(vector2 == int or vector2 == float):
            return Vector(self.x - vector2, self.y - vector2, self.z - vector2)

    def __mul__(self, vector2):
        if type(vector2) == Vector:
            return Vector(  self.y * vector2.z - self.z * vector2.y, 
                            self.z * vector2.x - self.x * vector2.z, 
                            self.x * vector2.y - self.y * vector2.x
                        )
        elif type(vector2 == int or vector2 == float):
            return Vector(self.x * vector2, self.y * vector2, self.z * vector2)
    
    def __mod__(self, vector2):
        return (self.x * vector2.x + self.y * vector2.y + self.z * vector2.z)

    def __str__(self) -> str:
        return f'<{self.x}, {self.y}, {self.z}>'.format(self=self)