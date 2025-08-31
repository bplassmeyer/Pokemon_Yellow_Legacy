#!/usr/bin/env python3
"""
Convert SDCC assembly output for game options to RGBDS-compatible assembly.
This script takes the SDCC output and generates proper RGBDS assembly functions.
"""

import sys
import re
import os

def convert_game_options_to_rgbds(sdcc_file, output_file):
    """
    Convert SDCC assembly output to RGBDS assembly for game options.
    
    Args:
        sdcc_file: Path to the SDCC output file
        output_file: Path to the output RGBDS assembly file
    """
    
    print(f"Converting {sdcc_file} to {output_file}")
    
    # Read the SDCC output file
    try:
        with open(sdcc_file, 'r') as f:
            sdcc_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: SDCC file {sdcc_file} not found")
        return False
    
    # Parse the SDCC output to extract function data
    functions = {}
    constants = {}
    current_function = None
    current_data = []
    
    for line in sdcc_lines:
        line = line.strip()
        
        # Look for function labels
        if line.startswith('_set_fast_text_speed::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_fast_text_speed'
            current_data = []
        elif line.startswith('_set_medium_text_speed::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_medium_text_speed'
            current_data = []
        elif line.startswith('_set_slow_text_speed::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_slow_text_speed'
            current_data = []
        elif line.startswith('_set_battle_style_shift::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_battle_style_shift'
            current_data = []
        elif line.startswith('_set_battle_style_set::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_battle_style_set'
            current_data = []
        elif line.startswith('_enable_battle_animations::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'enable_battle_animations'
            current_data = []
        elif line.startswith('_disable_battle_animations::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'disable_battle_animations'
            current_data = []
        elif line.startswith('_set_dev_options::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_dev_options'
            current_data = []
        elif line.startswith('_set_test_options::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_test_options'
            current_data = []
        elif line.startswith('_set_text_speed_only::'):
            if current_function:
                functions[current_function] = current_data
            current_function = 'set_text_speed_only'
            current_data = []
        elif line.startswith('_game_options_'):
            # Parse constants
            const_name = line.replace('_game_options_', '').replace(':', '')
            current_data = []
        elif line.startswith('.db #') and current_function is None:
            # This is a constant value
            const_value = line.split('#')[1].split()[0]  # Extract hex value
            # Remove the '0x' prefix to get just the hex digits
            if const_value.startswith('0x'):
                const_value = const_value[2:]  # Remove '0x' prefix
            constants[const_name] = const_value
        elif line.startswith('ret') and current_function:
            # End of function
            functions[current_function] = current_data
            current_function = None
            current_data = []
        elif current_function and line and not line.startswith(';') and not line.startswith(';c_code'):
            # Collect function data (skip comments and C source references)
            if line and not line.startswith('.area'):
                current_data.append(line)
    
    # Don't forget the last function
    if current_function:
        functions[current_function] = current_data
    
    # Generate RGBDS assembly
    rgbds_lines = []
    
    # Header
    rgbds_lines.append('; Game Options Control Functions')
    rgbds_lines.append('; This file provides functions to control game options like text speed, battle style, and animations')
    rgbds_lines.append('; Generated from C code by convert_game_options.py')
    rgbds_lines.append('')
    rgbds_lines.append('SECTION "GameOptions", ROMX')
    rgbds_lines.append('')
    
    # Generate each function
    for func_name, func_data in functions.items():
        if not func_data:
            continue
            
        # Function name stays the same (preserve underscores)
        rgbds_lines.append(f'; Function to {get_function_description(func_name)}')
        rgbds_lines.append(f'{func_name}::')
        
        # Convert the function body
        for line in func_data:
            converted_line = convert_sdcc_line_to_rgbds(line)
            if converted_line:
                rgbds_lines.append(f'\t{converted_line}')
        
        rgbds_lines.append('\tret')
        rgbds_lines.append('')
    
    # Add constants if we found any
    if constants:
        rgbds_lines.append('; Export constants for assembly linking')
        for const_name, const_value in constants.items():
            rgbds_lines.append(f'{const_name}::')
            rgbds_lines.append(f'\tdb ${const_value.upper()}')
            rgbds_lines.append('')
    
    # Write the output file
    try:
        with open(output_file, 'w') as f:
            f.write('\n'.join(rgbds_lines))
        print(f"Successfully generated {output_file}")
        return True
    except Exception as e:
        print(f"Error writing output file: {e}")
        return False

def get_function_description(func_name):
    """Get a human-readable description of what a function does."""
    descriptions = {
        'set_fast_text_speed': 'set text speed to FAST',
        'set_medium_text_speed': 'set text speed to MEDIUM',
        'set_slow_text_speed': 'set text speed to SLOW',
        'set_battle_style_shift': 'set battle style to SHIFT',
        'set_battle_style_set': 'set battle style to SET',
        'enable_battle_animations': 'enable battle animations',
        'disable_battle_animations': 'disable battle animations',
        'set_dev_options': 'set all options to development settings',
        'set_test_options': 'set all options to testing settings',
        'set_text_speed_only': 'set text speed while preserving other options'
    }
    return descriptions.get(func_name, 'perform game option operation')

def convert_sdcc_line_to_rgbds(line):
    """Convert a single SDCC line to RGBDS format."""
    # Skip comments and empty lines
    if not line or line.startswith(';'):
        return None
    
    # Convert common SDCC patterns to RGBDS
    line = line.strip()
    
    # Convert memory references: ld hl, #_wOptions -> ld hl, wOptions
    if 'ld\thl, #_' in line:
        var_name = line.split('#_')[1]
        return f'ld hl, {var_name}'
    
    # Convert indirect addressing: ld a, (hl) -> ld a, [hl]
    if line == 'ld\ta, (hl)':
        return 'ld a, [hl]'
    
    # Convert indirect addressing: ld (hl), a -> ld [hl], a
    if line == 'ld\t(hl), a':
        return 'ld [hl], a'
    
    # Convert immediate value to memory: ld (hl), #0x01 -> ld [hl], $01
    if line.startswith('ld\t(hl), #'):
        hex_val = line.split('#')[1]
        if hex_val.startswith('0x'):
            hex_val = hex_val[2:]  # Remove '0x' prefix
        return f'ld [hl], ${hex_val.upper()}'
    
    # Convert hex values: #0xf8 -> $F8
    if '#0x' in line:
        hex_val = line.split('#0x')[1].split()[0]  # Extract hex value
        line = line.replace(f'#0x{hex_val}', f'${hex_val.upper()}')
    
    # Convert function calls
    if line.startswith('call _'):
        func_name = line.replace('call _', '')
        return f'call {func_name}'
    
    # Convert bitwise operations
    if line.startswith('and\t'):
        return line.replace('\t', ' ')
    
    if line.startswith('or\t'):
        return line.replace('\t', ' ')
    
    if line.startswith('res\t'):
        return line.replace('\t', ' ')
    
    # Convert other common patterns
    if line.startswith('ret'):
        return 'ret'
    
    if line.startswith('ld a, '):
        return line.replace('\t', ' ')
    
    if line.startswith('ld b, '):
        return line.replace('\t', ' ')
    
    if line.startswith('ld hl, '):
        return line.replace('\t', ' ')
    
    if line.startswith('ld de, '):
        return line.replace('\t', ' ')
    
    # If we can't convert it, return the original line with tabs converted to spaces
    return line.replace('\t', ' ')

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python3 convert_game_options.py <sdcc_file> <output_file>")
        print("Example: python3 convert_game_options.py game_options.s game_options_rgbds.asm")
        sys.exit(1)
    
    sdcc_file = sys.argv[1]
    output_file = sys.argv[2]
    
    success = convert_game_options_to_rgbds(sdcc_file, output_file)
    if success:
        print("Conversion completed successfully!")
    else:
        print("Conversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
