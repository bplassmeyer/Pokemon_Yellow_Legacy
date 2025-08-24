#!/usr/bin/env python3
"""
Entry Point Patcher - Fix C ROM entry point to match working Pokemon Yellow ROM
This patches the Game Boy ROM header to use the exact same entry point as the working ROM
"""

def patch_entry_point(input_rom, output_rom):
    """Patch the ROM entry point to match the working Pokemon Yellow ROM"""
    
    print("🔧 Entry Point Patcher")
    print("======================")
    
    # Read the C ROM
    with open(input_rom, 'rb') as f:
        rom_data = bytearray(f.read())
    
    print(f"📖 Loaded ROM: {len(rom_data)} bytes")
    
    # Show current entry point
    current_entry = rom_data[0x100:0x104]
    print(f"🔍 Current entry point: {current_entry.hex()}")
    
    # The working Pokemon Yellow ROM uses: 00 c3 ab 01
    # 00 = NOP
    # c3 ab 01 = JP $01ab
    working_entry = bytes([0x00, 0xc3, 0xab, 0x01])
    
    # But we need to make sure there's valid code at 0x01ab
    # Let's check what's currently at our jump target (0x0157 from 18 55)
    our_jump_target = 0x100 + 2 + 0x55  # 0x0157
    print(f"🎯 Our current jump target (0x{our_jump_target:04x}): {rom_data[our_jump_target:our_jump_target+8].hex()}")
    
    # Let's put some simple initialization code at 0x01ab to match the working ROM
    init_code_addr = 0x01ab
    if init_code_addr < len(rom_data):
        # Simple initialization sequence that should work with Delta
        init_code = bytes([
            0xF3,        # DI (disable interrupts)
            0x31, 0xFF, 0xFF,  # LD SP, $FFFF (set stack pointer)
            0x3E, 0xE4,  # LD A, $E4 (palette data)
            0xE0, 0x47,  # LDH [$FF47], A (set background palette)
            0x3E, 0x91,  # LD A, $91 (LCD control)
            0xE0, 0x40,  # LDH [$FF40], A (turn on LCD)
            0xC3, 0x57, 0x01  # JP $0157 (jump to our actual code)
        ])
        
        # Make sure we don't overwrite too much
        if init_code_addr + len(init_code) < len(rom_data):
            rom_data[init_code_addr:init_code_addr + len(init_code)] = init_code
            print(f"✅ Placed initialization code at 0x{init_code_addr:04x}")
        
        # Now update the entry point to use the standard Game Boy format
        rom_data[0x100:0x104] = working_entry
        print(f"✅ Updated entry point to: {working_entry.hex()}")
        
        # Also ensure the Nintendo logo is correct (required for some emulators)
        nintendo_logo = bytes([
            0xCE, 0xED, 0x66, 0x66, 0xCC, 0x0D, 0x00, 0x0B, 0x03, 0x73, 0x00, 0x83, 0x00, 0x0C, 0x00, 0x0D,
            0x00, 0x08, 0x11, 0x1F, 0x88, 0x89, 0x00, 0x0E, 0xDC, 0xCC, 0x6E, 0xE6, 0xDD, 0xDD, 0xD9, 0x99,
            0xBB, 0xBB, 0x67, 0x63, 0x6E, 0x0E, 0xEC, 0xCC, 0xDD, 0xDC, 0x99, 0x9F, 0xBB, 0xB9, 0x33, 0x3E
        ])
        
        if len(nintendo_logo) == 48:  # Nintendo logo is 48 bytes at 0x104-0x133
            rom_data[0x104:0x104 + 48] = nintendo_logo
            print("✅ Updated Nintendo logo")
    
    # Write the patched ROM
    with open(output_rom, 'wb') as f:
        f.write(rom_data)
    
    print(f"💾 Patched ROM saved as: {output_rom}")
    print("")
    print("🎮 Changes made:")
    print(f"   - Entry point: {working_entry.hex()} (matches Pokemon Yellow)")
    print(f"   - Init code at: 0x{init_code_addr:04x}")
    print("   - Nintendo logo updated")
    print("")
    print("🎯 This ROM should now boot properly in Delta emulator!")

if __name__ == "__main__":
    input_file = "pokemon_c_game.gbc"
    output_file = "/mnt/c/Users/b_pla/Desktop/pokemon_c_fixed.gbc"
    
    try:
        patch_entry_point(input_file, output_file)
        print("✅ SUCCESS: Fixed Pokemon C ROM created!")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
