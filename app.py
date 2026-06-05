import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.title("Smart Analytics Tool")
file=st.file_uploader("Uploaded CSV File",type=["csv"])
if file is not None:
  df=pd.read_csv(file)
  st.header("Dataset Preview")
  st.write("First 5 rows: ")
  st.write(df.head())
  st.write("Last 5 rows: ")
  st.write(df.tail())
  st.write("shape: ")
  st.write(df.shape)
  st.write("Features: ")
  st.write(df.columns.tolist())
  st.write("Data types: ")
  st.write(df.dtypes)
  st.header("Missing Value Analysis")
  missingValues=df.isnull().sum()
  st.dataframe(missingValues)
  fig=px.bar(x=missingValues.index,y=missingValues.values,title="Missing value analysis",labels={"x":"Columns","y":"Missing values"})
  st.plotly_chart(fig)

  st.header("Statistical Summary")
  st.write(df.describe())

  numeric_columns=df.select_dtypes(include=np.number).columns.tolist()

  st.header("Histogram")
  hist_column=st.selectbox("Select column for histogram: ",numeric_columns)
  fig=px.histogram(df,x=hist_column,title=f"Histogram of {hist_column}")
  st.plotly_chart(fig)

  st.header("Box plot")
  box_column=st.selectbox("Select column for box plot: ",numeric_columns)
  fig=px.box(df,x=box_column,title=f"box plot of {box_column}")
  st.plotly_chart(fig)

  st.header("Scatter plot")
  x_column=st.selectbox("Select X Axis: ",numeric_columns)
  y_column=st.selectbox("Select Y Axis: ",numeric_columns)
  fig=px.scatter(df,x=x_column,y=y_column,title=f"{x_column}vs{y_column}")
  st.plotly_chart(fig)

  st.header("Correlation Matrix")
  correlation = df[numeric_columns].corr()
  st.write(correlation)
  fig = px.imshow(correlation,text_auto=True,title="Correlation Matrix")
  st.plotly_chart(fig)

  
