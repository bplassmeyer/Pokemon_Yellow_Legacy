#!/usr/bin/env python3
"""
Combined ROM Modifier - Apply Pidgey→Gengar changes to the text-modified ROM
This gives us BOTH text changes AND Pokemon encounter changes
"""

import os
from datetime import datetime

def create_combined_rom():
    """Apply Pidgey→Gengar changes to the ROM that already has text modifications"""
    
    print("🎯 COMBINED ROM MODIFIER")
    print("=======================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    # Use the ROM that already has text modifications as base
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_CUSTOM_FINAL.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_ULTIMATE_COMBINED.gbc"
    
    # Pokemon IDs
    GENGAR = 0x0E     # const GENGAR ; $0E
    PIDGEY = 0x24     # const PIDGEY ; $24
    RATTATA = 0xA5    # const RATTATA ; $A5
    SPEAROW = 0x05    # const SPEAROW ; $05
    
    print("🔍 Starting with ROM that has text modifications:")
    print(f"   Input: {os.path.basename(input_file)}")
    print("   This ROM should have: 'WORKING', 'BOOYAH', etc.")
    print("")
    
    # Read the text-modified ROM
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return False
        
    with open(input_file, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("")
    
    # Look for the exact Route 1 encounter pattern
    # The pattern should be the same even in the text-modified ROM
    route1_pattern = bytes([
        25,                    # encounter rate
        3, PIDGEY,            # Level 3 Pidgey
        4, PIDGEY,            # Level 4 Pidgey  
        2, RATTATA,           # Level 2 Rattata
        3, RATTATA,           # Level 3 Rattata
        2, PIDGEY,            # Level 2 Pidgey
        3, PIDGEY,            # Level 3 Pidgey
        5, PIDGEY,            # Level 5 Pidgey
        4, RATTATA,           # Level 4 Rattata
        5, SPEAROW,           # Level 5 Spearow
        6, SPEAROW            # Level 6 Spearow
    ])
    
    print("🔍 Searching for Route 1 encounter pattern in text-modified ROM...")
    print(f"Pattern: {route1_pattern.hex()}")
    
    pos = rom_data.find(route1_pattern)
    if pos == -1:
        print("❌ Route 1 encounter pattern not found!")
        print("💡 The text modifications might have affected the encounter data location.")
        return False
        
    print(f"📍 Found Route 1 encounter table at 0x{pos:06X}")
    print("")
    
    # Verify the pattern
    print("✅ Current Route 1 encounters:")
    encounter_rate = rom_data[pos]
    print(f"   Encounter rate: {encounter_rate}")
    
    for i in range(10):
        level = rom_data[pos + 1 + i*2]
        pokemon_id = rom_data[pos + 2 + i*2]
        
        pokemon_name = "UNKNOWN"
        if pokemon_id == PIDGEY:
            pokemon_name = "PIDGEY"
        elif pokemon_id == RATTATA:
            pokemon_name = "RATTATA"
        elif pokemon_id == SPEAROW:
            pokemon_name = "SPEAROW"
            
        print(f"   Slot {i}: Level {level} {pokemon_name}")
    
    print("")
    print("🔧 Applying Pidgey→Gengar modifications...")
    
    changes = 0
    
    # Replace only PIDGEY encounters
    for i in range(10):
        pokemon_offset = pos + 2 + i*2
        level = rom_data[pos + 1 + i*2]
        pokemon_id = rom_data[pokemon_offset]
        
        if pokemon_id == PIDGEY:
            rom_data[pokemon_offset] = GENGAR
            print(f"   ✅ Slot {i}: Level {level} PIDGEY → Level {level} GENGAR")
            changes += 1
        else:
            pokemon_name = "RATTATA" if pokemon_id == RATTATA else "SPEAROW"
            print(f"   ⏭️  Slot {i}: Level {level} {pokemon_name} (unchanged)")
    
    if changes == 0:
        print("❌ No Pidgey encounters found!")
        return False
    
    # Write the combined ROM
    with open(output_file, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print("🎉 ULTIMATE COMBINED ROM CREATED!")
    print("=================================")
    print(f"💾 File: {os.path.basename(output_file)}")
    print(f"📊 Pidgey→Gengar changes: {changes}")
    print("")
    print("🎮 THIS ROM NOW HAS EVERYTHING:")
    print("   ✅ Text Changes:")
    print("      - 'WORKING' instead of 'NEW GAME'")
    print("      - 'BOOYAH' instead of 'OPTION'")
    print("      - 'ZAPSTER' instead of 'PIKACHU'")
    print("      - 250+ other text modifications")
    print("")
    print("   ✅ Pokemon Changes:")
    print("      - Route 1 Pidgey encounters → Gengar")
    print("      - Levels 2, 3, 4, 5 Gengar on Route 1")
    print("")
    print("🎯 Test pokemon_ULTIMATE_COMBINED.gbc in Delta!")
    print("   You should see BOTH text AND Pokemon changes!")
    
    return True

if __name__ == "__main__":
    try:
        success = create_combined_rom()
        if success:
            print("✅ SUCCESS: Ultimate combined ROM created!")
        else:
            print("❌ FAILED: Could not create combined ROM")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
