#!/bin/bash

# Jarvis AI - Automated Installer for Mac
# One command installation and setup for MacBook Pro 2026

echo ""
echo "================================================"
echo "    JARVIS AI - Automated Installer"
echo "    Owner: Doctor Yusuph Mponzi"
echo "    MacBook Pro 2026 (M-Series)"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python3 from https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python3 found!"
echo ""

# Install Homebrew if needed
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "✓ Homebrew ready!"
echo ""

# Install PortAudio
echo "Installing PortAudio (for microphone support)..."
brew install portaudio

echo "✓ PortAudio installed!"
echo ""

# Create virtual environment
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate

echo "✓ Virtual environment created!"
echo ""

# Install dependencies
echo "Installing dependencies (this may take 2-3 minutes)..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "Trying alternative installation method..."
    pip install -r requirements.txt --ignore-installed
fi

echo ""
echo "================================================"
echo "    ✓ INSTALLATION COMPLETE!"
echo "================================================"
echo ""
echo "🎤 STARTING JARVIS AI"
echo ""
echo "Try these commands:"
echo "  • 'What time is it?'"
echo "  • 'Tell me the date'"
echo "  • 'Open Google'"
echo "  • 'Search for [topic]'"
echo "  • 'Goodbye' (to exit)"
echo ""
echo "================================================"
echo ""

# Run Jarvis
python jarvis.py
