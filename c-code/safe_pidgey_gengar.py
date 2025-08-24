#!/usr/bin/env python3
"""
Safe Pidgey → Gengar Modifier
Only changes Route 1 Pidgey encounters to prevent crashes
"""

import os
from datetime import datetime

def modify_pidgey_to_gengar():
    """Change ONLY Route 1 Pidgey encounters to Gengar - very safe approach"""
    
    print("👻 SAFE PIDGEY → GENGAR MODIFIER")
    print("===============================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_yellow_WORKING.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_SAFE_PIDGEY_GENGAR.gbc"
    
    # Pokemon IDs from constants/pokemon_constants.asm
    GENGAR = 0x0E     # const GENGAR ; $0E
    PIDGEY = 0x24     # const PIDGEY ; $24
    RATTATA = 0xA5    # const RATTATA ; $A5
    SPEAROW = 0x05    # const SPEAROW ; $05
    
    print("🔍 Pokemon IDs:")
    print(f"   PIDGEY  = 0x{PIDGEY:02X}")
    print(f"   GENGAR  = 0x{GENGAR:02X}")
    print(f"   RATTATA = 0x{RATTATA:02X}")
    print(f"   SPEAROW = 0x{SPEAROW:02X}")
    print("")
    
    # Read the ROM
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return False
        
    with open(input_file, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("")
    
    # Look for the exact Route 1 encounter pattern
    # From Route1.asm, the pattern should be:
    # encounter_rate(25), then:
    # 3,PIDGEY  4,PIDGEY  2,RATTATA  3,RATTATA  2,PIDGEY  3,PIDGEY  5,PIDGEY  4,RATTATA  5,SPEAROW  6,SPEAROW
    
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
    
    print("🔍 Searching for exact Route 1 encounter pattern...")
    print(f"Pattern: {route1_pattern.hex()}")
    
    pos = rom_data.find(route1_pattern)
    if pos == -1:
        print("❌ Exact Route 1 pattern not found!")
        print("💡 The ROM structure might be different than expected.")
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
    print("🔧 Replacing ONLY Pidgey encounters with Gengar...")
    
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
    
    # Write the modified ROM
    with open(output_file, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print("👻 SAFE PIDGEY MODIFICATION COMPLETE!")
    print("====================================")
    print(f"💾 File: {os.path.basename(output_file)}")
    print(f"📊 Changes made: {changes} Pidgey → Gengar")
    print("")
    print("🎮 EXPECTED RESULT:")
    print("   - Route 1 grass: Pidgey encounters are now Gengar")
    print("   - Route 1 grass: Rattata and Spearow unchanged")  
    print("   - All other areas: Completely unchanged")
    print("   - Should be 100% stable - minimal modification!")
    print("")
    print("🎯 Test this ROM in Delta - it should NOT crash!")
    
    return True

if __name__ == "__main__":
    try:
        success = modify_pidgey_to_gengar()
        if success:
            print("✅ SUCCESS: Safe Pidgey→Gengar mod created!")
        else:
            print("❌ FAILED: Could not create modification")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
