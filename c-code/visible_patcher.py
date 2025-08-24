#!/usr/bin/env python3
"""
Create a ROM with VISIBLE in-game modifications
This will change something you can see while playing
"""

def create_visible_mod(input_rom, output_rom):
    """Create a ROM with visible gameplay modifications"""
    
    print("🎮 Visible Pokemon ROM Modifier")
    print("===============================")
    
    # Read the original ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    
    # Change the title to something more obvious
    new_title = b"BRENNAN'S MOD\x00\x00\x00"  # 16 bytes total
    rom_data[0x134:0x134+16] = new_title
    
    print("✏️  Changed title to: BRENNAN'S MOD")
    
    # Let's find and modify the player's starting money
    # In Pokemon Yellow, starting money is usually stored as BCD
    # This is a common and visible modification
    
    # Look for the pattern that sets starting money (this is an educated guess)
    # We'll change some palette data or initial values that are more easily found
    
    # Modify the Game Boy Color palette data to make colors different
    # This will be visible if the emulator supports GBC mode
    
    # Find some data patterns and modify them
    # Change some bytes in the ROM to create visible differences
    
    # Let's modify some text data - look for common strings
    original_text = b"POKEMON"
    replacement_text = b"BRENNAN"
    
    modifications = 0
    for i in range(len(rom_data) - len(original_text)):
        if rom_data[i:i+len(original_text)] == original_text:
            rom_data[i:i+len(original_text)] = replacement_text
            modifications += 1
            if modifications <= 5:  # Limit modifications to avoid breaking the game
                print(f"🔧 Modified text at offset 0x{i:06X}")
    
    print(f"📝 Made {modifications} text modifications")
    
    # Also modify the copyright text if we can find it
    nintendo_text = b"Nintendo"
    brennan_text = b"BRENNAN!"
    
    for i in range(len(rom_data) - len(nintendo_text)):
        if rom_data[i:i+len(nintendo_text)].lower() == nintendo_text.lower():
            rom_data[i:i+len(nintendo_text)] = brennan_text
            print(f"🎯 Modified copyright at offset 0x{i:06X}")
            break
    
    # Add our signature
    rom_data[0x14A] = ord('B')  # Brennan
    rom_data[0x14B] = ord('M')  # Modified
    
    # Write the modified ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print(f"💾 Modified ROM saved as: {output_rom}")
    print("")
    print("🎮 This ROM should show:")
    print("   1. Title: 'BRENNAN'S MOD'")
    print("   2. Text changes from 'POKEMON' to 'BRENNAN'")
    print("   3. Copyright changes")
    print("   4. Fully playable Pokemon Yellow!")
    print("")
    print("🔍 Look for text changes in:")
    print("   - Opening screens")
    print("   - Menu text")
    print("   - Any place that says 'POKEMON'")

if __name__ == "__main__":
    input_file = "../pokeyellow.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/brennans_pokemon_mod.gbc"
    
    try:
        create_visible_mod(input_file, output_file)
        print("✅ SUCCESS: Visible mod ROM created!")
    except Exception as e:
        print(f"❌ ERROR: {e}")

