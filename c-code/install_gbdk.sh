#!/bin/bash

# GBDK-2020 Installation Script for Pokemon Yellow Legacy C Version

set -e

echo "=== Installing GBDK-2020 ==="

# Determine system architecture
ARCH=$(uname -m)
OS=$(uname -s)

if [ "$OS" = "Linux" ]; then
    if [ "$ARCH" = "x86_64" ]; then
        GBDK_URL="https://github.com/gbdk-2020/gbdk-2020/releases/download/4.4.0/gbdk-linux64.tar.gz"
        GBDK_FILE="gbdk-linux64.tar.gz"
    elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
        GBDK_URL="https://github.com/gbdk-2020/gbdk-2020/releases/download/4.4.0/gbdk-linux-arm64.tar.gz"
        GBDK_FILE="gbdk-linux-arm64.tar.gz"
    else
        echo "Error: Unsupported architecture: $ARCH"
        echo "Please download GBDK-2020 manually from:"
        echo "https://github.com/gbdk-2020/gbdk-2020/releases"
        exit 1
    fi
elif [ "$OS" = "Darwin" ]; then
    GBDK_URL="https://github.com/gbdk-2020/gbdk-2020/releases/download/4.4.0/gbdk-macos.tar.gz"
    GBDK_FILE="gbdk-macos.tar.gz"
else
    echo "Error: Unsupported OS: $OS"
    echo "Please download GBDK-2020 manually from:"
    echo "https://github.com/gbdk-2020/gbdk-2020/releases"
    exit 1
fi

# Download GBDK-2020
echo "Downloading GBDK-2020..."
if command -v wget >/dev/null 2>&1; then
    wget -O "$GBDK_FILE" "$GBDK_URL"
elif command -v curl >/dev/null 2>&1; then
    curl -L -o "$GBDK_FILE" "$GBDK_URL"
else
    echo "Error: Neither wget nor curl found. Please install one of them."
    exit 1
fi

# Extract GBDK-2020
echo "Extracting GBDK-2020..."
tar -xzf "$GBDK_FILE"

# Install to /opt/gbdk (with sudo) or local directory
if [ -w "/opt" ] || sudo -n true 2>/dev/null; then
    echo "Installing to /opt/gbdk (requires sudo)..."
    sudo rm -rf /opt/gbdk
    sudo mv gbdk /opt/gbdk
    GBDK_PATH="/opt/gbdk"
else
    echo "Installing to local directory..."
    mkdir -p "$HOME/.local"
    rm -rf "$HOME/.local/gbdk"
    mv gbdk "$HOME/.local/gbdk"
    GBDK_PATH="$HOME/.local/gbdk"
fi

# Clean up
rm -f "$GBDK_FILE"

echo ""
echo "✓ GBDK-2020 installed successfully!"
echo "  Installation path: $GBDK_PATH"
echo ""
echo "To use GBDK-2020, add this to your shell profile (~/.bashrc or ~/.zshrc):"
echo "  export GBDK_HOME=$GBDK_PATH"
echo "  export PATH=\$GBDK_HOME/bin:\$PATH"
echo ""
echo "Or run this command now:"
echo "  export GBDK_HOME=$GBDK_PATH && export PATH=\$GBDK_HOME/bin:\$PATH"
echo ""
echo "Then you can build Pokemon Yellow C version with:"
echo "  cd c-code"
echo "  ./build.sh"
