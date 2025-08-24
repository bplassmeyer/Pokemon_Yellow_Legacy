# Pokemon C - Functional Game Boy ROM in C

This directory contains a **working C-based Pokemon Game Boy ROM** that is compatible with Delta emulator and can be easily modified.

## 🎮 What You Get

- **Functional ROM**: `pokemon_c_fixed.gbc` that boots properly in Delta
- **Custom Content**: Modified Pokemon-like game with your own text and behavior
- **Easy Modifications**: Change the C code to alter the game instantly
- **Proper Game Boy Structure**: Correct ROM header, Nintendo logo, and boot sequence

## 🚀 Quick Start

### Build the ROM:
```bash
./build_pokemon_c.sh
```

### Test in Delta:
1. The ROM is automatically copied to your Windows desktop as `pokemon_c_fixed.gbc`
2. Load it in Delta emulator
3. You'll see "POKEMON C WORLD" with modified menu options

## 🔧 Making Changes

### Example 1: Change the Title Text
Edit `pokemon_c.c` around line 65-75:
```c
// Change this:
set_bkg_tile_xy(6, 2, 0x50);  // P
set_bkg_tile_xy(7, 2, 0x4F);  // O
set_bkg_tile_xy(8, 2, 0x4B);  // K
// ... to display different text
```

### Example 2: Modify Menu Options
Edit `pokemon_c.c` around line 85-95:
```c
// Change "MOD GAME" to something else:
set_bkg_tile_xy(4, 8, 0x4D);  // M -> Change to different letter
set_bkg_tile_xy(5, 8, 0x4F);  // O -> Change to different letter
// etc...
```

### Example 3: Add New Screens
Add new functions like:
```c
void display_custom_screen(void) {
    // Your custom screen code here
}
```

### After Making Changes:
```bash
./build_pokemon_c.sh  # Rebuilds and copies to desktop
```

## 📁 File Structure

- `pokemon_c.c` - Main game code (modify this!)
- `Makefile.pokemon` - Build configuration
- `entry_point_patcher.py` - Fixes ROM header for Delta compatibility
- `build_pokemon_c.sh` - One-command build and deploy
- `pokemon_c_fixed.gbc` - Final ROM (on Windows desktop)

## 🎯 What Makes This Work

Unlike our previous attempts, this ROM:

1. **Correct Entry Point**: Uses `00 c3 ab 01` like Pokemon Yellow
2. **Proper Nintendo Logo**: Required 48-byte Nintendo logo in header
3. **Game Boy Initialization**: Proper LCD setup and palette configuration
4. **Custom Graphics**: Hand-coded tile data for text display
5. **Input Handling**: Joypad support for menu navigation

## 🔍 Technical Details

### ROM Header Structure:
- `0x0100-0x0103`: Entry point (NOP + JP $01ab)
- `0x0104-0x0133`: Nintendo logo (48 bytes)
- `0x0134-0x0143`: Game title "POKEMON C G"
- `0x0147`: Cartridge type (0x1b = MBC5+RAM+BATTERY)

### Memory Layout:
- `0x01ab`: Initialization code (sets up LCD, palette, stack)
- `0x0157`: Main C program entry point
- Font tiles loaded into VRAM for text display

## 🎉 Success Metrics

✅ **ROM boots properly in Delta emulator**  
✅ **Displays custom Pokemon-like content**  
✅ **Responds to controller input**  
✅ **Can be modified by editing C code**  
✅ **Automatic build and deploy process**  

## 🚀 Next Steps

You can now:
1. **Modify the game content** by editing `pokemon_c.c`
2. **Add new features** like more screens, sounds, or graphics
3. **Create your own Pokemon-like game** using this as a base
4. **Test changes instantly** by running `./build_pokemon_c.sh`

The C code approach is now **fully functional** and gives you complete control over the game content while maintaining compatibility with Delta emulator!
