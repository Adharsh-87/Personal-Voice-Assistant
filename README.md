# Personal-Voice-Assistant
Create your own personal assistant which can do tasks on behalf of you..

# 🗣️ Personal Voice Assistant using Python

A smart, customizable **Personal Voice Assistant** built with Python that listens to your commands, responds intelligently, and performs a variety of useful tasks — such as searching the web, opening apps, playing music, fetching news, and more!

---

## 🚀 Features

- 🎙️ **Voice Recognition:** Understands and responds to voice commands.
- 💬 **Text-to-Speech (TTS):** Speaks responses using natural voice output.
- 🌐 **Web Integration:** Opens websites, performs Google searches, and fetches online data.
- 🕒 **System Utilities:** Opens applications, checks the time/date, tells jokes, and more.
- 🧠 **Custom Commands:** You can add your own commands easily in the code.
- 📰 **Optional:** News/weather updates, YouTube search, or automation (if added).

---

## 🧩 Tech Stack

- **Language:** Python 3.x  
- **Libraries Used:**  
  - `speech_recognition` — for converting speech to text  
  - `pyttsx3` — for text-to-speech  
  - `datetime` — to get current date/time  
  - `wikipedia` — to fetch summaries  
  - `webbrowser` — to open URLs  
  - `os` — to control local apps/files  
  - *(Add more if you used — e.g., `requests`, `pywhatkit`, etc.)*

---

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   
Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

Install dependencies
pip install -r requirements.txt

Run the assistant
python voice_assistant.py

🗂️ Project Structure
📁 Personal-Voice-Assistant/
│
├── voice_assistant.py     
├── requirements.txt        
├── README.md              
└── assets/                  

🧠 How It Works

The assistant listens through the microphone 🎧
Speech is converted to text using speech_recognition
It matches your command to a predefined action
The assistant performs the task and responds using pyttsx3 voice output 🔊

💡Example Commands
Try saying...
"What’s the time?"
"Open YouTube"
"Search for Artificial Intelligence on Google"
"Tell me a joke"
"Who is Elon Musk?"
"Play music"

License:
This project is licensed under the MIT License


⭐ If you like this project, give it a star on GitHub!

