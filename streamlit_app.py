from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import openai

import json

import requests

import streamlit as st

openai.api_key="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"

def generate_headline(input_text):

    completion = openai.Completion.create(

        model="text-davinci-002",

        prompt="""given a topic provided by the user, generate at least five attention grabbing titles and headlines on different perspectives that follow specific formats,

               one title should use specific numbers and data in the headline. It should utilize unique rationales like ways, tips, tricks, ideas, facts, and similar words.Another title should use emotional words and provide a sense of urgency.The next title should try to use all the headline formulas.Two additional titles should follow any other format of your choice.

                titles and headlines should be short, clear, and direct, as well as unexpected and surprising. They should aim to catch the reader's attention and be highly shareable. The user can then select which title suits their needs the best:""",

        temperature=0.7,

        max_tokens=60,

        top_p=1,

        frequency_penalty=0,

        presence_penalty=0

    )

    headline = completion.choices[0].text

    return headline

if st.button("Generate Headline"):

    input_text = st.text_input("Enter a topic:")

    if input_text:

        with st.spinner('Generating your headline....'):

            result = generate_headline(input_text)

            st.text(result)

            st.success('done')


"""
# Welcome to Streamlit!

Edit holiday`/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
