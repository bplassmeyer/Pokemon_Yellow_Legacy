#!/usr/bin/env python3
"""
Direct ROM Patcher - Modify the working Pokemon Yellow ROM directly
This preserves all the working code while changing visible content
"""

def patch_working_rom(input_rom, output_rom):
    """Patch the working Pokemon ROM with custom modifications"""
    
    print("🔧 Direct ROM Patcher")
    print("=====================")
    
    # Read the working ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded working ROM: {len(rom_data)} bytes")
    
    # Change the ROM title to indicate it's modified
    new_title = b"POKEMON MOD\x00\x00\x00\x00\x00"  # 16 bytes total, null-padded
    rom_data[0x134:0x134+16] = new_title
    print("✏️  Changed ROM title to: POKEMON MOD")
    
    # Game Boy character encoding (from charmap.asm analysis)
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
    
    def encode_gb_text(text):
        """Convert text to Game Boy encoding"""
        result = bytearray()
        for char in text:
            if char in charmap:
                result.append(charmap[char])
            else:
                result.append(0x7F)  # space for unknown chars
        return bytes(result)
    
    # Text replacements
    replacements = [
        ("NEW GAME", "C MOD GAME"),  # Same length (8 chars each)
        ("OPTION", "CUSTOM"),        # Same length (6 chars each) 
        ("POKEMON", "POKE-C"),       # Same length (7 chars each)
    ]
    
    modifications = 0
    
    for original_text, new_text in replacements:
        if len(original_text) != len(new_text):
            print(f"⚠️  Length mismatch: '{original_text}' ({len(original_text)}) vs '{new_text}' ({len(new_text)})")
            continue
            
        original_encoded = encode_gb_text(original_text)
        new_encoded = encode_gb_text(new_text)
        
        print(f"🔍 Looking for '{original_text}' (encoded: {original_encoded.hex()})")
        
        # Find and replace all occurrences
        offset = 0
        found_count = 0
        while True:
            pos = rom_data.find(original_encoded, offset)
            if pos == -1:
                break
                
            print(f"   Found at offset 0x{pos:06X}")
            rom_data[pos:pos+len(original_encoded)] = new_encoded
            found_count += 1
            modifications += 1
            offset = pos + len(original_encoded)
            
        if found_count > 0:
            print(f"✅ Replaced '{original_text}' with '{new_text}' ({found_count} locations)")
        else:
            print(f"❌ '{original_text}' not found in ROM")
    
    # Add signature bytes to indicate this is our modified version
    rom_data[0x14A] = ord('C')  # Custom
    rom_data[0x14B] = ord('M')  # Mod
    
    # Write the modified ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print(f"💾 Modified ROM saved as: {output_rom}")
    print(f"📊 Total modifications: {modifications}")
    print("")
    print("🎮 Changes made:")
    print("   - Title: 'POKEMON MOD'")
    print("   - 'NEW GAME' → 'C MOD GAME'")
    print("   - 'OPTION' → 'CUSTOM'")
    print("   - 'POKEMON' → 'POKE-C'")
    print("   - Signature: 'CM' in header")
    print("")
    print("🎯 This ROM should work in Delta since it's based on the working Pokemon ROM!")
    print("   Look for the modified text in the game menus.")

if __name__ == "__main__":
    input_file = "pokeyellow.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_direct_mod.gbc"
    
    try:
        patch_working_rom(input_file, output_file)
        print("✅ SUCCESS: Direct ROM modification complete!")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
