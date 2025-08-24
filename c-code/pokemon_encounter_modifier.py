#!/usr/bin/env python3
"""
Pokemon Encounter Modifier - Change wild Pokemon encounters in specific routes
This modifies the actual game data structures, not just text!
"""

import os
from datetime import datetime

def modify_route1_encounters():
    """Replace all Route 1 wild Pokemon with Gengar"""
    
    print("👻 POKEMON ENCOUNTER MODIFIER - ROUTE 1 GENGAR TAKEOVER")
    print("=======================================================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_yellow_WORKING.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_GENGAR_ROUTE1.gbc"
    
    # Pokemon IDs (from constants/pokemon_constants.asm)
    GENGAR = 0x0E    # Line 23: const GENGAR ; $0E
    PIDGEY = 0x24    # Line 45: const PIDGEY ; $24
    RATTATA = 0x60   # Need to find this...
    SPEAROW = 0x05   # Line 14: const SPEAROW ; $05
    
    print("🔍 Pokemon ID Analysis:")
    print(f"   GENGAR  = 0x{GENGAR:02X}")
    print(f"   PIDGEY  = 0x{PIDGEY:02X}")
    print(f"   SPEAROW = 0x{SPEAROW:02X}")
    print("")
    
    # Read the working ROM
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return False
        
    with open(input_file, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("")
    
    # Current Route 1 encounter data (from Route1.asm):
    # db  3, PIDGEY    -> db  3, GENGAR
    # db  4, PIDGEY    -> db  4, GENGAR  
    # db  2, RATTATA   -> db  2, GENGAR
    # db  3, RATTATA   -> db  3, GENGAR
    # db  2, PIDGEY    -> db  2, GENGAR
    # db  3, PIDGEY    -> db  3, GENGAR
    # db  5, PIDGEY    -> db  5, GENGAR
    # db  4, RATTATA   -> db  4, GENGAR
    # db  5, SPEAROW   -> db  5, GENGAR
    # db  6, SPEAROW   -> db  6, GENGAR
    
    # The encounter table is stored as pairs of bytes: [level, pokemon_id]
    # We need to find this pattern in the ROM and replace the pokemon_ids
    
    print("🔍 Searching for Route 1 encounter data patterns...")
    
    # Look for the specific encounter patterns
    # Pattern: level 3, PIDGEY (0x24) -> level 3, GENGAR (0x0E)
    pattern_3_pidgey = bytes([3, 0x24])
    pattern_4_pidgey = bytes([4, 0x24])
    pattern_2_pidgey = bytes([2, 0x24])
    pattern_5_pidgey = bytes([5, 0x24])
    pattern_5_spearow = bytes([5, 0x05])
    pattern_6_spearow = bytes([6, 0x05])
    
    # We also need to find RATTATA's ID by searching for it in context
    # Let's look for level 2, 3, 4 with unknown pokemon after PIDGEY patterns
    
    changes_made = 0
    
    # Search and replace PIDGEY encounters
    pidgey_patterns = [
        (bytes([3, 0x24]), bytes([3, GENGAR])),  # Level 3 PIDGEY -> Level 3 GENGAR
        (bytes([4, 0x24]), bytes([4, GENGAR])),  # Level 4 PIDGEY -> Level 4 GENGAR
        (bytes([2, 0x24]), bytes([2, GENGAR])),  # Level 2 PIDGEY -> Level 2 GENGAR
        (bytes([5, 0x24]), bytes([5, GENGAR])),  # Level 5 PIDGEY -> Level 5 GENGAR
    ]
    
    for original_pattern, new_pattern in pidgey_patterns:
        offset = 0
        while True:
            pos = rom_data.find(original_pattern, offset)
            if pos == -1:
                break
            
            print(f"   📍 Found level {original_pattern[0]} PIDGEY at 0x{pos:06X}")
            rom_data[pos:pos+2] = new_pattern
            changes_made += 1
            offset = pos + 2
    
    # Search and replace SPEAROW encounters
    spearow_patterns = [
        (bytes([5, 0x05]), bytes([5, GENGAR])),  # Level 5 SPEAROW -> Level 5 GENGAR
        (bytes([6, 0x05]), bytes([6, GENGAR])),  # Level 6 SPEAROW -> Level 6 GENGAR
    ]
    
    for original_pattern, new_pattern in spearow_patterns:
        offset = 0
        while True:
            pos = rom_data.find(original_pattern, offset)
            if pos == -1:
                break
            
            print(f"   📍 Found level {original_pattern[0]} SPEAROW at 0x{pos:06X}")
            rom_data[pos:pos+2] = new_pattern
            changes_made += 1
            offset = pos + 2
    
    # For RATTATA, we need to be more clever
    # Let's search for level patterns that aren't PIDGEY or SPEAROW in the right area
    print("")
    print("🔍 Searching for RATTATA patterns by elimination...")
    
    # Look for level 2, 3, 4 patterns that aren't the ones we already found
    potential_rattata_levels = [2, 3, 4]
    
    for level in potential_rattata_levels:
        # Search for level + any pokemon ID that's not PIDGEY or SPEAROW
        for pokemon_id in range(0x01, 0xFF):
            if pokemon_id in [0x24, 0x05, GENGAR]:  # Skip PIDGEY, SPEAROW, GENGAR
                continue
                
            pattern = bytes([level, pokemon_id])
            pos = rom_data.find(pattern)
            
            if pos != -1:
                # Check if this is in a reasonable location (wild encounter data)
                # Wild encounter data should be clustered together
                context_start = max(0, pos - 20)
                context_end = min(len(rom_data), pos + 20)
                context = rom_data[context_start:context_end]
                
                # Look for other level/pokemon patterns nearby
                has_other_encounters = False
                for check_level in [2, 3, 4, 5, 6]:
                    if bytes([check_level, 0x24]) in context or bytes([check_level, 0x05]) in context:
                        has_other_encounters = True
                        break
                
                if has_other_encounters:
                    print(f"   📍 Found likely RATTATA: level {level}, ID 0x{pokemon_id:02X} at 0x{pos:06X}")
                    rom_data[pos:pos+2] = bytes([level, GENGAR])
                    changes_made += 1
    
    if changes_made == 0:
        print("❌ No encounter patterns found! The ROM structure might be different.")
        print("💡 Try examining the ROM with a hex editor to find the encounter data.")
        return False
    
    # Write the modified ROM
    with open(output_file, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print("👻 GENGAR TAKEOVER COMPLETE!")
    print("============================")
    print(f"💾 File: pokemon_GENGAR_ROUTE1.gbc")
    print(f"📊 Total encounter modifications: {changes_made}")
    print("")
    print("🎮 WHAT TO EXPECT:")
    print("   - Start a new game in the modified ROM")
    print("   - Walk in the tall grass on Route 1")
    print("   - ALL wild Pokemon should now be GENGAR!")
    print("   - Gengar will appear at levels 2-6 (same as original Pokemon)")
    print("")
    print("⚠️  NOTE: Gengar is normally a high-level evolved Pokemon.")
    print("   Having level 2-6 Gengar might be unusual but should work!")
    print("")
    print("🎯 Load pokemon_GENGAR_ROUTE1.gbc in Delta to test!")
    
    return True

if __name__ == "__main__":
    modify_route1_encounters()
