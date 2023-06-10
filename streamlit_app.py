import openai 

import streamlit as st


import json

import requests

import streamlit as st

openai.api_key="sk-PghLUnl

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


