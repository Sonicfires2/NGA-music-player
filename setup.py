#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
import urllib.request
import zipfile
import tarfile
import shutil
from pathlib import Path

# List of Python packages to install
REQUIRED_PACKAGES = ["yt-dlp", "pygame", "prompt_toolkit"]

# Install required Python packages via pip
def install_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", *REQUIRED_PACKAGES])

# Download, extract, and locate ffmpeg binary
def setup_ffmpeg():
    system = platform.system()

    # macOS: use Homebrew for ffmpeg (includes ffprobe)
    if system == "Darwin":
        ff = shutil.which("ffmpeg")
        if ff:
            print(f"✅ Found system ffmpeg at: {ff}")
            return os.path.dirname(ff)
        brew = shutil.which("brew")
        if brew:
            print("⬇️ Installing ffmpeg via Homebrew...")
            subprocess.check_call(["brew", "install", "ffmpeg"])
            ff = shutil.which("ffmpeg")
            if ff:
                print(f"✅ ffmpeg installed at: {ff}")
                return os.path.dirname(ff)
        print("❌ Homebrew not found. Please install Homebrew from https://brew.sh and rerun.")
        sys.exit(1)

    ffmpeg_dir = Path("ffmpeg")

    # Check common local binary paths
    candidates = [
        ffmpeg_dir / "bin" / "ffmpeg",
        ffmpeg_dir / "ffmpeg"
    ]
    for candidate in candidates:
        if candidate.exists():
            path = candidate.parent.resolve()
            print(f"✅ ffmpeg found at: {candidate.resolve()}")
            return str(path)

    print("⬇️ Downloading ffmpeg static build...")
    if system == "Windows":
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        archive = "ffmpeg.zip"
    elif system == "Linux":
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
        archive = "ffmpeg.tar.xz"
    else:
        raise RuntimeError(f"Unsupported OS: {system}")

    urllib.request.urlretrieve(url, archive)
    ffmpeg_dir.mkdir(exist_ok=True)
    if archive.endswith(".zip"):
        with zipfile.ZipFile(archive, "r") as zip_ref:
            zip_ref.extractall(ffmpeg_dir)
    else:
        with tarfile.open(archive) as tar_ref:
            tar_ref.extractall(ffmpeg_dir)
    os.remove(archive)

    # Locate ffmpeg binary
    for root, dirs, files in os.walk(ffmpeg_dir):
        if "ffmpeg" in files:
            binary = Path(root) / "ffmpeg"
            print(f"✅ ffmpeg extracted to: {binary.resolve()}")
            return str(binary.parent.resolve())

    raise FileNotFoundError("ffmpeg binary not found after extraction.")

# Hide the pygame support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

if __name__ == "__main__":
    install_packages()
    ffmpeg_loc = setup_ffmpeg()
    # Write ffmpeg location to file for downloader
    with open("ffmpeg_path.txt", "w") as f:
        f.write(ffmpeg_loc)
    print(f"ℹ️ Saved ffmpeg location to ffmpeg_path.txt: {ffmpeg_loc}")
