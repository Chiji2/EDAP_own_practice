import matplotlib.pyplot as plt
import numpy as np
# import streamlit as st
# if st.button("Test this one"):
time_series = np.random.randn(100)
plt.plot(time_series)
plt.title("Random 100-unit Time Series")
plt.xlabel("Time")
plt.ylabel("Values")
plt.show()
