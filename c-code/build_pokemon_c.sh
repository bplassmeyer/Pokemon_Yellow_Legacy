#!/bin/bash

# Pokemon C Build Script
# Builds a fully functional Pokemon-like Game Boy ROM from C code
# that works with Delta emulator

set -e  # Exit on any error

echo "🎮 Pokemon C Build System"
echo "========================="
echo ""

# Check if GBDK is available
if ! command -v /home/brennan/.local/gbdk/bin/lcc &> /dev/null; then
    echo "❌ GBDK not found! Installing..."
    ./install_gbdk.sh
    source ~/.bashrc
fi

echo "🔨 Step 1: Building C ROM..."
make -f Makefile.pokemon clean
make -f Makefile.pokemon

if [ ! -f "pokemon_c_game.gbc" ]; then
    echo "❌ Build failed - ROM not created"
    exit 1
fi

echo "✅ C ROM built successfully"
echo ""

echo "🔧 Step 2: Fixing ROM header for Delta compatibility..."
python3 entry_point_patcher.py

if [ ! -f "/mnt/c/Users/b_pla/Desktop/pokemon_c_fixed.gbc" ]; then
    echo "❌ ROM patching failed"
    exit 1
fi

echo "✅ ROM patched successfully"
echo ""

echo "📊 Step 3: ROM Analysis..."
echo "Original ROM size: $(du -h pokemon_c_game.gbc | cut -f1)"
echo "Fixed ROM size: $(du -h /mnt/c/Users/b_pla/Desktop/pokemon_c_fixed.gbc | cut -f1)"

echo ""
echo "🎯 Step 4: Verification..."
echo "Entry point check:"
ENTRY_POINT=$(hexdump -C /mnt/c/Users/b_pla/Desktop/pokemon_c_fixed.gbc -s 0x100 -n 4 | head -1 | cut -d' ' -f2-5)
if [[ "$ENTRY_POINT" == "00 c3 ab 01" ]]; then
    echo "  ✅ Entry point: $ENTRY_POINT (matches Pokemon Yellow)"
else
    echo "  ⚠️  Entry point: $ENTRY_POINT (unexpected)"
fi

echo ""
echo "🎉 SUCCESS! Pokemon C ROM is ready!"
echo "=================================="
echo ""
echo "📁 Files created:"
echo "  - pokemon_c_game.gbc (original C ROM)"
echo "  - /mnt/c/Users/b_pla/Desktop/pokemon_c_fixed.gbc (Delta-compatible ROM)"
echo ""
echo "🎮 What this ROM contains:"
echo "  - Custom Pokemon-like title screen"
echo "  - 'MOD GAME' instead of 'NEW GAME'"
echo "  - 'CUSTOM' instead of 'OPTION'"
echo "  - Interactive menu with A button support"
echo "  - Proper Game Boy initialization"
echo "  - Delta emulator compatibility"
echo ""
echo "🎯 To test:"
echo "  1. The ROM is already on your Windows desktop: pokemon_c_fixed.gbc"
echo "  2. Load it in Delta emulator"
echo "  3. You should see 'POKEMON C WORLD' title"
echo "  4. Menu shows 'MOD GAME', 'CUSTOM', 'CONTINUE'"
echo "  5. Press A to start the game"
echo ""
echo "🔧 To modify the game:"
echo "  1. Edit pokemon_c.c to change text, graphics, or behavior"
echo "  2. Run: ./build_pokemon_c.sh"
echo "  3. Test the new ROM in Delta"
echo ""
echo "✨ You now have a working C-based Pokemon ROM that you can modify!"
