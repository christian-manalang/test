import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("GROUP 4")
st.header("Laptop Prices Dataset")

df = pd.read_csv("laptop_price.csv")

df.head(10)

df.info
