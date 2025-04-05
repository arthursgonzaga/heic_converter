# HEIC Converter 🖼️ ➜ 📸

A simple Python tool to convert `.heic` image files to `.jpeg` or `.png`.

## Features

- 🔁 Convert single `.heic` files
- 📁 (Optional) Batch conversion support
- ✅ Lightweight dependencies

## Setup

1. Clone this repository:

```bash
git clone https://github.com/your-username/heic-converter.git
cd heic-converter
```

2. Run the setup script to create a virtual environment and install dependencies:

```bash
chmod a+x setup.sh
./setup.sh
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. To convert a single file:

```bash
python convert.py path/to/image.heic jpeg
```

Replace jpeg with png if you prefer.

## Requirements

Python 3.7+
libheif installed on your system (may be required for some platforms)

## macOS Setup Notes (Apple Silicon / Intel)

If you see an error like:

`fatal error: 'libheif/heif.h' file not found`

You need to install libheif on your system using Homebrew:

```bash
brew install libheif
```

If the error persists, try setting the following environment variables before installing:

```bash
export CFLAGS="-I/opt/homebrew/include"
export LDFLAGS="-L/opt/homebrew/lib"
pip install pyheif
```

This is already handled automatically if you run the setup.sh script.