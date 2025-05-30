import subprocess
import os
import shutil


def find_ffmpeg():
    """
    Locate ffmpeg:
      1) Check if system ffmpeg is on PATH
      2) Fallback to path stored in ffmpeg_path.txt
    Returns the directory containing the ffmpeg binary, or None if not found.
    """
    # 1) system ffmpeg?
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return os.path.dirname(system_ffmpeg)

    # 2) local copy?
    if os.path.exists("ffmpeg_path.txt"):
        with open("ffmpeg_path.txt", "r") as f:
            path = f.read().strip()
        if os.path.isdir(path) and os.path.exists(os.path.join(path, "ffmpeg")):
            return path

    return None


def download_audio(query):
    """
    Download and convert YouTube audio to MP3 using yt-dlp.
    """
    os.makedirs("downloads", exist_ok=True)

    ffmpeg_loc = find_ffmpeg()
    cmd = ["yt-dlp"]

    if ffmpeg_loc:
        cmd.append(f"--ffmpeg-location={ffmpeg_loc}")
        print(f"▶️ Using ffmpeg at: {ffmpeg_loc}")
    else:
        print("⚠️ No ffmpeg found: downloading only webm")

    cmd += [
        "-x",
        "--audio-format", "mp3",
        f"ytsearch1:{query}",
        "-o", "downloads/%(title)s.%(ext)s"
    ]

    print("🔄 Running command:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("❌ yt-dlp failed:", result.stderr)
