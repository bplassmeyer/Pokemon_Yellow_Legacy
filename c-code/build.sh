#!/bin/bash

# Pokemon Yellow Legacy C Version Build Script

set -e  # Exit on any error

echo "=== Pokemon Yellow Legacy C Version Build ==="

# Check if GBDK_HOME is set
if [ -z "$GBDK_HOME" ]; then
    echo "Error: GBDK_HOME environment variable not set!"
    echo "Please install GBDK-2020 and set GBDK_HOME:"
    echo ""
    echo "Option 1 - Install GBDK-2020 automatically:"
    echo "  ./install_gbdk.sh"
    echo ""
    echo "Option 2 - Manual installation:"
    echo "  wget https://github.com/gbdk-2020/gbdk-2020/releases/download/4.4.0/gbdk-linux64.tar.gz"
    echo "  tar -xzf gbdk-linux64.tar.gz"
    echo "  sudo mv gbdk /opt/gbdk"
    echo "  export GBDK_HOME=/opt/gbdk"
    echo ""
    echo "Option 2 - Set existing GBDK path:"
    echo "  export GBDK_HOME=/path/to/your/gbdk"
    echo ""
    exit 1
fi

# Check if GBDK tools exist
if [ ! -f "$GBDK_HOME/bin/lcc" ]; then
    echo "Error: GBDK tools not found at $GBDK_HOME/bin/lcc"
    echo "Please install GBDK-2020 and set GBDK_HOME correctly."
    exit 1
fi

# Check if RGBDS is available
if ! command -v rgbfix &> /dev/null; then
    echo "Error: rgbfix (RGBDS) not found!"
    echo "Please install RGBDS: sudo apt install rgbds"
    exit 1
fi

echo "✓ GBDK found at: $GBDK_HOME"
echo "✓ RGBDS tools found"

# Navigate to c-code directory
cd "$(dirname "$0")"

echo ""
echo "Building tools..."
make tools || echo "Warning: Some tools may not build (this is often okay)"

echo ""
echo "Building Pokemon Yellow C version..."

# Build the ROM
if [ "$1" = "debug" ]; then
    echo "Building DEBUG version..."
    make yellow_debug DEBUG=1
    ROM_FILE="pokeyellow_debug.gbc"
else
    echo "Building RELEASE version..."
    make yellow
    ROM_FILE="pokeyellow.gbc"
fi

echo ""
echo "=== Build Complete! ==="

if [ -f "$ROM_FILE" ]; then
    echo "✓ ROM file created: $ROM_FILE"
    echo "  File size: $(ls -lh $ROM_FILE | awk '{print $5}')"
    echo ""
    echo "To test the ROM:"
    echo "  1. Load $ROM_FILE in a Game Boy emulator"
    echo "  2. Recommended emulators: SameBoy, VisualBoyAdvance-M"
    echo ""
    echo "Build artifacts:"
    ls -la *.gbc *.map *.sym 2>/dev/null || true
else
    echo "✗ Build failed - ROM file not created"
    exit 1
fi

echo ""
echo "=== Build Summary ==="
echo "Source files: $(find . -name '*.c' | wc -l) C files"
echo "Header files: $(find . -name '*.h' | wc -l) header files"
echo "Total lines: $(find . -name '*.c' -o -name '*.h' | xargs wc -l | tail -1)"
echo ""
echo "Happy gaming! 🎮"
