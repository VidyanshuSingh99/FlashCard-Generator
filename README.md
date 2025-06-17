# 📚 AI Flashcard Generator

An AI-powered tool that converts educational content — like notes or PDFs — into flashcards (Q&A format). Perfect for students, educators, or lifelong learners!

---

## ⚙️ How It Works

- 🔑 Uses [DeepSeek R1 (Free)](https://openrouter.ai/models/deepseek/deepseek-r1) via OpenRouter API
- 🌐 Built with **Streamlit** for an interactive web UI
- 📄 Supports direct text input or uploading PDF/TXT files
- 🧠 Converts content into 10–15 question-answer flashcards using an LLM

---

## 🚀 Setup Instructions

These steps are for Windows users (other OS users: just change the virtual environment syntax accordingly):

## 1. Clone this repository and open it in VS Code

git clone https://github.com/yourusername/AI-FlashCard-Generator.git
cd AI-FlashCard-Generator

# 2. Set up and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install the required libraries
pip install -r requirements.txt

# 4. Configure your API key
Create a new file called .env in the root of the project and add your OpenRouter API key:

OPENROUTER_API_KEY=sk-your-api-key-here
TITLE=Flashcard Generator

# 5. Run the Streamlit app
streamlit run app.py


##  App Features
Choose between pasting text or uploading a file
Optional dropdowns for subject and difficulty level
Flashcards are generated in real-time and displayed in the app



# Sample Input
🇮🇳 India’s Independence: A Brief Overview
(Includes events like the 1857 revolt, Gandhi’s movements, Partition of India, Nehru, etc.)



# Sample Output
Here are some flashcards the model generated for the above content:

Q1: What event in 1857 led to British colonial rule in India?
A1: The Revolt of 1857, after which the British Crown took control from the East India Company.

Q2: Name two negative effects of British rule.
A2: Economic exploitation and political suppression.

Q3: What organization was founded in 1885 during early nationalism?
A3: The Indian National Congress (INC).

Q4: What 1905 event sparked mass protests?
A4: The Partition of Bengal.

...

(and so on, with 15 total flashcards)

