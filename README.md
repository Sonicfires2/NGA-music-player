# 🎵 Terminal Music Player

A lightweight, terminal-based music player written in Python using [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit). This is a personal side project built for fun and experimentation.

## ✨ Features

- 🎧 **Play downloaded MP3 songs** directly in the terminal  
- 🧭 **Interactive song selection** with arrow keys or mouse  
- 🗑️ **Delete unwanted tracks** from within the app  
- ⬇️ **Search and download songs** using a text-based interface  
- 🛠️ Designed for a simple and responsive command-line experience

---

## 🚀 Getting Started

### 1. Clone the repository and navigate to the folder
```bash
git clone https://github.com/your-username/music-player
cd music-player
```

### 2. Run the startup script
```bash
chmod +x run_music_player.sh
./run_music_player.sh
```

> This script sets up a virtual environment (if not already created), activates it, and runs the main player script.

---

## 🕹️ How to Use

- Use the **arrow keys** or **mouse** to select a song from your local `downloads/` folder.
- Choose an action:
  - `1`: ▶️ Play the song
  - `2`: 🔙 Return to the song list
  - `3`: ❌ Exit the program
  - `4`: 🗑️ Delete the selected song (with confirmation)
- Use `Ctrl+C` anytime to safely quit the program.

---

## 📂 Directory Structure

```
music-player/
├── downloader.py        # Handles song download logic
├── player.py            # Plays MP3 files
├── run_music_player.sh  # Setup and launch script
├── main.py              # Main interactive UI
└── downloads/           # Folder where MP3s are saved
```

---

## 🔧 Requirements

- Python 3.7+
- `prompt_toolkit`
- `playsound` or your preferred MP3 playback library
- Internet access (for downloading songs)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## ❓ Notes

- This app does **not** ship with music. You must use the "Download Song" feature or place your `.mp3` files in the `downloads/` folder manually.
- Make sure your terminal supports mouse and keyboard input (most modern terminals do).

---

## 📜 License

MIT License. Free to use and modify. Feedback and contributions welcome!