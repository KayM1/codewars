from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(1200, 900)
    maze = Maze(10, 10, 7, 7, 40, 40, win, False)
    

    win.wait_for_close()

main()