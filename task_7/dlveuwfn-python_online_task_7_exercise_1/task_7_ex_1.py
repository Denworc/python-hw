class Rectangle:
    def __init__(self, a: float = 4.0, b: float = 3.0):
        if a <= 0 or b <= 0:
            raise ValueError

        self.__side_a = a
        self.__side_b = b

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def is_square(self):
        return self.__side_a == self.__side_b

    def replace_sides(self):
        self.__side_a, self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n: int = 0):
        rectangle_array = []

        for rectangle in args:
            if isinstance(rectangle, Rectangle):
                rectangle_array.append(rectangle)
            else:
                rectangle_array.extend(rectangle)
        if len(rectangle_array) < n:
            rectangle_array += [None] * (n - len(rectangle_array))
        self.__rectangle_array = rectangle_array

    def add_rectangle(self, new_rectangle: Rectangle) -> bool:
        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle is None:
                self.__rectangle_array[i] = new_rectangle
                return True
        return False

    def number_max_area(self) -> int:
        max_area = 0
        max_area_index = 0

        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle is not None and rectangle.area() > max_area:
                max_area = rectangle.area()
                max_area_index = i
        return max_area_index

    def number_min_perimeter(self) -> int:
        min_perimeter = float("inf")
        min_perimeter_index = 0

        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle is not None and rectangle.perimeter() < min_perimeter:
                min_perimeter = rectangle.perimeter()
                min_perimeter_index = i
        return min_perimeter_index

    def number_square(self) -> int:
        number_square = 0

        for rectangle in self.__rectangle_array:
            if rectangle is not None and rectangle.is_square():
                number_square += 1
        return number_square
