<h1 align="center">🎙️ Speech to Text (Persian)</h1>

<p align="center">
  <b>Convert Persian speech into clean, right-to-left text — from a file or live from your microphone.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Language-Persian%20(fa--IR)-green" alt="Persian">
  <img src="https://img.shields.io/badge/Output-TXT%20%7C%20DOCX-orange" alt="Output">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" alt="License">
</p>

---

## ✨ Overview

**Speech to Text** is a set of two Python programs that turn Persian speech into text.
Both use **Google Speech Recognition** (`fa-IR`) and export the result as **`.txt`** or **`.docx`**,
with full right-to-left layout and the **B Nazanin** font applied automatically in Word documents.

| Program | Input | Best for |
| :--- | :--- | :--- |
| 📄 `SpeechToText_File.py` | Audio file (`.wav`) | Transcribing long recordings, chunk by chunk |
| 🎤 `SpeechToText_Live.py` | Your microphone | Real-time, on-the-fly transcription |

---

## 📄 1) SpeechToText_File.py — Transcribe an Audio File

Feed it a pre-recorded audio file and get a full transcript back.

- 🕒 Asks for the **file duration** in minutes and seconds.
- ✂️ Processes the audio in **20-second chunks**, so long files stay memory-friendly.
- 🔁 Automatically **retries** any chunk that comes back empty, then moves on.
- 📊 Shows a live progress indicator (`xxs / total s`).
- 💾 Asks how you want to save the result: `.txt` or `.docx`.

---

## 🎤 2) SpeechToText_Live.py — Live Speech to Text

Talk directly into your microphone and watch the text appear.

- 🎧 Captures audio from the microphone and transcribes it in real time.
- ➕ Keeps appending each new segment to the transcript.
- 🛑 Stops when you say the word **"پایان"** (meaning *end*).
- 🛡️ Gracefully handles network and microphone errors with friendly messages.
- 💾 Saves the final transcript as `output.txt` or `output.docx`.

---

## ⚙️ Requirements

```bash  
pip install SpeechRecognition  
pip install arabic-reshaper  
pip install python-bidi  
pip install python-docx  
pip install sounddevice
```

ℹ️ Microphone capture uses sounddevice instead of pyaudio.
For the file-based program, FFmpeg is required for full audio-format support.

###

🧩 Shared Features
✅ Persian speech recognition (fa-IR)
✅ Dual output: TXT and DOCX
✅ Right-to-left, B Nazanin formatting in Word files
✅ Correct Persian rendering in the terminal (letter shaping + RTL)
✅ Persian error messages and input validation

###

🗂️ Project Structure
Speech_To_Text/
├── SpeechToText_File.py   # Audio file → text
├── SpeechToText_Live.py   # Live microphone → text
└── README.md

###

📌 Note
An active internet connection is required, since Google's speech engine runs online.
If the connection drops, the program shows a clear message and lets you retry.
