# Jarvis Voice Assistant

**Jarvis Voice Assistant** is a Python-based personal assistant that can perform various tasks using voice commands. It includes features like time, weather updates, Google search, Wikipedia search, playing jokes, and much more.

This project uses libraries like `pyttsx3` for text-to-speech, `SpeechRecognition` for voice recognition, and external APIs like `WeatherAPI`, `NewsAPI`, and others for fetching real-time data.

---

### **Features**
- **Voice Command Recognition**: Uses the `SpeechRecognition` library to process user voice input.
- **Voice Output**: Jarvis responds via speech using the `pyttsx3` library.
- **Time and Date**: Ask Jarvis for the current time and date.
- **Weather**: Fetch current weather data from **WeatherAPI**.
- **Google Search**: Search Google with voice commands.
- **Wikipedia Search**: Search Wikipedia for any topic.
- **YouTube Search**: Search YouTube using voice.
- **Jokes and Advice**: Tell random jokes and give advice.
- **News**: Fetch the latest news headlines from **NewsAPI**.
- **Open Applications**: Open and close apps like **Discord** and **Telegram**.

---

### **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MRxO11/jarvis-voice-assistant.git
   cd jarvis-voice-assistant

Install the required libraries: You can install the dependencies using pip:
pip install -r requirements.txt

Set up API Keys:

- For WeatherAPI: Get your API key from WeatherAPI.
- For NewsAPI: Get your API key from NewsAPI.
- Modify the api_key variables in the code: Replace the empty strings with your actual API keys for both WeatherAPI and NewsAPI.

How to Use:

Run the Assistant: To start the assistant, run the following Python script:
**python jarvis.py**

Voice Commands: Jarvis will listen to voice commands and respond accordingly. You can ask Jarvis to:

- Tell the time: "What is the time?"
- Tell the date: "What is the date today?"
- Search Google: "Search Google for [query]"
- Search Wikipedia: "Search Wikipedia for [query]"
- Search Youtube: "Search Youtube for[query]"
- Tell a joke: "Tell me a joke"
- Give advice: "Give me some advice"
- Open apps: "Open Discord" / "Close Discord" / "Open Telegram" / "Close Telegram" / "Open CMD" / "Close CMD"
- Fetch news: "What is the latest news?"

Wake Word Detection: The assistant supports wake word detection, listening for the words "terminator" or "jarvis" to activate it.

To Run it Just Say "JARVIS" and wait for it to recognize then say "Wake Up" After that it will start listening for your commands


![Screenshot 2024-11-14 223330](https://github.com/user-attachments/assets/a153cfb0-81d8-4c69-9c2f-0d5897ef034b)

**Important Notes**

To use wake word detection, you need to set up Picovoice Porcupine and input your access key.
Ensure you have the required APIs and dependencies set up in your environment for all features to work correctly.

**Contributing**

Feel free to fork the repository, make improvements, and submit pull requests. Contributions are always welcome!
