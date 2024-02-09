import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats

dataframe = pd.read_csv("data/house/house.csv")
dataframe["loyer_per_m2"] = dataframe.loyer / dataframe.surface
res = stats.linregress(dataframe.surface, dataframe.loyer)
x = np.arange(400)
y = res[0] * x + res[1]
df = pd.DataFrame()
df["x"] = x
df["y"] = y
st.scatter_chart(dataframe, x="surface", y="loyer")
st.line_chart(df, x="x", y="y")