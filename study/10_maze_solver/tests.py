import unittest
from graphics import Window
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(20, 20, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        win.wait_for_close()

    def test_maze_create_cells2(self):
        num_cols = 5
        num_rows = 5
        win = Window(1200, 900)
        m1 = Maze(30, 30, num_rows, num_cols, 40, 20, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

  
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(10, 10, num_rows, num_cols, 30, 30, win)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )



if __name__ == "__main__":
    unittest.main()

