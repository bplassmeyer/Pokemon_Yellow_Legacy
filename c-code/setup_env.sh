#!/bin/bash
# Environment setup for Pokemon Yellow Legacy C Version

# GBDK was installed to ~/.local/gbdk
export GBDK_HOME="$HOME/.local/gbdk"
export PATH="$GBDK_HOME/bin:$PATH"

echo "=== Environment Setup Complete ==="
echo "GBDK_HOME: $GBDK_HOME"
echo "LCC compiler: $(which lcc)"
echo ""
echo "You can now build Pokemon Yellow with:"
echo "  make yellow"
echo "  # or"
echo "  ./build.sh"


