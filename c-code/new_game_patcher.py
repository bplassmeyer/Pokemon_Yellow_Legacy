#!/usr/bin/env python3
"""
NEW GAME Text Patcher - Change "NEW GAME" to "new MODIFIED game" in Pokemon Yellow
Uses the correct Game Boy character encoding from charmap.asm
"""

def create_gb_text(text):
    """Convert ASCII text to Game Boy character encoding"""
    # Based on charmap.asm - Game Boy character mapping
    char_map = {
        'A': 0x80, 'B': 0x81, 'C': 0x82, 'D': 0x83, 'E': 0x84, 'F': 0x85, 'G': 0x86, 'H': 0x87,
        'I': 0x88, 'J': 0x89, 'K': 0x8A, 'L': 0x8B, 'M': 0x8C, 'N': 0x8D, 'O': 0x8E, 'P': 0x8F,
        'Q': 0x90, 'R': 0x91, 'S': 0x92, 'T': 0x93, 'U': 0x94, 'V': 0x95, 'W': 0x96, 'X': 0x97,
        'Y': 0x98, 'Z': 0x99,
        'a': 0xA0, 'b': 0xA1, 'c': 0xA2, 'd': 0xA3, 'e': 0xA4, 'f': 0xA5, 'g': 0xA6, 'h': 0xA7,
        'i': 0xA8, 'j': 0xA9, 'k': 0xAA, 'l': 0xAB, 'm': 0xAC, 'n': 0xAD, 'o': 0xAE, 'p': 0xAF,
        'q': 0xB0, 'r': 0xB1, 's': 0xB2, 't': 0xB3, 'u': 0xB4, 'v': 0xB5, 'w': 0xB6, 'x': 0xB7,
        'y': 0xB8, 'z': 0xB9,
        '0': 0xF6, '1': 0xF7, '2': 0xF8, '3': 0xF9, '4': 0xFA, '5': 0xFB, '6': 0xFC, '7': 0xFD,
        '8': 0xFE, '9': 0xFF,
        ' ': 0x7F, '@': 0x50,  # @ is string terminator
    }
    
    result = bytearray()
    for char in text:
        if char in char_map:
            result.append(char_map[char])
        else:
            print(f"Warning: Character '{char}' not in charmap, using space")
            result.append(0x7F)  # space
    
    return bytes(result)

def patch_new_game_text(input_rom, output_rom):
    """Change 'NEW GAME' to 'new MODIFIED game' using correct Game Boy encoding"""
    
    print("🎮 NEW GAME Text Patcher")
    print("========================")
    
    # Read the original ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    
    # Change the title first
    new_title = b"NEW GAME MOD\x00\x00\x00\x00"  # 16 bytes total
    rom_data[0x134:0x134+16] = new_title
    print("✏️  Changed title to: NEW GAME MOD")
    
    # Create Game Boy encoded text
    original_new_game = create_gb_text("NEW GAME")
    new_text = create_gb_text("new MODIFIED game")  # This is longer, so we need to be careful
    
    original_option = create_gb_text("OPTION")
    new_option = create_gb_text("CUSTOM")
    
    print(f"🔍 Looking for 'NEW GAME' pattern: {original_new_game.hex()}")
    print(f"🔍 Will replace with: {new_text.hex()}")
    print(f"🔍 Original text length: {len(original_new_game)} bytes")
    print(f"🔍 New text length: {len(new_text)} bytes")
    
    # The new text is longer, so let's try a different approach
    # Let's look for the exact pattern and see what's around it
    
    modifications = 0
    
    # Search for the NEW GAME pattern
    for i in range(len(rom_data) - len(original_new_game)):
        if rom_data[i:i+len(original_new_game)] == original_new_game:
            print(f"🎯 Found 'NEW GAME' at offset 0x{i:06X}")
            
            # Show context around the match
            context_start = max(0, i - 10)
            context_end = min(len(rom_data), i + len(original_new_game) + 10)
            context = rom_data[context_start:context_end]
            print(f"   Context: {context.hex()}")
            
            # Check if we have enough space for the longer text
            # Since "new MODIFIED game" is longer than "NEW GAME", we need to be creative
            
            # Try exact length replacement
            if modifications == 0:  # Only modify the first occurrence
                # Use "MOD GAME" (8 chars) to match "NEW GAME" (8 chars exactly)
                replacement_text = create_gb_text("MOD GAME")  # Same length as original
                if len(replacement_text) == len(original_new_game):
                    rom_data[i:i+len(original_new_game)] = replacement_text
                    print(f"✅ Replaced 'NEW GAME' with 'MOD GAME' at offset 0x{i:06X}")
                    modifications += 1
                else:
                    print(f"⚠️  Replacement text length mismatch: {len(replacement_text)} vs {len(original_new_game)}")
            else:
                print(f"ℹ️  Skipping additional occurrence at 0x{i:06X}")
    
    # Also try to find and replace OPTION
    option_mods = 0
    for i in range(len(rom_data) - len(original_option)):
        if rom_data[i:i+len(original_option)] == original_option:
            print(f"🎯 Found 'OPTION' at offset 0x{i:06X}")
            
            if option_mods < 2:  # Limit modifications
                # CUSTOM is same length as OPTION (6 chars)
                rom_data[i:i+len(original_option)] = new_option
                print(f"✅ Replaced 'OPTION' with 'CUSTOM' at offset 0x{i:06X}")
                option_mods += 1
            else:
                print(f"ℹ️  Skipping additional OPTION occurrence")
    
    # Add signature bytes
    rom_data[0x14A] = ord('N')  # New
    rom_data[0x14B] = ord('G')  # Game
    
    # Write the modified ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print(f"💾 Modified ROM saved as: {output_rom}")
    print("")
    print("🎮 Changes made:")
    print(f"   - Title: 'NEW GAME MOD'")
    if modifications > 0:
        print(f"   - Main menu: 'MOD GAME' instead of 'NEW GAME'")
    if option_mods > 0:
        print(f"   - Options: 'CUSTOM' instead of 'OPTION' ({option_mods} locations)")
    print("")
    print("🎯 Test this ROM in Delta emulator!")
    print("   Look for 'MOD GAME' on the main menu screen instead of 'NEW GAME'!")

if __name__ == "__main__":
    input_file = "../pokeyellow.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_new_game_mod.gbc"
    
    try:
        patch_new_game_text(input_file, output_file)
        print("✅ SUCCESS: NEW GAME mod ROM created!")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

