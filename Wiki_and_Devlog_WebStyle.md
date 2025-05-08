
# WebStyle 2.0 - Wiki and Devlog

## Wiki: Developer Documentation

### Overview

**WebStyle 2.0** is a Telegram bot built to help users generate HTML, CSS, and JavaScript templates easily. The goal is to provide a seamless way for individuals and small businesses to create websites without needing extensive web development knowledge. The bot interacts with users via Telegram and customizes templates based on their preferences.

### Project Structure

The main components of the project are:

```
│── /docs → Contains `questions.pdf` and `Sketch_Idea.pdf` 📄
│── bot_Telegram.py → Main bot code that handles user input and generates responses
│── README.md → Project documentation
│── requirements.txt → List of dependencies for the project
│── LICENSE → Project license file
```

- **bot_Telegram.py**: This is where the main bot logic resides. It listens for user input, prompts them for design preferences, and generates HTML, CSS, and JavaScript based on those preferences.
- **requirements.txt**: Contains all the dependencies needed to run the project, including libraries like `python-telegram-bot` for bot communication, and `openai` for the AI model.
- **docs**: This folder contains PDF files that provide additional information about the design and planning phases of the project.

### Key Components and Libraries

1. **python-telegram-bot**  
   This library is used for integrating with the Telegram API. It handles messages, commands, and updates from users.
   
2. **openai**  
   The AI model used to generate HTML, CSS, and JavaScript code based on user input. It provides the functionality that allows the bot to “understand” the user's requests and generate appropriate web design templates.

3. **dotenv**  
   Used for managing environment variables (e.g., Telegram Bot Token and OpenAI API Key).

4. **logging**  
   Used to log important events, errors, and information for debugging and tracking the bot's activity.

### How the Bot Works

1. **User Interaction**  
   - The bot begins by greeting the user and prompting them to choose a type of website (e.g., blog, portfolio, online store).
   - The bot then asks for colors, style, and layout preferences.
   - Based on the answers, the bot generates a corresponding HTML, CSS, and JavaScript template.

2. **Generating Templates**  
   - The bot uses **OpenAI’s API** to create the HTML structure. Based on the chosen layout and colors, it generates a clean, responsive design with accompanying CSS and JavaScript.
   - The generated templates are sent back to the user as downloadable files.

### Extending the Bot

To add new features, simply modify the conversation flow in `bot_Telegram.py`. You can also enhance the AI model’s capabilities by refining the prompts used to generate web templates, or by integrating more advanced AI features (like a more personalized design system).

### Running the Bot Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Currogomez/WebStyle.git
   cd WebStyle
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scriptsctivate  # On Windows
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables** in a `.env` file:
   ```
   TELEGRAM_TOKEN=your_telegram_token
   OPENAI_KEY=your_openai_key
   ```

5. **Run the bot**:
   ```bash
   python bot_Telegram.py
   ```

---

## Devlog: Stages of the Project

**Project Devlog - WebStyle 2.0**  
This section will serve as the development log, detailing the key stages of the project and updates shared with the community. I’ve documented the development process on LinkedIn for each major milestone to share my progress with others in the industry.

### Stage 1: Initial Planning and Conceptualization  
The first stage was brainstorming the idea for the bot. The motivation was simple: **make web design accessible to everyone**, especially for people with no technical background. I wanted to create something that could simplify the process of web design by using the **Telegram app**, which is already widely used.

- **Key goals**:
   - Allow users to create a basic website without any coding knowledge.
   - Provide a simple and accessible interface through a Telegram bot.
   - Enable users to customize their site with just a few questions (type of site, colors, style).

**LinkedIn Post:**  
"In the initial stages of creating a Telegram bot that helps generate websites. The goal: make web design easier for non-tech users. #WebDesign #AI #TelegramBots #StartupJourney"

### Stage 2: Bot Development and OpenAI Integration  
Once the idea was solidified, the development began. The hardest part was figuring out how to integrate **OpenAI** to generate the HTML/CSS code dynamically. After some experimentation, I was able to connect the OpenAI model to generate responsive templates.

- **Key achievements**:
   - Set up the **Telegram bot** using `python-telegram-bot`.
   - Integrated **OpenAI’s GPT-3** to generate HTML and CSS code.
   - Defined the user experience with simple prompts (questions about colors, style, and layout).
   
**LinkedIn Post:**  
"Integration with OpenAI is going smoothly! Now users can interact with a bot that generates HTML/CSS based on their preferences. The first real-time template is coming together. #AI #TelegramBots #OpenAI #WebDesign"

### Stage 3: Testing and Refining  
With the bot functional, it was time to test it with real users. I reached out to a few people to try out the bot and give feedback. It became clear that there were a few key areas that could be improved, such as the AI’s ability to generate more complex layouts.

- **Key improvements**:
   - Refined the AI prompts to ensure more accurate and varied templates.
   - Enhanced user interaction by adding more customizable options.
   - Improved the design responsiveness to cater to mobile and desktop views.

**LinkedIn Post:**  
"Getting great feedback from users! The bot now generates more responsive and customizable templates. Making it even smarter with better design suggestions! #UserTesting #WebDesign #AI #TelegramBots"

### Stage 4: Launch and Future Enhancements  
The bot is now fully functional and deployed! Users can easily generate HTML, CSS, and even JavaScript templates. I plan to continually improve the AI’s capabilities, and future updates will focus on expanding the range of templates and adding more interactive features.

- **Plans for the future**:
   - Add **JavaScript interactivity** such as form validation, popups, etc.
   - Allow users to choose between **multiple frameworks** like Bootstrap or Tailwind CSS.
   - Translate the bot interface into different languages to reach a broader audience.

**LinkedIn Post:**  
"Exciting to launch WebStyle 2.0! It’s an AI-driven Telegram bot that generates websites. Stay tuned for future updates. #Launch #WebDesign #AI #TechStartup"

### Conclusion of the Devlog  
Throughout the development of **WebStyle 2.0**, I’ve been constantly learning new things, especially about AI integration and making it accessible to non-technical users. The goal has always been to democratize web design, and this project is only the beginning of many exciting updates. I look forward to seeing how users interact with the bot and what ideas they have for future versions.

