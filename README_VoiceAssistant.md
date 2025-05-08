# Voice Activated Assistant – Jarvis

This project is a Python-based voice-activated assistant named **Jarvis**, designed to perform basic tasks through voice commands.
It serves as a foundational framework for building more advanced voice-controlled applications.

## Features

- **Voice Recognition**: Utilizes speech recognition to process user commands.
- **Text-to-Speech**: Provides vocal responses using text-to-speech capabilities.
- **Basic Commands**: Performs simple tasks like telling the time or opening websites.
- **Extensible Architecture**: Structured to allow easy addition of new functionalities.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ThomasStoyles/Voice_Activated_Assistant.git
   cd Voice_Activated_Assistant
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3 installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If `requirements.txt` is not present, manually install the necessary libraries such as `speechrecognition`, `pyttsx3`, and `pywhatkit`.

## Usage

1. **Run the Assistant**:
   ```bash
   python main.py
   ```

2. **Interact with Jarvis**:
   - Upon running, Jarvis will await your voice commands.
   - Speak clearly into your microphone to issue commands like "What time is it?" or "Open YouTube."
   - Jarvis will process your command and respond accordingly.

## Project Structure

- `main.py`: The main script that initializes and runs the voice assistant.
- `Scripts/`: Directory containing auxiliary scripts and modules.
- `pyvenv.cfg`: Configuration file for the Python virtual environment.
- `pywhatkit_dbs.txt`: Database file used by the `pywhatkit` library.

## Future Enhancements

- **Expanded Command Set**: Incorporate more complex commands and functionalities.
- **GUI Integration**: Develop a graphical user interface for easier interaction.
- **Improved Error Handling**: Enhance robustness to handle unexpected inputs gracefully.
- **Cross-Platform Support**: Ensure compatibility across different operating systems.

## License

This project is open-source and available under the [MIT License](LICENSE).
