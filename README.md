# Writing-Assistant


This is a creative writing assistant that helps writers overcome writer’s block using thought-provoking prompts, gentle reflection, and creative nudges using LLaMA 3.2 via Ollama and LangChain.

This is not a content generator. It doesn't write for you — it **guides you to think better**, reflect deeper, and get un-stuck.

---

## ✨ Features

* 🏈 **Reflective Mode**: Calm, supportive questions to help you reconnect with your creative voice
* 🧠 **Socratic Mode**: Minimal, open-ended questioning to guide your own insight
* 🎇 **Creative Spark Mode**: Unexpected angles, scene flips, or perspective changes

---

## 📁 Project Structure

```
writers_block/
├── main.py                      # Main loop
├── chains/
│   ├── reflective.py            # Reflective guidance chain
│   ├── socratic.py              # Socratic question chain
│   └── spark.py                 # Creative nudges chain
└── .venv/                       # Virtual environment
|
```

---

## 🚀 Setup & Run

### 1. Install Ollama(https://ollama.com/)

Make sure it’s running with the LLaMA 3.2 model:

```bash
ollama run llama3.2
```


### 2. Clone this repo & create a virtual environment https://github.com/eleonoraferns/Writing-Assistant

```bash
git clone 
cd writing-assistant
python -m venv .venv
.venv\Scripts\activate  # (or source .venv/bin/activate on Mac/Linux)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

---

## 💠 Tech Stack

* **Python** 3.11+
* **LangChain** (core + community)
* **Ollama** (local LLMs — uses `llama3.2` here)
* No external APIs, no OpenAI key needed 🔓

---

## 📌 Why This Project?

Built to help real writers think more clearly, rather than replace their creativity.

Sometimes, you don’t need a full paragraph.
You just need a **good question** and a **little nudge** 

---

## 📈 Future Scope

* [ ] Add memory to recall past responses
* [ ] GUI version
* [ ] Export session as a mini reflection journal
* [ ] Automatically adjust mode based on how *stuck* the user is.

---

> Built with a little writer’s desperation.

