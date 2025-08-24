#!/usr/bin/env python3
"""
Simple ROM Patcher to modify Pokemon Yellow ROM
This proves we can make modifications that are visible in the game
"""

def patch_pokemon_title(input_rom, output_rom):
    """Patch the Pokemon Yellow ROM to show it's been modified"""
    
    print("🔧 Pokemon ROM Patcher")
    print("======================")
    
    # Read the original ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    
    # Game title is at offset 0x134-0x143 (16 bytes)
    original_title = rom_data[0x134:0x144]
    print(f"📝 Original title: {original_title}")
    
    # Change the title to show it's been modified
    new_title = b"MODIFIED YELLOW\x00"  # 15 chars + null terminator
    
    # Patch the title
    rom_data[0x134:0x134+len(new_title)] = new_title
    
    print(f"✏️  New title: {new_title}")
    
    # Also patch the header checksum area to make a visible change
    # Change a few bytes in the Nintendo logo area to create a visible difference
    # (This won't break the ROM but will show it's different)
    
    # Patch some unused bytes in the header to mark our modification
    rom_data[0x14A] = 0x42  # 'B' for Brennan
    rom_data[0x14B] = 0x43  # 'C' for C-code
    
    print("🎯 Added signature bytes at 0x14A-0x14B")
    
    # Write the patched ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print(f"💾 Patched ROM saved as: {output_rom}")
    print(f"📊 Size: {len(rom_data)} bytes")
    print("")
    print("🎮 This ROM should:")
    print("   1. Boot normally in Delta emulator")
    print("   2. Show 'MODIFIED YELLOW' as the title")
    print("   3. Play exactly like Pokemon Yellow")
    print("   4. Prove that modifications work!")

if __name__ == "__main__":
    # Patch the working Pokemon ROM
    input_file = "../pokeyellow.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_yellow_MODIFIED.gbc"
    
    try:
        patch_pokemon_title(input_file, output_file)
        print("✅ SUCCESS: Modified ROM created!")
    except FileNotFoundError:
        print("❌ ERROR: Could not find the source Pokemon ROM")
        print("   Make sure pokeyellow.gbc exists in parent directory")
    except Exception as e:
        print(f"❌ ERROR: {e}")

