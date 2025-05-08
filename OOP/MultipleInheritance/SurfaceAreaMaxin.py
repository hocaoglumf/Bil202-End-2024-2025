import Rectangle as rec

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)
        return surface_area

class Cube(rec.Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [rec.Square, rec.Square, rec.Square, rec.Square, rec.Square, rec.Square]

class RightPyramid(rec.Square, rec.Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [rec.Square, rec.Triangle, rec.Triangle, rec.Triangle, rec.Triangle]

cube=Cube(3)
cube.surface_area()

py=RightPyramid(5,7)
py.surface_area()