import analyzer
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
import streamlit as st
import plotly.express as px


# Get all files in a specific folder
filepaths = sorted(glob.glob('diary/*.txt'))

negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath) as file:
        diary_entries = file.read()
    scores = analyzer.polarity_scores(diary_entries)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]


#Add title, text input, slider, selectio and subheader
st.title("Mood Analysis")
st.subheader("Positivity")

pos_figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})

st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)