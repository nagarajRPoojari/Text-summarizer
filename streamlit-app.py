import streamlit as st
import PyPDF2
import io 
from textSummarizer.pipeline.prediction import PredictionPipeline
import warnings
from contextlib import contextmanager

@contextmanager
def suppress_streamlit_warnings():
    original_showwarning = warnings.showwarning
    warnings.showwarning = lambda *args, **kwargs: None
    yield
    warnings.showwarning = original_showwarning


st.set_page_config(layout="wide")
st.title('Text Summarizer')


@st.cache(allow_output_mutation=True)
def load_model():
    predictor = PredictionPipeline()
    return predictor

model = load_model()
col1, col2 = st.columns([1, 1])

input_text = col1.text_area("Enter your text:", height=300)

uploaded_file = col1.file_uploader("Upload a text or PDF file", type=["txt", "pdf"])



if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1].lower()

    if file_extension == 'pdf':
        pdf_content = uploaded_file.read()
        if pdf_content:
            pdf_text = ""

            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

            input_text = pdf_text
        else:
            st.warning("The uploaded PDF file is empty.")
    elif file_extension == 'txt':
        uploaded_text = uploaded_file.read()
        if uploaded_text:
            input_text = uploaded_text.decode("utf-8", errors="ignore")
        else:
            st.warning("The uploaded text file is empty.")


if col1.button("Generate Summary"):
    if input_text:
        summary = model.predict(input_text)
        uploaded_file=None
        limited_text=input_text[:500]
        col2.subheader("Generated Summary")
        col2.write(summary)

    else:
        st.warning("Please enter text or upload a text or PDF file for summarization.")







