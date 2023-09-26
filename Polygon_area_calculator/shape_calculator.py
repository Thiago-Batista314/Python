class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def get_diagonal(self):
        diagonal = float(((self.width ** 2) + (self.height ** 2)) ** 0.5)
        return diagonal

    def get_picture(self):
        picture = ''
        if self.height >= 50 or self.width >= 50: picture = 'Too big for picture.'
        else:
            for c in range(0, self.height):
                picture += '*' * self.width + '\n'
        return picture
    
    def get_amount_inside(self, shape):
        width = self.width // shape.width
        height = self.height // shape.height
        amount_inside = width * height
        return amount_inside


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
