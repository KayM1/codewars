from graphics import Point, Line

class Cell:
    def __init__(self, window, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall 
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited=False
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        point_tl = Point(self._x1, self._y1)
        point_br = Point(self._x2, self._y2)
        point_bl = Point(self._x1, self._y2)
        point_tr = Point(self._x2, self._y1)
        left_wall = Line(point_tl, point_bl)
        right_wall = Line(point_tr, point_br)
        top_wall = Line(point_tl, point_tr)
        bottom_wall = Line(point_bl, point_br)

        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        else:
            self._win.draw_line(left_wall, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall, "black")
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall, "black")
        else:
            self._win.draw_line(top_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "black")
        else:
            self._win.draw_line(bottom_wall, "white")
    
    def draw_move(self, to_cell, undo=False):
        if undo==False:
            color = "red"
        else:
            color = "light gray"
        start_point_x = ((self._x1 + self._x2)/2)
        start_point_y = ((self._y1 + self._y2)/2)
        point_start = Point(start_point_x, start_point_y)
        end_point_x = ((to_cell._x1 + to_cell._x2)/2)
        end_point_y = ((to_cell._y1 + to_cell._y2)/2)
        point_end = Point(end_point_x, end_point_y)
        print(f"drawing line from {start_point_x}, {start_point_y} to {end_point_x}, {end_point_y}")
        self._win.draw_line(Line(point_start, point_end), color)
