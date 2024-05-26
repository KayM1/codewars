from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # point1 = Point(50, 50)
    # point2 = Point(200, 100)
    # point3 = Point(500,500)
    # line = Line(point1, point2)
    # line2 = Line(point2, point3)
    # win.draw_line(line, "red")
    # win.draw_line(line2, "green")

    # c1 = Cell(win)
    # c1.has_right_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(100, 50, 150, 100)

    # c1.draw_move(c2)

    # c3 = Cell(win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw(100, 100, 150, 150)

    # c2.draw_move(c3)

    # c4 = Cell(win)
    # c4.has_left_wall = False
    # c4.draw(150, 100, 200, 150)

    # c3.draw_move(c4, True)


    maze = Maze(10, 10, 20, 20, 40, 40, win)
    maze.solve()

    win.wait_for_close()

main()