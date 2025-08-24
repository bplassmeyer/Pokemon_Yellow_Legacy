#!/usr/bin/env python3
"""
Precise Gengar Modifier - ONLY change Route 1 Pidgey encounters
This is much more surgical to avoid crashes
"""

import os
from datetime import datetime

def find_route1_encounter_table(rom_data):
    """Find the exact Route 1 encounter table in the ROM"""
    
    # From Route1.asm, the encounter table should look like:
    # encounter_rate (25), then 10 pairs of [level, pokemon_id]:
    # db  3, PIDGEY    (3, 0x24)
    # db  4, PIDGEY    (4, 0x24)  
    # db  2, RATTATA   (2, 0x??)
    # db  3, RATTATA   (3, 0x??)
    # db  2, PIDGEY    (2, 0x24)
    # db  3, PIDGEY    (3, 0x24)
    # db  5, PIDGEY    (5, 0x24)
    # db  4, RATTATA   (4, 0x??)
    # db  5, SPEAROW   (5, 0x05)
    # db  6, SPEAROW   (6, 0x05)
    
    PIDGEY = 0x24
    SPEAROW = 0x05
    
    print("🔍 Searching for Route 1 encounter table pattern...")
    
    # Look for the specific pattern: encounter_rate followed by level/pokemon pairs
    # We know SPEAROW (0x05) appears at levels 5 and 6 at the end
    spearow_pattern = bytes([5, SPEAROW, 6, SPEAROW])  # Level 5,6 SPEAROW
    
    spearow_pos = rom_data.find(spearow_pattern)
    if spearow_pos == -1:
        print("❌ Could not find Route 1 SPEAROW pattern")
        return None
        
    print(f"📍 Found SPEAROW pattern at 0x{spearow_pos:06X}")
    
    # The encounter table should start 18 bytes before the SPEAROW pattern
    # (encounter_rate + 8 pairs of level/pokemon before SPEAROW)
    table_start = spearow_pos - 18
    
    if table_start < 0:
        print("❌ Table start would be before ROM beginning")
        return None
        
    print(f"📍 Route 1 encounter table likely starts at 0x{table_start:06X}")
    
    # Verify this looks like an encounter table
    encounter_rate = rom_data[table_start]
    print(f"📊 Encounter rate: {encounter_rate}")
    
    if encounter_rate != 25:
        print(f"⚠️  Expected encounter rate 25, got {encounter_rate}")
        print("   Continuing anyway...")
    
    return table_start

def modify_route1_pidgey_only(input_rom, output_rom):
    """Change ONLY Route 1 Pidgey encounters to Gengar"""
    
    print("👻 PRECISE ROUTE 1 PIDGEY → GENGAR MODIFIER")
    print("===========================================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    GENGAR = 0x0E
    PIDGEY = 0x24
    
    # Read the ROM
    if not os.path.exists(input_rom):
        print(f"❌ Error: {input_rom} not found!")
        return False
        
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("")
    
    # Find Route 1 encounter table
    table_start = find_route1_encounter_table(rom_data)
    if table_start is None:
        return False
        
    print("")
    print("🎯 Route 1 encounter table found!")
    print("Current encounters:")
    
    # Display current encounter table
    for i in range(10):  # 10 encounter slots
        offset = table_start + 1 + (i * 2)  # +1 to skip encounter rate
        level = rom_data[offset]
        pokemon_id = rom_data[offset + 1]
        
        pokemon_name = "UNKNOWN"
        if pokemon_id == PIDGEY:
            pokemon_name = "PIDGEY"
        elif pokemon_id == 0x05:
            pokemon_name = "SPEAROW"
        else:
            pokemon_name = f"RATTATA(?0x{pokemon_id:02X})"
            
        print(f"   Slot {i}: Level {level} {pokemon_name}")
    
    print("")
    print("🔧 Modifying ONLY Pidgey encounters...")
    
    changes_made = 0
    
    # Modify only PIDGEY encounters in the Route 1 table
    for i in range(10):  # 10 encounter slots
        offset = table_start + 1 + (i * 2)  # +1 to skip encounter rate
        level = rom_data[offset]
        pokemon_id = rom_data[offset + 1]
        
        if pokemon_id == PIDGEY:
            rom_data[offset + 1] = GENGAR  # Change pokemon ID to Gengar
            print(f"   ✅ Slot {i}: Level {level} PIDGEY → Level {level} GENGAR")
            changes_made += 1
        else:
            print(f"   ⏭️  Slot {i}: Level {level} {pokemon_name} (unchanged)")
    
    if changes_made == 0:
        print("❌ No Pidgey encounters found to modify!")
        return False
    
    # Write the modified ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print("👻 PRECISE GENGAR MODIFICATION COMPLETE!")
    print("=======================================")
    print(f"💾 File: {os.path.basename(output_rom)}")
    print(f"📊 Pidgey encounters changed: {changes_made}")
    print("")
    print("🎮 WHAT TO EXPECT:")
    print("   - Route 1: Pidgey encounters are now Gengar")
    print("   - Route 1: Rattata and Spearow unchanged")
    print("   - All other routes: Completely unchanged")
    print("   - Should NOT crash - very minimal changes!")
    print("")
    print("🎯 Test this ROM in Delta emulator!")
    
    return True

if __name__ == "__main__":
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_yellow_WORKING.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_SAFE_GENGAR.gbc"
    
    try:
        success = modify_route1_pidgey_only(input_file, output_file)
        if success:
            print("✅ SUCCESS: Safe Gengar mod created!")
        else:
            print("❌ FAILED: Could not create mod")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
