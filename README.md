# AI Voice & Web Assistant

This AI Voice Assistant is a modular desktop and web-based jarvis style voice assistant. It uses a Naive Bayes machine learning classifier (`scikit-learn`) to understand user commands. This version includes a clean **Streamlit UI** alongside its core modules, allowing you to control Jarvis via both text and voice.

---

## Project Structure

```text
voice-assistant/
│
├── main.py                # Console entry point for the assistant
├── requirements.txt      # Project dependencies
│
├── assistant/            # Core processing engine
│   ├── __init__.py
│   ├── speech.py         # Voice recognition & text-to-speech engine
│   ├── intents.py        # Intent dictionary definitions
│   ├── ml_model.py       # Scikit-learn training & prediction logic
│   ├── actions.py        # Execution handlers (Apps, Volume, Wiki)
│   └── brain.py          # Unified request orchestration engine
│
├── ui/
│   └── app.py            # Streamlit graphical web application
│
└── assets/               # Storage for icons, styles, or local data
```

---

## System Prerequisites

Before initializing the workspace, ensure your operating system has the necessary underlying audio capture and automation headers.

### Windows
* Ensure a working microphone is enabled in your system settings.

### Linux (Ubuntu / Debian)
Install compilation files for audio stream processing and graphical window control:
```bash
sudo apt update
sudo apt install -y portaudio19-dev python3-dev xdotool ALSA-utils espeak
```

---

## Installation & Environment Setup with `uv`

### Step 0: Install uv

```bash
pip install uv      #For Windows
pip3 install uv     #For Linux
```

### Step 1: Initialize the Environment
Navigate to your project root folder and create a virtual environment:
```bash
uv init voice-assistant
cd voice-assistant
uv venv
```

### Step 2: Install Project Dependencies
Use `uv pip` to resolve and pull everything specified in your `requirements.txt`:
```bash
uv add -r requirements.txt
```
---

## How to Run the Assistant

You can launch Jarvis either through the CLI terminal environment or via the Streamlit web dashboard.

### Option A: Run via Web Dashboard (Streamlit)
To interact using a graphical panel with visual log messaging:
```bash
uv run streamlit run ui/app.py
```

### Option B: Run via Console Terminal
To run exclusively inside your local terminal application using standard voice loop protocols:
```bash
uv run main.py
```

---

## User Guide & Application Features

### Web UI Functions
* **Text Input:** Type direct commands into the main entry window and click **Send**.
* **Voice Input:** Click **Speak**, talk clearly into your mic, and wait for processing.
* **Message Board:** A history of your chat session renders cleanly below the divider.

### Supported Intent Queries
Always precede spoken voice commands with your wake word **"jarvis"** (e.g., *"Jarvis, play music"*). Text commands inside the Streamlit box do not require the wake prefix.

* **Media Controls:** *"play music by Queen"*, *"volume up"*, *"mute volume"*
* **Utility Queries:** *"what is the time"*, *"today date"*
* **App Ecosystem:** *"open chrome"*, *"open vs code"*
* **Knowledge Queries:** *"tell about Artificial Intelligence"* $\rightarrow$ *"tell more"*
