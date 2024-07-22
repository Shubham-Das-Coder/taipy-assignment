# streamlit_app.py

import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import io

def upload_and_plot(file):
    start_time = time.time()
    df = pd.read_csv(io.StringIO(file.read().decode('utf-8')))
    upload_time = time.time() - start_time

    start_time = time.time()
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Age'], df['Income'], label='Age vs Income')
    plt.title('Age vs Income')
    plt.xlabel('Age')
    plt.ylabel('Income')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot.png')
    plt.close()
    plot_time = time.time() - start_time

    return upload_time, plot_time

def main():
    st.title("CSV Upload and Plotting")
    uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])
    if uploaded_file is not None:
        upload_time, plot_time = upload_and_plot(uploaded_file)
        st.write(f"Upload Time: {upload_time:.2f} seconds")
        st.write(f"Plot Time: {plot_time:.2f} seconds")
        st.image('plot.png', caption='Plot of Age vs Income')

if __name__ == "__main__":
    main()
