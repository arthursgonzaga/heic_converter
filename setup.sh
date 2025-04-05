#!/bin/bash

VENV_NAME="venv"

echo "🔧 Creating virtual environment..."
python3 -m venv $VENV_NAME

echo "✅ Virtual environment created. Activating..."
source $VENV_NAME/bin/activate

echo "📦 Installing dependencies..."

# Set macOS flags if needed (e.g. Apple Silicon)
if [[ "$OSTYPE" == "darwin"* ]]; then
  export CFLAGS="-I/opt/homebrew/include"
  export LDFLAGS="-L/opt/homebrew/lib"
fi

pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo "👉 To activate the virtual environment later, run:"
echo "   source $VENV_NAME/bin/activate"
