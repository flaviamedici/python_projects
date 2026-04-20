import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search For Happiness")

option1 = st.selectbox("Select the data for the x-axis",
                      ("GDP", "Happiness", "Generosity"))

option2 = st.selectbox("Select the data for the y-axis",
                      ("GDP", "Happiness", "Generosity"))


df = pd.read_csv("happy.csv")
print(df)

match option1:
    case "GDP":
        x_axis = df["gdp"]
    case "Happiness":
        x_axis = df["happiness"]
    case "Generosity":
        x_axis = df['generosity']

match option2:
    case "GDP":
        y_axis = df["gdp"]
    case "Happiness":
        y_axis = df["happiness"]
    case "Generosity":
        y_axis = df['generosity']

st.subheader(f"{option1} and {option2}")
print(x_axis)
print(y_axis)

figure = px.scatter(x=x_axis,
                    y=y_axis,
                    labels={"x": option1, "y": option2})
st.plotly_chart(figure)