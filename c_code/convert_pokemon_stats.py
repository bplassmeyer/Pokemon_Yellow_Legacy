#!/usr/bin/env python3
"""
Convert Pokemon stats from SDCC assembly to RGBASM format.
This script reads the SDCC output and generates RGBASM-compatible assembly
that can replace the original Pokemon base stats files.
"""

import re
import sys
import os

def convert_pokemon_stats_to_rgbds(sdcc_file, output_dir):
    """
    Convert SDCC assembly output to RGBASM format for Pokemon stats.
    Generates individual files that can replace the original base stats files.
    """
    print(f"Converting {sdcc_file} to individual Pokemon files in {output_dir}...")
    
    # Read the SDCC assembly file
    try:
        with open(sdcc_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not find {sdcc_file}")
        return False
    
    # Parse the Pokemon stats data from SDCC output
    pokemon_data = {}
    
    # Define the Pokemon we're looking for
    pokemon_names = ['pikachu', 'pidgey', 'rattata']
    
    for pokemon in pokemon_names:
        pokemon_data[pokemon] = []
        in_stats_section = False
        
        for line in lines:
            line = line.strip()
            if line.startswith(f'_{pokemon}_stats:'):
                in_stats_section = True
                continue
            elif in_stats_section and line.startswith('_'):
                # We've hit the next label, stop copying stats
                in_stats_section = False
            elif in_stats_section and line:
                if line.startswith('.db #0x'):
                    match = re.match(r'\.db #0x([0-9a-fA-F]+)', line)
                    if match:
                        hex_val = int(match.group(1), 16)
                        pokemon_data[pokemon].append(hex_val)
        
        print(f"Found {len(pokemon_data[pokemon])} stats for {pokemon}: {pokemon_data[pokemon]}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate individual Pokemon files
    for pokemon in pokemon_names:
        if pokemon_data[pokemon]:
            # Get the Pokemon's data
            data = pokemon_data[pokemon]
            
            # Generate the file content in the exact format expected
            file_content = []
            
            # Pokedex ID
            file_content.append(f'\tdb DEX_{pokemon.upper()} ; pokedex id')
            file_content.append("")
            
            # Base stats
            file_content.append(f'\tdb  {data[1]:3d},  {data[2]:3d},  {data[3]:3d},  {data[4]:3d},  {data[5]:3d}')
            file_content.append(f'\t;   hp  atk  def  spd  spc')
            file_content.append("")
            
            # Types
            type1_name = get_type_name(data[6])
            type2_name = get_type_name(data[7])
            file_content.append(f'\tdb {type1_name}, {type2_name} ; type')
            
            # Catch rate and base exp
            file_content.append(f'\tdb {data[8]} ; catch rate')
            file_content.append(f'\tdb {data[9]} ; base exp')
            file_content.append("")
            
            # Graphics (keep original)
            file_content.append(f'\tINCBIN "gfx/pokemon/front/{pokemon}.pic", 0, 1 ; sprite dimensions')
            file_content.append(f'\tdw {pokemon.capitalize()}PicFront, {pokemon.capitalize()}PicBack')
            file_content.append("")
            
            # Moves (keep original for now)
            if pokemon == 'pikachu':
                file_content.append('\tdb THUNDERSHOCK, GROWL, NO_MOVE, NO_MOVE ; level 1 learnset')
            elif pokemon == 'pidgey':
                file_content.append('\tdb GUST, NO_MOVE, NO_MOVE, NO_MOVE ; level 1 learnset')
            elif pokemon == 'rattata':
                file_content.append('\tdb TACKLE, TAIL_WHIP, NO_MOVE, NO_MOVE ; level 1 learnset')
            
            # Growth rate
            growth_name = get_growth_name(data[10])
            file_content.append(f'\tdb {growth_name} ; growth rate')
            file_content.append("")
            
            # TM/HM learnset (keep original for now)
            if pokemon == 'pikachu':
                file_content.append('\t; tm/hm learnset')
                file_content.append('\ttmhm MEGA_PUNCH,   MEGA_KICK,    TOXIC,        BODY_SLAM,    TAKE_DOWN,    \\')
                file_content.append('\t     DOUBLE_EDGE,  PAY_DAY,      SUBMISSION,   SEISMIC_TOSS, RAGE,         \\')
                file_content.append('\t     THUNDERBOLT,  THUNDER,      MIMIC,        DOUBLE_TEAM,  REFLECT,      \\')
                file_content.append('\t     BIDE,         SWIFT,        SKULL_BASH,   REST,         THUNDER_WAVE, \\')
                file_content.append('\t     SUBSTITUTE,   CUT,    FLY,    SURF,       STRENGTH,     FLASH')
            elif pokemon == 'pidgey':
                file_content.append('\t; tm/hm learnset')
                file_content.append('\ttmhm RAZOR_WIND,    TOXIC,        TAKE_DOWN,    DOUBLE_EDGE,  \\')
                file_content.append('\t     RAGE,         MIMIC,        DOUBLE_TEAM,  REFLECT,      BIDE,         \\')
                file_content.append('\t     SWIFT,        SKY_ATTACK,   REST,         SUBSTITUTE,   FLY')
            elif pokemon == 'rattata':
                file_content.append('\t; tm/hm learnset')
                file_content.append('\ttmhm SWORDS_DANCE,\tTOXIC,        BODY_SLAM,    TAKE_DOWN,    DOUBLE_EDGE,  BUBBLEBEAM,   \\')
                file_content.append('\t     WATER_GUN,    BLIZZARD,     RAGE,         THUNDERBOLT,  THUNDER,      \\')
                file_content.append('\t     DIG,          MIMIC,        DOUBLE_TEAM,  BIDE,         SWIFT,        \\')
                file_content.append('\t     SKULL_BASH,   REST,         SUBSTITUTE')
            
            file_content.append('\t; end')
            file_content.append("")
            file_content.append('\tdb 0 ; padding')
            
            # Write the individual Pokemon file
            output_file = os.path.join(output_dir, f"{pokemon}.asm")
            try:
                with open(output_file, 'w') as f:
                    f.write('\n'.join(file_content))
                print(f"Generated {output_file}")
            except Exception as e:
                print(f"Error writing {output_file}: {e}")
                return False
    
    print(f"Successfully generated Pokemon files in {output_dir}")
    return True

def get_type_name(type_id):
    """Convert type ID to type name constant."""
    type_names = {
        0: "NORMAL",
        1: "FIGHTING", 
        2: "FLYING",
        3: "POISON",
        4: "GROUND",
        5: "ROCK",
        6: "BIRD",
        7: "BUG",
        8: "GHOST",
        20: "FIRE",
        21: "WATER",
        22: "GRASS",
        23: "ELECTRIC",
        24: "PSYCHIC",
        25: "ICE",
        26: "DRAGON"
    }
    return type_names.get(type_id, "NORMAL")

def get_growth_name(growth_id):
    """Convert growth rate ID to growth rate name constant."""
    growth_names = {
        0: "GROWTH_MEDIUM_FAST",
        1: "GROWTH_ERRATIC",
        2: "GROWTH_FLUCTUATING", 
        3: "GROWTH_MEDIUM_SLOW",
        4: "GROWTH_FAST",
        5: "GROWTH_SLOW"
    }
    return growth_names.get(growth_id, "GROWTH_MEDIUM_FAST")

def main():
    """Main function to run the conversion."""
    sdcc_file = "pokemon_stats.asm"
    output_dir = "../data/pokemon/base_stats"
    
    if len(sys.argv) > 1:
        sdcc_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    
    success = convert_pokemon_stats_to_rgbds(sdcc_file, output_dir)
    
    if success:
        print("Conversion completed successfully!")
        print(f"Output directory: {output_dir}")
    else:
        print("Conversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
