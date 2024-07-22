# Install the necessary packages first
# pip install taipy

from taipy.gui import Gui, State

# Function to double the input value
def double_input(state: State):
    state.output_value = state.input_value * 2

# Define the initial state
state = {
    "input_value": 1,
    "output_value": 2
}

# Define the GUI layout
page = """
<|layout|columns=1|gap=10px|
    <|NumberInput|value={input_value}|label="Input Value"|>
    <|Button|label="Double the Value"|on_action=double_input|>
    <|Text|text="Output Value: {output_value}"|>
|>
"""

# Initialize the Gui
gui = Gui(page=page)

# Assign the state and functions
gui.state = state
gui.functions = {'double_input': double_input}

# Run the GUI
if __name__ == "__main__":
    gui.run()
