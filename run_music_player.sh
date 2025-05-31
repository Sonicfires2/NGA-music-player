#!/bin/bash
# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the venv
echo "Activating virtual environment..."
source venv/bin/activate

python3 setup.py

python main.py  # replace with your actual script