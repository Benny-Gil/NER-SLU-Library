# usage: streamlit run app.py

import streamlit as st
import streamlit.components.v1 as components
import spacy
from spacy import displacy

st.set_page_config(page_title="SLU Library NER Demo", layout="wide")

@st.cache_resource
def load_model():
    return spacy.load("training/output/model-best")

nlp = load_model()

st.title("SLU Library NER DEMO")

st.write("This is a demo of the NER model trained on the SLU Library dataset.")

if "input" not in st.session_state:
    st.session_state["input"] = ""

with st.form(key="ner_form"):
    st.write("Enter a sentence to extract named entities:")
    st.text_input("Input", key="input")
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        doc = nlp(st.session_state.input)
        
        # Generate the HTML visualization
        html = displacy.render(doc, style="ent", page=True)
        
        # Display the visualization in Streamlit
        components.html(html, height=300,scrolling=True)
        
        # Optionally, display entities in a table format too
        if doc.ents:
            entities_data = [(ent.text, ent.label_) for ent in doc.ents]
            st.write("### Extracted Entities:")
            st.table({
                "Text": [ent[0] for ent in entities_data],
                "Type": [ent[1] for ent in entities_data]
            })
        else:
            st.info("No named entities were found in the text.")