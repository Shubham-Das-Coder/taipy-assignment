from taipy import Gui

# Define the content to be displayed
content = """
# Hello, World!

This is my first program using Taipy"""

# Create the GUI
gui = Gui(page=content)

# Run the GUI
gui.run()
