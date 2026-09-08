# Diseases in Agriculture — Streamlit Study & Test App

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Flow

1. Study Unit
2. 10 MCQs
3. Instant score + explanations
4. 30-minute written test (5 × 2 marks + 1 × 5 marks)
5. Write answers on paper
6. Timer locks the written test
7. A 30-second transition message appears: "I am grateful to you for chatting to ordinary people like us."
8. The next unit starts automatically after 30 seconds

Question/content data is stored in `questions.py`.
