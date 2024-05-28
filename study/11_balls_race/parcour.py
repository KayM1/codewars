import tkinter as tk
import time

# Set up the main window
root = tk.Tk()
root.title("Ball Animation")

bottom_cv = 400
right_cv = 400

# Set up canvas
canvas = tk.Canvas(root, width=right_cv, height=bottom_cv, bg="black")
canvas.pack()

# Create a blue ball
blue_ball = canvas.create_oval(195, 10, 225, 40, fill="blue")
blue_ball_radius = 5

# create a red ball
red_ball = canvas.create_oval(205, 10, 235, 40, fill="red")
red_ball_radius = 5

# Define ball properties
blue_x_velocity = -2
blue_y_velocity = 0.5
red_x_velocity = 0.3
red_y_velocity = 1
gravity = 0.1
bounce_factor = -0.9

# Function to animate the ball
def animate():
    global blue_x_velocity, blue_y_velocity, red_x_velocity, red_y_velocity

    # Move the balls
    canvas.move(blue_ball, blue_x_velocity, blue_y_velocity)
    canvas.move(red_ball, red_x_velocity, red_y_velocity)

    # Get blue ball coordinates
    blue_x1, blue_y1, blue_x2, blue_y2 = canvas.coords(blue_ball)
    blue_center_x = (blue_x1 + blue_x2) / 2
    blue_center_y = (blue_y1 + blue_y2) / 2
    blue_bottom = blue_y2

    # Get red ball coordinates
    red_x1, red_y1, red_x2, red_y2 = canvas.coords(red_ball)
    red_center_x = (red_x1 + red_x2) / 2
    red_center_y = (red_y1 + red_y2) / 2
    red_bottom = red_y2


    # Check collision between blue and red balls
    distance = ((red_center_x - blue_center_x) ** 2 + (red_center_y - blue_center_y) ** 2) ** 0.5
    if distance <= blue_ball_radius + red_ball_radius:
        # If collision, adjust velocities to simulate bounce
        blue_x_velocity *= bounce_factor*1.05
        canvas.move(blue_ball, blue_x_velocity, blue_y_velocity - distance)
        blue_y_velocity *= bounce_factor*1.05
        red_x_velocity *= bounce_factor*1.05
        red_y_velocity *= bounce_factor*1.05

    # Bounce off the walls and floor for blue ball
    if blue_x1 <= 0 or blue_x2 >= 400:
        blue_x_velocity *= bounce_factor
    if blue_y1 <= 0:
        blue_y_velocity = abs(blue_y_velocity)  # Ensure positive velocity
    if blue_bottom >= 400:
        blue_y_velocity = -abs(blue_y_velocity)  # Ensure negative velocity
        canvas.move(blue_ball, 0, 400 - blue_bottom)

    # Bounce off the walls and floor for red ball
    if red_x1 <= 0 or red_x2 >= 400:
        red_x_velocity *= bounce_factor
    if red_y1 <= 0:
        red_y_velocity = abs(red_y_velocity)  # Ensure positive velocity
    if red_bottom >= 400:
        red_y_velocity = -abs(red_y_velocity)  # Ensure negative velocity
        canvas.move(red_ball, 0, 400 - red_bottom)

    # Apply gravity
    # blue_y_velocity += gravity
    # red_y_velocity += gravity


    # Repeat animation
    root.after(1, animate)

# Start animation
animate()

root.mainloop()