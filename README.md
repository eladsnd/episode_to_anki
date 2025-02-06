# 🎬 Episode to Anki - Sentence Mining Tool 📚

This project extracts **sentences, audio clips, images, and translations** from an **anime or any Japanese video/audio** and formats them into an **Anki-compatible CSV**. The goal is to learn Japanese through the **+1 word learning method**, introducing minimal new vocabulary per sentence.

---

## 🚀 Features
✅ **Extracts sentences** using OpenAI's **Whisper** speech-to-text  
✅ **Extracts audio clips** for each sentence using **FFmpeg**  
✅ **Extracts images** from the episode using **OpenCV**  
✅ **Translates sentences** using **DeepL / Google Translate**  
✅ **Orders sentences** to introduce **only 1 new word at a time** (`+1 method`)  
✅ **Saves output as an Anki-compatible CSV**  
✅ **Progress bar** for better visualization of the process  

---

## 🛠️ Installation

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed, then run:
```bash
pip install -r requirements.txt
```

### **2️⃣ Install FFmpeg**
- **Windows:** [Download FFmpeg](https://ffmpeg.org/download.html) and add it to `PATH`
- **Mac:** `brew install ffmpeg`
- **Linux:** `sudo apt install ffmpeg`

---

## 📂 Project Structure
```
episode_to_anki/
│── main.py                # Main entry point
│── config.py              # Configuration settings (paths, models, etc.)
│── utils/                 # Helper modules
│   ├── transcriber.py     # Handles Whisper speech-to-text transcription
│   ├── audio_extractor.py # Extracts audio clips
│   ├── image_extractor.py # Extracts images from video
│   ├── translator.py      # Translates sentences
│   ├── sentence_orderer.py# Orders sentences by +1 word method
│   ├── csv_writer.py      # Saves output in Anki-compatible CSV format
│── data/                  # Output files
│   ├── anki_audio/        # Stores generated MP3 audio files
│   ├── anki_images/       # Stores extracted images
│   ├── anki_sentences.csv # Final output CSV for Anki
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
```

---

## 🏃 Usage
### **1️⃣ Place Your Episode File**
Put your **.mp4** or **.mp3** file in the project root.

### **2️⃣ Update `config.py` (Optional)**
Modify paths and model settings in **`config.py`** if needed:
```python
EPISODE_FILE = "your_episode.mp4"  # Change to your file
OUTPUT_CSV = "data/anki_sentences.csv"
WHISPER_MODEL = "small"  # Options: tiny, small, medium, large
```

### **3️⃣ Run the Program**
```bash
python main.py
```
This will:
- **Extract sentences**
- **Extract audio clips**
- **Extract images**
- **Translate sentences**
- **Sort them by the +1 word method**
- **Save everything in an Anki-compatible CSV**

---

## 📄 **Output: Anki-Compatible CSV**
The final CSV is saved in **`data/anki_sentences.csv`**, with the following columns:

| Sentence | Audio File | Image | Translation | New Words |
|----------|-----------|-------|-------------|-----------|
| おはよう | [sound:audio_0.mp3] | <img src='image_0.jpg'> | Good morning | おはよう |
| おはようございます | [sound:audio_1.mp3] | <img src='image_1.jpg'> | Good morning (formal) | ございます |
| これはペンです | [sound:audio_2.mp3] | <img src='image_2.jpg'> | This is a pen | これ, ペン |

---

## 📥 **Importing into Anki**
### **1️⃣ Copy Media Files**
Move the **MP3 and image files** into Anki's `collection.media` folder:
- **Windows:** `C:\Users\YourUser\AppData\Roaming\Anki2\User 1\collection.media`
- **Mac/Linux:** `~/Library/Application Support/Anki2/User 1/collection.media`

### **2️⃣ Import the CSV into Anki**
- Open **Anki → File → Import**
- Select **`data/anki_sentences.csv`**
- Match the fields accordingly:
  - **Front**: Sentence
  - **Back**: Translation
  - **Audio**: Audio File
  - **Image**: Image
  - **Extra**: New Words
- Click **"Import"** 🎉

---

## 🛠 **Configuration (`config.py`)**
Modify `config.py` to adjust:
- **File paths**
- **Whisper model** (`small`, `medium`, `large`)
- **Translation settings**

Example:
```python
# Paths
EPISODE_FILE = "one_piece.mp4"
AUDIO_DIR = "data/anki_audio"
IMAGE_DIR = "data/anki_images"
OUTPUT_CSV = "data/anki_sentences.csv"

# Whisper Model (Options: "tiny", "small", "medium", "large")
WHISPER_MODEL = "small"
```

---

## 🔥 Advanced Features
- 📌 **+1 Word Learning Order:** Sentences are **ordered** so you always **learn only 1 new word** at a time.
- 🎵 **Audio Support:** Extracts **MP3 clips** of each sentence.
- 🎞 **Images from Episode:** Captures a **frame** from the episode at the right moment.
- 🌎 **Translations Included:** Auto-translates sentences into English.
