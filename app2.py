import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
if st.button("Test this one_now I know why it failed before"):
  time_series = np.random.randn(100)
  plt.plot(time_series)
  plt.title("Random 100-unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Values")
  st.pyplot(plt.gcf())
