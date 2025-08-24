#!/usr/bin/env python3
"""
EXTREME Pokemon ROM Modifier - Go completely wild with modifications!
This creates the most dramatic changes possible while maintaining Delta compatibility
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
        ' ': 0x7F, '@': 0x50, '-': 0xE3, '.': 0xE8, ',': 0xE4, '!': 0xE6, '?': 0xE7
    }
    
    result = bytearray()
    for char in text:
        if char in charmap:
            result.append(charmap[char])
        else:
            result.append(0x7F)  # space for unknown chars
    
    return bytes(result)

def create_extreme_pokemon_rom():
    """Create the most extreme Pokemon ROM modifications possible!"""
    
    print("💥 EXTREME POKEMON ROM MODIFIER")
    print("===============================")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    print("🎯 Preparing for MAXIMUM CHAOS!")
    print("")
    
    input_file = "/mnt/c/Users/b_pla/Desktop/pokemon_yellow_WORKING.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_EXTREME_CHAOS.gbc"
    
    # EXTREME modifications - going completely wild!
    extreme_mods = [
        # === MAIN MENU CHAOS ===
        ("NEW GAME", "CHAOS!!!"),     # 8 chars - dramatic!
        ("CONTINUE", "MAYHEM  "),     # 8 chars - continue the chaos
        ("OPTION", "INSANE"),         # 6 chars - options are insane
        
        # === POKEMON NAME TRANSFORMATIONS ===
        ("PIKACHU", "ZAPSTER"),       # 7 chars - electric chaos
        ("CHARMANDER", "FLAMEBEAST"),  # 10 chars - wait, this won't work...
        ("SQUIRTLE", "AQUADOOM"),     # 8 chars - water destruction  
        ("BULBASAUR", "LEAFSTORM"),   # 9 chars - plant power
        ("RATTATA", "BITERAT"),       # 7 chars - aggressive rodent
        ("PIDGEY", "BIRDIE"),         # 6 chars - simple bird
        ("CATERPIE", "WORMZOID"),     # 8 chars - alien worm
        ("WEEDLE", "STINGER"),        # 6 chars - dangerous bug
        ("SPEAROW", "STABBER"),       # 7 chars - aggressive bird
        
        # === BATTLE TEXT MAYHEM ===
        ("FIGHT", "CRUSH!"),          # 5 chars - aggressive combat
        ("POKEMON", "MONSTER"),       # 7 chars - more dramatic
        ("ATTACK", "STRIKE"),         # 6 chars - more violent
        ("DEFEND", "SHIELD"),         # 6 chars - protective
        ("ITEM", "GEAR"),             # 4 chars - equipment
        ("RUN", "FLEE"),              # 3 chars - escape
        
        # === LOCATION TRANSFORMATIONS ===
        ("PALLET", "CHAOS "),         # 6 chars - hometown chaos
        ("VIRIDIAN", "DOOMCITY"),     # 8 chars - city of doom
        ("PEWTER", "ROCKON"),         # 6 chars - rock city
        ("CERULEAN", "BLUEHELL"),     # 8 chars - water hell
        ("VERMILION", "THUNDERBAY"),  # 9 chars - electric bay
        ("LAVENDER", "GHOSTOWN"),     # 8 chars - spooky town
        ("CELADON", "MEGAMART"),      # 7 chars - shopping chaos
        ("FUCHSIA", "NINJALAND"),     # 8 chars - ninja territory
        ("SAFFRON", "PSYCHOVILLE"),   # 10 chars - won't work, too long
        ("CINNABAR", "VOLCANOPEAK"),  # 10 chars - won't work either
        
        # === TRAINER TYPES ===
        ("YOUNGSTER", "KIDWARRIOR"),  # 9 chars - young fighter
        ("BUG CATCHER", "INSECTHUNTER"), # 11 chars - won't work
        ("LASS", "GIRL"),             # 4 chars - simple
        ("SAILOR", "PIRATE"),         # 6 chars - sea criminal
        ("HIKER", "WALKER"),          # 5 chars - mountain person
        ("BIKER", "RIDER"),           # 5 chars - motorcycle person
        ("BURGLAR", "THIEF  "),       # 7 chars - criminal
        ("ENGINEER", "MECHANIC"),     # 8 chars - tech person
        ("FISHERMAN", "ANGLER   "),   # 9 chars - fishing person
        
        # === BATTLE MOVES ===
        ("TACKLE", "SMASH "),         # 6 chars - aggressive move
        ("SCRATCH", "CLAW   "),       # 7 chars - animal attack
        ("GROWL", "ROAR "),           # 5 chars - intimidation
        ("LEER", "GLARE"),            # 4 chars - scary look
        ("BITE", "CHOMP"),            # 4 chars - eating attack
        ("SLAM", "BASH"),             # 4 chars - impact move
        
        # === ITEMS AND OBJECTS ===
        ("POTION", "HEALTH"),         # 6 chars - healing item
        ("ANTIDOTE", "CUREALL "),     # 8 chars - medicine
        ("POKEBALL", "CAPTUREBALL"),  # 8 chars - wait, too long!
        ("GREAT", "SUPER"),           # 5 chars - better quality
        ("ULTRA", "MEGA "),           # 5 chars - best quality
        
        # === STATUS AND SYSTEM ===
        ("LEVEL", "POWER"),           # 5 chars - strength indicator
        ("HEALTH", "ENERGY"),         # 6 chars - life force
        ("SPEED", "SWIFT"),           # 5 chars - quickness
        ("SPECIAL", "MAGICAL"),       # 7 chars - mystical power
        
        # === WILD REPLACEMENTS ===
        ("YELLOW", "GOLDEN"),         # 6 chars - precious metal
        ("VERSION", "EDITION"),       # 7 chars - game variant
        ("ELECTRIC", "LIGHTNING"),    # 8 chars - more dramatic
        ("WATER", "HYDRO"),           # 5 chars - scientific
        ("FIRE", "BLAZE"),            # 4 chars - intense flame
        ("GRASS", "PLANT"),           # 5 chars - vegetation
        ("NORMAL", "BASIC "),         # 6 chars - standard type
    ]
    
    # Read the working ROM
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return False
        
    with open(input_file, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    print("🔒 ROM header will NOT be modified (Delta compatibility)")
    print("")
    print("💥 APPLYING EXTREME MODIFICATIONS...")
    print("")
    
    total_changes = 0
    successful_mods = []
    
    for original_text, new_text in extreme_mods:
        # Ensure same length
        if len(original_text) != len(new_text):
            print(f"⚠️  Skipping '{original_text}' → '{new_text}' (length: {len(original_text)} vs {len(new_text)})")
            continue
            
        original_encoded = create_gb_text(original_text)
        new_encoded = create_gb_text(new_text)
        
        # Find and replace all occurrences
        offset = 0
        found_count = 0
        locations = []
        
        while True:
            pos = rom_data.find(original_encoded, offset)
            if pos == -1:
                break
                
            # Skip ROM header area for Delta compatibility
            if 0x100 <= pos <= 0x14F:
                offset = pos + len(original_encoded)
                continue
                
            locations.append(f"0x{pos:06X}")
            rom_data[pos:pos+len(original_encoded)] = new_encoded
            found_count += 1
            total_changes += 1
            offset = pos + len(original_encoded)
            
        if found_count > 0:
            print(f"💥 '{original_text}' → '{new_text}' ({found_count} locations)")
            successful_mods.append((original_text, new_text, found_count))
        else:
            print(f"❌ '{original_text}' not found")
    
    # Write the extreme ROM
    with open(output_file, 'wb') as f:
        f.write(rom_data)
    
    print("")
    print("🎉 EXTREME CHAOS ROM CREATED!")
    print("=============================")
    print(f"💾 File: pokemon_EXTREME_CHAOS.gbc")
    print(f"📊 Total modifications: {total_changes}")
    print("")
    print("💥 EXTREME CHANGES APPLIED:")
    for orig, new, count in successful_mods[:10]:  # Show first 10
        print(f"   🔥 '{orig}' → '{new}' ({count}x)")
    
    if len(successful_mods) > 10:
        print(f"   ... and {len(successful_mods) - 10} more changes!")
    
    print("")
    print("🎮 WHAT TO EXPECT:")
    print("   - Main menu shows 'CHAOS!!!' instead of 'NEW GAME'")
    print("   - Pokemon have wild new names like 'ZAPSTER'")
    print("   - Battle text is more aggressive: 'CRUSH!' instead of 'FIGHT'")
    print("   - Locations renamed: 'DOOMCITY' instead of 'VIRIDIAN'")
    print("   - Everything is MORE EXTREME!")
    print("")
    print("🚨 WARNING: This ROM is MAXIMUM CHAOS!")
    print("🎯 Load pokemon_EXTREME_CHAOS.gbc in Delta for wild fun!")
    
    return True

if __name__ == "__main__":
    create_extreme_pokemon_rom()
