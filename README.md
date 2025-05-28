# 🧠 Context-Aware Gemini Chat (Console)

A simple multi-turn chatbot that uses the **Google Gemini Free API** to maintain full conversation context. The chatbot runs in the terminal and remembers previous user inputs, allowing for contextual follow-ups.

---

## 📦 Features

- Supports **multi-turn conversations** with context preservation.
- Tracks the **entire conversation history** manually.
- Uses **Google Gemini 1.5 Flash** model.
- Simple **console-based input/output**.
- Configurable **temperature** via code.
- Secure usage with a `.env` file for the API key.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rawatshubham1645/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` File

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

⚠️ **Do NOT share or commit your `.env` file or API key.**

---

## ▶️ How to Run

```bash
python gemini_chat.py
```

You'll see a prompt in your terminal. Start chatting with the bot.

To exit, simply type:

```
exit
```

---

## 💬 Example Interaction

```
🌡️ Enter temperature (0.0 - 1.0): 0.7
You: My name is Shubham Rawat.
Gemini: Nice to meet you, Shubham Rawat!

You: What did I say earlier?
Gemini: You said your name is Shubham Rawat.
```

---

## 🧠 How It Works
-Temperature can be customized at runtime by user input
- The script tracks each message (user + model) in a `history` list.
- Before each new message, it sends the full history to Gemini using `generate_content(history)`.
- This ensures full **context awareness** across turns.

---

## 📁 Project Structure

```
gemini-multi-turn-chat/
├── .env                # Contains your Gemini API key (not committed)
├── gemini_chat.py      # Main chatbot script
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation
```
