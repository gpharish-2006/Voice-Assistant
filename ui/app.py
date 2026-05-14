import streamlit as st
import sys,os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from assistant.brain import process_command
from assistant.speech import listen

st.set_page_config(
    page_title="Jarvis AI",
    page_icon="🤖",
    layout="centered"
)

st.title("Jarvis AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input(
    "Type your command"
)

col1, col2 = st.columns(2)

with col1:

    if st.button("Send"):

        if user_input:

            response = process_command(user_input)

            st.session_state.messages.append(
                ("You", user_input)
            )

            st.session_state.messages.append(
                ("Jarvis", str(response))
            )

with col2:

    if st.button("Speak"):

        text = listen()

        if text:

            response = process_command(text)

            st.session_state.messages.append(
                ("You", text)
            )

            st.session_state.messages.append(
                ("Jarvis", str(response))
            )

st.divider()

for sender, message in st.session_state.messages:

    if sender == "You":
        st.markdown(
            f"### {message}"
        )

    else:
        st.markdown(
            f"### {message}"
        )