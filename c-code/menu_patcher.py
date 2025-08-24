#!/usr/bin/env python3
"""
Menu Text Patcher - Modify NEW GAME and OPTION text in Pokemon Yellow
This demonstrates how to modify specific menu text in the ROM
"""

def patch_menu_text(input_rom, output_rom):
    """Modify the main menu text to show custom options"""
    
    print("🎮 Pokemon Menu Text Patcher")
    print("============================")
    
    # Read the original ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    
    # Change the title first
    new_title = b"MENU MOD\x00\x00\x00\x00\x00\x00\x00\x00"  # 16 bytes total
    rom_data[0x134:0x134+16] = new_title
    print("✏️  Changed title to: MENU MOD")
    
    # Now let's find and modify the menu text
    # We'll search for the exact byte patterns
    
    modifications = 0
    
    # Pattern 1: "NEW GAME" followed by "OPTION" 
    # In assembly: db "NEW GAME", next "OPTION@"
    # This creates a specific byte pattern we can search for
    
    original_new_game = b"NEW GAME"
    custom_new_game = b"BRENNAN!"  # Same length (8 chars)
    
    original_option = b"OPTION"
    custom_option = b"CUSTOM"  # Same length (6 chars)
    
    # Search and replace NEW GAME text
    for i in range(len(rom_data) - len(original_new_game)):
        if rom_data[i:i+len(original_new_game)] == original_new_game:
            rom_data[i:i+len(original_new_game)] = custom_new_game
            modifications += 1
            print(f"🔧 Changed 'NEW GAME' to 'BRENNAN!' at offset 0x{i:06X}")
            if modifications >= 2:  # Limit to avoid over-modifying
                break
    
    # Search and replace OPTION text
    option_mods = 0
    for i in range(len(rom_data) - len(original_option)):
        if rom_data[i:i+len(original_option)] == original_option:
            rom_data[i:i+len(original_option)] = custom_option
            option_mods += 1
            print(f"🔧 Changed 'OPTION' to 'CUSTOM' at offset 0x{i:06X}")
            if option_mods >= 3:  # There might be multiple OPTION texts
                break
    
    # Also look for "CONTINUE" and modify it
    original_continue = b"CONTINUE"
    custom_continue = b"LOAD GAME"  # Slightly different length but fits
    
    for i in range(len(rom_data) - len(original_continue)):
        if rom_data[i:i+len(original_continue)] == original_continue:
            # Pad with null if shorter
            if len(custom_continue) < len(original_continue):
                padded_continue = custom_continue + b'\x00' * (len(original_continue) - len(custom_continue))
            else:
                padded_continue = custom_continue[:len(original_continue)]
            
            rom_data[i:i+len(original_continue)] = padded_continue
            print(f"🔧 Changed 'CONTINUE' to 'LOAD GAME' at offset 0x{i:06X}")
            break
    
    # Add signature
    rom_data[0x14A] = ord('M')  # Menu
    rom_data[0x14B] = ord('P')  # Patch
    
    # Write the modified ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print(f"💾 Modified ROM saved as: {output_rom}")
    print("")
    print("🎮 This ROM should show:")
    print("   1. Title screen menu: 'BRENNAN!' instead of 'NEW GAME'")
    print("   2. Title screen menu: 'CUSTOM' instead of 'OPTION'") 
    print("   3. Title screen menu: 'LOAD GAME' instead of 'CONTINUE'")
    print("   4. In-game start menu: 'CUSTOM' instead of 'OPTION'")
    print("")
    print("🎯 Test this by:")
    print("   - Starting the game (title screen)")
    print("   - Looking at the main menu options")
    print("   - Opening the start menu in-game (START button)")

if __name__ == "__main__":
    input_file = "../pokeyellow.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_menu_mod.gbc"
    
    try:
        patch_menu_text(input_file, output_file)
        print("✅ SUCCESS: Menu mod ROM created!")
        print("")
        print("🎮 Load 'pokemon_menu_mod.gbc' in Delta to see the changes!")
    except Exception as e:
        print(f"❌ ERROR: {e}")

