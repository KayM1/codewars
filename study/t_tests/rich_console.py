from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import to_formatted_text
import random

# Object statuses and logic
statuses = ["OK", "Warning", "Critical"]

# Initialize objects and their status
objects = {"Object A": "OK", "Object B": "OK", "Object C": "OK"}

# Change the status of the object randomly on click
def change_status(object_name):
    objects[object_name] = random.choice(statuses)

# Function to generate the formatted text with mouse event handler
def get_text_with_mouse_handler(object_name):
    status = objects[object_name]
    
    if status == "OK":
        color = "green"
    elif status == "Warning":
        color = "yellow"
    else:
        color = "red"

    # Create formatted text with a mouse handler
    text = [
        (f"{color} bold", f"{object_name}: {status}", lambda mouse_event: change_status(object_name) if mouse_event.event_type == "MOUSE_UP" else None)
    ]
    
    # Convert the text to formatted text that prompt_toolkit understands
    return FormattedTextControl(to_formatted_text(text))

# Create the layout with clickable objects
def render_objects():
    return [Window(content=get_text_with_mouse_handler(obj_name), height=1) for obj_name in objects]

# Key bindings to quit the application
kb = KeyBindings()

@kb.add('q')
def quit_app(event):
    event.app.exit()

# Application style
style = Style.from_dict({
    'green': 'fg:green bold',
    'yellow': 'fg:yellow bold',
    'red': 'fg:red bold',
})

# Main loop for interactive app
app = Application(
    layout=Layout(HSplit(render_objects())),  # Display the object rows
    key_bindings=kb,
    style=style,
    full_screen=False,
    mouse_support=True,  # Enable mouse support
)

# Run the application
if __name__ == "__main__":
    print("Press 'q' to quit. Click on objects to change their status.")
    app.run()
