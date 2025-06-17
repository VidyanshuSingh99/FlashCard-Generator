import streamlit as st
from llm_utils import generate_flashcards
from utils import extract_text_from_pdf

st.set_page_config(page_title="Flashcard Generator", layout="centered")
st.title("📚 AI Flashcard Generator (DeepSeek via OpenRouter)")

input_option = st.radio("Choose Input Type", ["Paste Text", "Upload File"])
subject = st.selectbox("📘 Select Subject (optional)", ["", "Biology", "History", "Physics", "Computer Science", "Geography"])
difficulty = st.selectbox("🎯 Select Difficulty Level (optional)", ["", "Easy", "Medium", "Hard"])

input_text = ""

if input_option == "Paste Text":
    input_text = st.text_area("Paste your educational content here:")
else:
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            input_text = extract_text_from_pdf(uploaded_file)
        else:
            input_text = uploaded_file.read().decode("utf-8")

if st.button("Generate Flashcards"):
    if not input_text.strip():
        st.warning("Please enter or upload valid content.")
    else:
        with st.spinner("Calling LLM..."):
            try:
                flashcards = generate_flashcards(input_text, subject, difficulty)
                st.success("✅ Flashcards generated!")
                st.text_area("🧠 Flashcards Output", flashcards, height=400)
            except Exception as e:
                st.error(f"Error: {e}")
