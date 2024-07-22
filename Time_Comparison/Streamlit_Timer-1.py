# Install Streamlit
# !pip install streamlit

import streamlit as st
import time
import datetime

# Start the timer
start_time = time.time()

# Function to get the current time
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Display the current time
st.title("Current Time")
current_time = st.text(get_current_time())

# Button to refresh the time
if st.button("Refresh"):
    current_time.text(get_current_time())

# Calculate and display load time
end_time = time.time()
load_time = round(end_time - start_time, 2)
st.write(f"Streamlit Load Time: {load_time} seconds")
