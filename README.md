# 🤖 Web Design Bot – Create Websites Easily

**WebStyle 2.0** is an open-source bot for the Telegram app that uses artificial intelligence to provide real-time assistance in basic web design (HTML, CSS, and some simple JavaScript).

The bot interacts with users through the Telegram chat, guiding them step by step to create a personalized website.  
The main idea is to make web design accessible to individuals and small businesses without the need for advanced programming knowledge or expensive tools.

With **WebStyle 2.0** (an improved version over the previous one), the goal is to demonstrate that it is possible to create a creative project without spending a lot of money or resources.

---

**Testing ↘️**
This is a test video of the WebStyle 2.0 Bot.  
Testing how the bot works and interacts with users. 🤖

[Click here to watch the video](https://youtube.com/shorts/-2ieAw50lt0?si=8IMCIAz99Tkp_-wW)

**➡️**
[🔗 Try the bot here](https://t.me/WwwebStylebot)

---

## 🚀 Features

### Key Features:

1. **Interactive Questions**
    - Type of website (corporate, blog, online store, portfolio, educational, newsletter, etc.)
    - Primary color
    - Secondary color
    - Tertiary color
    - Visual style (minimalistic, modern, classic, creative, or free)
    - Layout (one-page, navigable sections, grid of cards, sidebar menu, others…)

2. **Smart Suggestions from the AI Implementation**
    - Predefined HTML/CSS templates adapted to the user's answers.
    - Automatic injection of color palette and style into a CSS file.
    - Creative ideas and suggestions for the website to be developed.
    - Essential content required for the specific type of website.

3. **Real-Time Assistance**
    - Users can ask questions in the chat and receive code snippets to copy and paste into their website.
    - Basic JavaScript tips when necessary (e.g., adding an interactive button).

4. **Easy to Use**
    - No installation required beyond having the Telegram app/web.
    - Use `/start` command to begin the bot and inline buttons so that even non-technical users can navigate easily.

5. **Open Source and Free**
    - MIT License, allowing the community to review, learn, contribute, and extend the project.

---

## 🛠️ How to Use

1. **Start the bot** with `/start`.
2. **Answer questions** about the type of page, colors, and structure.
3. **Receive your ready-to-use HTML, CSS and Java code** to copy and paste.

---

## 📂 Project Structure
│── /docs → Contains questions.pdf and Sketch_Idea.pdf 📄
│── bot_Telegram.py → Main bot code
│── README.md → Project documentation
│──CONTRIBUTING_WebStyle.md → Contribution guidelines for WebStyle.
│──Wiki_and_Devlog_WebStyle.md → Developer documentation and project devlog.

---

## 🔧 Technologies Used

- **Python** → Logic of the bot.
- **python-telegram-bot** → For Telegram integration.
- **PlantUML** → For planning diagrams.
- **HTML, CSS and a little bit of JS** → Generation of well-structured code with best practices.

---

## 🌐 Online Demo

The **WebStyle 2.0** bot is available on Telegram. It can be accessed directly via the Telegram web or mobile app.

- **No installation required** except for having the Telegram app on your device or accessing Telegram via the web at [https://web.telegram.org](https://web.telegram.org).
- Simply interact with the bot by typing `/start`, answering a few questions about your website preferences, and receiving a fully generated HTML and CSS template with JavaScript functionalities for you to use.

This bot is **not hosted as a web demo** outside of Telegram because its primary function is to be accessible within the **Telegram ecosystem**. The goal is to provide a **simple and accessible web design experience** directly through the app, without the need for setting up additional web hosting or platform accounts.

For a **seamless experience**, simply use the bot on your Telegram app or through the [Telegram web interface](https://web.telegram.org).

---

## 📜 License

**MIT License**

Copyright (c) [2025] [Francisco Castro Gomez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# 🧠 How to Launch Locally WebStyle Bot.

---
⬇️⬇️⬇️
---

### 1. Clone the repository.

```bash
git clone https://github.com/Currogomez/WebStyle.git
cd WebStyle
```

---

### 2. Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# .\venv\Scripts\activate  # On Windows
```

---

### 3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, generate it with `pip freeze > requirements.txt` after installing your packages.

---

### 4. Create a `.env` file.

Create a `.env` file in the root directory with the following content:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
```

> Replace the values with your actual Telegram bot token and OpenRouter API key.

---

### 5. Run the bot.

```bash
python main.py
```

> If your main file has a different name, replace `main.py` with the correct filename.

---

### 6. Interact with the bot.

Open Telegram, search for your bot, and type `/start` or any other command you’ve set up. The bot should respond accordingly.

---

## 🧩 Notes.

- Use `python3` and `pip3` if you're on Mac and face issues with `python`.
- To keep your bot running 24/7, consider using `screen`, `tmux`, or deploying it to a cloud server.

---
