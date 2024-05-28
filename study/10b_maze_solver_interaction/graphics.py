from tkinter import Tk, BOTH, Canvas, Entry, Button, Label, Frame, TOP

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

        # interactions:
        # Create a frame for the input fields and button
        self.__frame = Frame(self.__root)
        self.__frame.pack(side=TOP, pady=10)
        
        self.__label_rows = Label(self.__frame, text="Rows:")
        self.__label_rows.grid(row=0, column=0)

        self.__label_size = Label(self.__frame, text="Size:")
        self.__label_size.grid(row=0, column=4)
        
        self.__entry_rows = Entry(self.__frame)
        self.__entry_rows.grid(row=0, column=1)
        self.__entry_rows.insert(0, "40")
        
        self.__label_cols = Label(self.__frame, text="Columns:")
        self.__label_cols.grid(row=1, column=0)
        
        self.__entry_cols = Entry(self.__frame)
        self.__entry_cols.grid(row=1, column=1)
        self.__entry_cols.insert(0, "40")

        self.__entry_size = Entry(self.__frame)
        self.__entry_size.grid(row=0, column=5)
        self.__entry_size.insert(0, "20")

        self.__label_speed = Label(self.__frame, text="Speed: ")
        self.__label_speed.grid(row=1, column=4)

        self.__entry_speed = Entry(self.__frame)
        self.__entry_speed.grid(row=1, column=5)
        self.__entry_speed.insert(0, "0.01")
        
        
        self.__button_go = Button(self.__frame, text="GO!", command=self.start_simulation)
        self.__button_go.grid(row=2, column=0, columnspan=2, pady=10)

        self.__button_solve = Button(self.__frame, text="Solve!", command=self.solve_simulation)
        self.__button_solve.grid(row=2, column=2, columnspan=3, pady=1)

        self.maze = None

    def start_simulation(self):     # !!! circular reference
        from maze import Maze
        rows = int(self.__entry_rows.get())
        cols = int(self.__entry_cols.get())
        size = int(self.__entry_size.get())
        speed = float(self.__entry_speed.get())
        self.create_maze(rows, cols, size, speed)
    
    def create_maze(self, rows, cols, size, speed): # !!! circular reference
        self.__canvas.delete("all")
        from maze import Maze
        # Example values for position and cell size
        self.maze = Maze(10, 10, rows, cols, size, size, self, None, True, speed)
    
    def redraw_maze(self):
        self.__canvas.delete("all")  # Clear the canvas
        # Drawing logic goes here
        if self.maze is not None:
            self.maze.draw()
    
    def solve_simulation(self):
        from maze import Maze
        self.maze.solve()
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2
        )



