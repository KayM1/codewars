from cell import Cell
from graphics import Window
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed=None,
            start=False,
            speed=0.02
            ):
        
        if seed:
            seed = random.seed(seed)
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.start = start
        self.speed = speed
        self.draw()

    def draw(self):
        if self.start == True:
            self._create_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
        # for i in range(self.num_cols):
        #     for j in range(self.num_rows):
        #         self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        _top_maze=self.y1
        _side_maze=self.x1
        #  c1.draw(50, 50, 100, 100)
        top_lx = _side_maze + self.cell_size_x * i
        top_ly = _top_maze + self.cell_size_y * j
        bot_rx = top_lx + self.cell_size_x
        bot_ry = top_ly + self.cell_size_y
        self._cells[i][j].draw(top_lx, top_ly, bot_rx, bot_ry)

    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(self.speed)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            directions = []
            to_visit = []
            if i-1 >= 0 and i-1 < self.num_cols: 
                if self._cells[i-1][j].visited == False:
                    to_visit.append((i-1, j))
                    directions.append("Left")
                    self._animate()
            if i+1 >= 0 and i+1 < self.num_cols:
                if self._cells[i+1][j].visited == False:
                    to_visit.append((i+1, j))
                    directions.append("Right")
                    self._animate()
            if j+1 >= 0 and j+1 < self.num_rows:
                if self._cells[i][j+1].visited == False:
                    to_visit.append((i, j+1))
                    directions.append("Down")
                    self._animate()
            if j-1 >= 0 and j-1 < self.num_rows:
                if self._cells[i][j-1].visited == False:
                    to_visit.append((i, j-1))
                    directions.append("Up")
                    self._animate()
            # print(f"checking: {i},{j}, visited={self._cells[i][j].visited} -- to_visit: {to_visit}")
            if not to_visit:
            #    print("empty!")
                self._draw_cell(i, j)
                return
            else:
                random.shuffle(directions)
                direction = directions.pop()
                if direction == "Up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                    j -= 1
                if direction == "Down":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                    j += 1
                if direction == "Left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                    i -= 1
                if direction == "Right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                    i += 1
                self._draw_cell(i, j)
                self._break_walls_r(i, j)
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        if self.start == True:
            return self._self_r(0, 0)

    def _self_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        directions = []
        if not self._cells[i][j].has_top_wall and j > 0 and not self._cells[i][j-1].visited:
            directions.append("Up")
        if not self._cells[i][j].has_bottom_wall and j < self.num_rows - 1 and not self._cells[i][j+1].visited:
            directions.append("Down")
        if not self._cells[i][j].has_left_wall and i > 0 and not self._cells[i-1][j].visited:
            directions.append("Left")
        if not self._cells[i][j].has_right_wall and i < self.num_cols - 1 and not self._cells[i+1][j].visited:
            directions.append("Right")

        if not directions:
            return False
        random.shuffle(directions)

        random.shuffle(directions)
        
        for direction in directions:
            if direction == "Up":
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._self_r(i, j-1):
                    return True
                else:
                    self._cells[i][j-1].draw_move(self._cells[i][j], True)
            elif direction == "Down":
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._self_r(i, j+1):
                    return True
                else:
                    self._cells[i][j+1].draw_move(self._cells[i][j], True)
            elif direction == "Left":
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._self_r(i-1, j):
                    return True
                else:
                    self._cells[i-1][j].draw_move(self._cells[i][j], True)
            elif direction == "Right":
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._self_r(i+1, j):
                    return True
                else:
                    self._cells[i+1][j].draw_move(self._cells[i][j], True)
        
        return False
        



    
    




