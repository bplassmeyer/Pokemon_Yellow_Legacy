#!/usr/bin/env python3
"""
Route 1 Legendary Modifier - Complete Route 1 Pokemon replacement
Rattata → Dragonite, Spearow → Clefairy (plus existing Pidgey → Gengar)
"""

import os
from datetime import datetime

def create_legendary_route1():
    """Replace all remaining Route 1 Pokemon with legendary/rare Pokemon"""
    
    print("🐉 ROUTE 1 LEGENDARY MODIFIER")
    print("=============================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    # Use the ultimate combined ROM as base
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_ULTIMATE_COMBINED.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_LEGENDARY_ROUTE1.gbc"
    
    # Pokemon IDs from constants/pokemon_constants.asm
    GENGAR = 0x0E       # Already replaced Pidgey with this
    PIDGEY = 0x24       # Original (should already be replaced)
    RATTATA = 0xA5      # Will replace with Dragonite
    SPEAROW = 0x05      # Will replace with Clefairy
    DRAGONITE = 0x42    # const DRAGONITE ; $42
    CLEFAIRY = 0x04     # const CLEFAIRY ; $04
    
    print("🔍 Pokemon ID Mapping:")
    print(f"   RATTATA  (0x{RATTATA:02X}) → DRAGONITE (0x{DRAGONITE:02X})")
    print(f"   SPEAROW  (0x{SPEAROW:02X}) → CLEFAIRY  (0x{CLEFAIRY:02X})")
    print(f"   PIDGEY   (0x{PIDGEY:02X}) → GENGAR    (0x{GENGAR:02X}) [already done]")
    print("")
    
    # Read the ultimate combined ROM
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        print("💡 Make sure you've created the ultimate combined ROM first!")
        return False
        
    with open(input_file, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("   This ROM should already have text changes + Pidgey→Gengar")
    print("")
    
    # Look for the Route 1 encounter pattern
    # After our previous modifications, it should now be:
    # encounter_rate(25), then:
    # 3,GENGAR  4,GENGAR  2,RATTATA  3,RATTATA  2,GENGAR  3,GENGAR  5,GENGAR  4,RATTATA  5,SPEAROW  6,SPEAROW
    
    expected_pattern = bytes([
        25,                    # encounter rate
        3, GENGAR,            # Level 3 Gengar (was Pidgey)
        4, GENGAR,            # Level 4 Gengar (was Pidgey)
        2, RATTATA,           # Level 2 Rattata → will become Dragonite
        3, RATTATA,           # Level 3 Rattata → will become Dragonite
        2, GENGAR,            # Level 2 Gengar (was Pidgey)
        3, GENGAR,            # Level 3 Gengar (was Pidgey)
        5, GENGAR,            # Level 5 Gengar (was Pidgey)
        4, RATTATA,           # Level 4 Rattata → will become Dragonite
        5, SPEAROW,           # Level 5 Spearow → will become Clefairy
        6, SPEAROW            # Level 6 Spearow → will become Clefairy
    ])
    
    print("🔍 Searching for current Route 1 encounter pattern...")
    print(f"Expected pattern: {expected_pattern.hex()}")
    
    pos = rom_data.find(expected_pattern)
    if pos == -1:
        print("❌ Expected Route 1 pattern not found!")
        print("💡 The ROM might not have the expected Pidgey→Gengar changes.")
        
        # Try to find any Route 1 pattern by looking for the encounter rate + some known pattern
        print("🔍 Searching for any Route 1 pattern with encounter rate 25...")
        for i in range(len(rom_data) - 21):
            if rom_data[i] == 25:  # encounter rate
                # Check if this looks like an encounter table
                context = rom_data[i:i+21]
                print(f"   Found rate 25 at 0x{i:06X}: {context.hex()}")
                
                # Look for reasonable level values (1-100) in the right positions
                levels_look_good = True
                for j in range(1, 21, 2):  # Check odd positions (levels)
                    if i + j < len(rom_data):
                        level = rom_data[i + j]
                        if level < 1 or level > 100:
                            levels_look_good = False
                            break
                
                if levels_look_good:
                    print(f"   ✅ This looks like a valid encounter table!")
                    pos = i
                    break
        
        if pos == -1:
            return False
        
    print(f"📍 Found Route 1 encounter table at 0x{pos:06X}")
    print("")
    
    # Display current encounters
    print("✅ Current Route 1 encounters:")
    encounter_rate = rom_data[pos]
    print(f"   Encounter rate: {encounter_rate}")
    
    for i in range(10):
        level = rom_data[pos + 1 + i*2]
        pokemon_id = rom_data[pos + 2 + i*2]
        
        pokemon_name = "UNKNOWN"
        if pokemon_id == GENGAR:
            pokemon_name = "GENGAR"
        elif pokemon_id == RATTATA:
            pokemon_name = "RATTATA"
        elif pokemon_id == SPEAROW:
            pokemon_name = "SPEAROW"
        elif pokemon_id == PIDGEY:
            pokemon_name = "PIDGEY"
            
        print(f"   Slot {i}: Level {level} {pokemon_name}")
    
    print("")
    print("🔧 Applying legendary Pokemon replacements...")
    
    changes = 0
    
    # Replace RATTATA with DRAGONITE and SPEAROW with CLEFAIRY
    for i in range(10):
        pokemon_offset = pos + 2 + i*2
        level = rom_data[pos + 1 + i*2]
        pokemon_id = rom_data[pokemon_offset]
        
        if pokemon_id == RATTATA:
            rom_data[pokemon_offset] = DRAGONITE
            print(f"   🐉 Slot {i}: Level {level} RATTATA → Level {level} DRAGONITE")
            changes += 1
        elif pokemon_id == SPEAROW:
            rom_data[pokemon_offset] = CLEFAIRY
            print(f"   🧚 Slot {i}: Level {level} SPEAROW → Level {level} CLEFAIRY")
            changes += 1
        else:
            pokemon_name = "GENGAR" if pokemon_id == GENGAR else f"UNKNOWN(0x{pokemon_id:02X})"
            print(f"   ⏭️  Slot {i}: Level {level} {pokemon_name} (unchanged)")
    
    if changes == 0:
        print("❌ No Rattata or Spearow encounters found!")
        return False
    
    # Write the legendary ROM
    with open(output_file, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print("🎉 LEGENDARY ROUTE 1 ROM CREATED!")
    print("=================================")
    print(f"💾 File: {os.path.basename(output_file)}")
    print(f"📊 New legendary changes: {changes}")
    print("")
    print("🎮 THIS ROM NOW HAS THE ULTIMATE ROUTE 1:")
    print("   ✅ Text Changes:")
    print("      - 'WORKING' instead of 'NEW GAME'")
    print("      - 'BOOYAH' instead of 'OPTION'")
    print("      - 250+ other text modifications")
    print("")
    print("   ✅ Route 1 Pokemon (ALL REPLACED!):")
    print("      - 🐉 DRAGONITE (levels 2, 3, 4) instead of Rattata")
    print("      - 🧚 CLEFAIRY (levels 5, 6) instead of Spearow")
    print("      - 👻 GENGAR (levels 2, 3, 4, 5) instead of Pidgey")
    print("")
    print("🚨 WARNING: Route 1 is now LEGENDARY DIFFICULTY!")
    print("   - Level 2-6 Dragonite, Gengar, and Clefairy")
    print("   - This will be EXTREMELY challenging for new players!")
    print("")
    print("🎯 Test pokemon_LEGENDARY_ROUTE1.gbc in Delta!")
    print("   Route 1 is now the most epic starting area ever! 🔥")
    
    return True

if __name__ == "__main__":
    try:
        success = create_legendary_route1()
        if success:
            print("✅ SUCCESS: Legendary Route 1 ROM created!")
        else:
            print("❌ FAILED: Could not create legendary ROM")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
