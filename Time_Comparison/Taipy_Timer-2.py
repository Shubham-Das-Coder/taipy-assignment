# taipy_app.py

from taipy.gui import Gui
import pandas as pd
import time
import matplotlib.pyplot as plt
import io

path = None
data = None
upload_time = None
plot_time = None
plot_image = None

md = """
<|{path}|file_selector|label=Upload dataset|on_action=load_csv_file|extensions=.csv|>

<|{upload_time}|text|label=Upload Time|>
<|{plot_time}|text|label=Plot Time|>

<|{data}|table|rebuild|>

<|{plot_image}|image|>
"""

def load_csv_file(state):
    start_time = time.time()
    state.data = pd.read_csv(state.path)
    state.upload_time = f"Upload Time: {time.time() - start_time:.2f} seconds"
    
    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.scatter(state.data['Age'], state.data['Income'], label='Age vs Income')
    plt.title('Age vs Income')
    plt.xlabel('Age')
    plt.ylabel('Income')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot.png')
    plt.close()
    state.plot_time = f"Plot Time: {time.time() - start_time:.2f} seconds"
    state.plot_image = 'plot.png'

Gui(md).run()
