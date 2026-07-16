#!/bin/bash

echo "⚡ Installing Power Center Extreme..."

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "❌ Error: Go is not installed on your system."
    echo "Please install Go (https://go.dev/doc/install) and try again."
    exit 1
fi

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR" || exit

echo "📥 Downloading source code..."
git clone https://github.com/Juan-Martin-Cerezo/power-center-extreme.git . &> /dev/null

echo "🔨 Compiling binary (requires root for installation)..."
go build -o power-center

# Move to a global bin directory
sudo mv power-center /usr/local/bin/power-center

# Clean up
cd /
rm -rf "$TEMP_DIR"

echo "✅ Installation complete!"
echo "🚀 You can now run the program from anywhere using:"
echo "   sudo power-center"
