# Install Taipy
# !pip install taipy

from taipy.gui import Gui
import time
import datetime

# Function to get the current time
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the timer
start_time = time.time()

# Initial time
current_time = get_current_time()
load_time = None

# Define the page layout
layout = """
# Current Time
<|{current_time}|>

<|Refresh|button|on_action=refresh_time|>

# Load Time
<|Load Time: {load_time} seconds|>
"""

# Function to refresh the time
def refresh_time(state):
    state.current_time = get_current_time()
    if state.load_time is None:
        state.load_time = round(time.time() - start_time, 2)

# GUI configuration
gui = Gui(page=layout)
gui.run()

# Update load time after GUI is running
end_time = time.time()
load_time = round(end_time - start_time, 2)
print(f"Taipy Load Time: {load_time} seconds")
