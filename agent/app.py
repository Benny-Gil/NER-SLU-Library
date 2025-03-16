import streamlit as st

st.title("SLU Library NER DEMO")

st.write("This is a demo of the NER model trained on the SLU Library dataset.")

if "input" not in st.session_state:
    st.session_state["input"] = ""

with st.form(key="ner_form"):
    st.write("Enter a sentence to extract named entities:")
    st.text_input("Input", key="input")
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.write("You entered:", st.session_state["input"])