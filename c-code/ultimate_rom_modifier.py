#!/usr/bin/env python3
"""
Ultimate ROM Modifier - Create custom Pokemon ROMs that work in Delta
Based on the discovery that Delta accepts text modifications but rejects header changes
"""

import os
from datetime import datetime

def create_gb_text(text):
    """Convert ASCII text to Game Boy character encoding"""
    charmap = {
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
        if char in charmap:
            result.append(charmap[char])
        else:
            print(f"Warning: Character '{char}' not in charmap, using space")
            result.append(0x7F)  # space
    
    return bytes(result)

def modify_pokemon_rom(input_rom, output_rom, modifications):
    """
    Modify Pokemon ROM with custom text changes
    IMPORTANT: Does NOT modify ROM header to maintain Delta compatibility
    """
    
    print("🎮 Ultimate Pokemon ROM Modifier")
    print("================================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    # Read the working ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("🔒 ROM header will NOT be modified (Delta compatibility)")
    print("")
    
    total_changes = 0
    
    for original_text, new_text in modifications:
        # Ensure same length to avoid breaking game layout
        if len(original_text) != len(new_text):
            print(f"⚠️  Skipping '{original_text}' → '{new_text}' (length mismatch: {len(original_text)} vs {len(new_text)})")
            continue
            
        original_encoded = create_gb_text(original_text)
        new_encoded = create_gb_text(new_text)
        
        print(f"🔍 Looking for '{original_text}'...")
        
        # Find and replace all occurrences
        offset = 0
        found_count = 0
        locations = []
        
        while True:
            pos = rom_data.find(original_encoded, offset)
            if pos == -1:
                break
                
            # Skip ROM header area (0x100-0x14F) to maintain Delta compatibility
            if 0x100 <= pos <= 0x14F:
                print(f"   ⚠️  Found in ROM header at 0x{pos:06X}, skipping for Delta compatibility")
                offset = pos + len(original_encoded)
                continue
                
            locations.append(f"0x{pos:06X}")
            rom_data[pos:pos+len(original_encoded)] = new_encoded
            found_count += 1
            total_changes += 1
            offset = pos + len(original_encoded)
            
        if found_count > 0:
            print(f"   ✅ Replaced at: {', '.join(locations)}")
            print(f"   📝 '{original_text}' → '{new_text}' ({found_count} locations)")
        else:
            print(f"   ❌ '{original_text}' not found in ROM")
        print("")
    
    # Write the modified ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print(f"💾 Modified ROM saved as: {output_rom}")
    print(f"📊 Total changes made: {total_changes}")
    print("")
    print("✅ SUCCESS: ROM modified while preserving Delta compatibility!")
    print("🎯 This ROM should work in Delta emulator!")
    
    return total_changes

def create_custom_pokemon_rom():
    """Create a custom Pokemon ROM with various text modifications"""
    
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_yellow_WORKING.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_CUSTOM_FINAL.gbc"
    
    # Text modifications (must be same length!)
    modifications = [
        # Main menu modifications
        ("NEW GAME", "WORKING "),     # 8 chars each (note extra space)
        ("CONTINUE", "RESUME  "),     # 8 chars each (note extra spaces)
        ("OPTION", "BOOYAH"),         # 6 chars each
        
        # In-game text modifications  
        ("POKEMON", "POKE-C"),        # 7 chars each (but this might break things)
        ("YELLOW", "C-HACK"),         # 6 chars each
        
        # Battle text modifications
        ("FIGHT", "BRAWL"),           # 5 chars each
        ("ITEM", "TOOL"),             # 4 chars each
        ("RUN", "FLY"),               # 3 chars each
        
        # Additional fun modifications
        ("PROF.OAK", "PROF.C++"),     # 8 chars each
        ("PIKACHU", "HACKCHU"),       # 7 chars each
    ]
    
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        print("Make sure you have the working Pokemon ROM on your desktop.")
        return False
        
    try:
        changes = modify_pokemon_rom(input_file, output_file, modifications)
        
        if changes > 0:
            print("🎉 CUSTOM POKEMON ROM CREATED!")
            print("===============================")
            print("")
            print("🎮 Your custom ROM features:")
            print("   - 'WORKING' instead of 'NEW GAME'")
            print("   - 'RESUME' instead of 'CONTINUE'") 
            print("   - 'BOOYAH' instead of 'OPTION'")
            print("   - 'BRAWL' instead of 'FIGHT'")
            print("   - 'HACKCHU' instead of 'PIKACHU'")
            print("   - And more custom text!")
            print("")
            print("📁 File: pokemon_CUSTOM_FINAL.gbc")
            print("🎯 Load this in Delta emulator!")
            print("")
            print("🔧 To make more changes:")
            print("   1. Edit the 'modifications' list in this script")
            print("   2. Run the script again")
            print("   3. Test in Delta")
            
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    create_custom_pokemon_rom()
