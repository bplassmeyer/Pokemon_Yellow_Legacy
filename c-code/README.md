# Pokemon Yellow Legacy - C Version

This directory contains a C-language version of the Pokemon Yellow Legacy ROM, converted from the original Game Boy assembly language source code.

## Structure

The C version maintains the same directory structure as the original assembly version:

- `main.c` - Main entry point and ROM bank initialization
- `home.c` - Core system functions (joypad, LCD, etc.)
- `audio.c` - Sound and music system
- `text.c` - Text display and processing
- `maps.c` - Map loading and management
- `ram.c` - Memory management and save data
- `constants/` - Header files for all game constants
- `macros/` - C macros equivalent to assembly macros
- `gfx/` - Graphics-related C files
- `includes.h` - Main header file including all dependencies

## Building

### Prerequisites

This C version is designed to be compiled with GBDK-2020, a modern C compiler for Game Boy development.

1. Install GBDK-2020 from: https://github.com/gbdk-2020/gbdk-2020
2. Set the GBDK_HOME environment variable to your GBDK installation path
3. Ensure RGBDS tools are available for final ROM processing

### Compilation

```bash
# Build the main ROM
make yellow

# Build debug version
make yellow_debug DEBUG=1

# Clean build artifacts
make clean

# Get help
make help
```

### Output

The build process produces:
- `pokeyellow.gbc` - The main Pokemon Yellow ROM file
- `pokeyellow_debug.gbc` - Debug version with symbols

## Conversion Notes

### Assembly to C Translation

The conversion from Game Boy assembly to C follows these principles:

1. **Memory Model**: The Game Boy's memory map is emulated using a global `gb_state` structure
2. **Registers**: CPU registers are simulated in the `gb_registers_t` structure
3. **Hardware Access**: Memory-mapped I/O is handled through `MEM_READ`/`MEM_WRITE` macros
4. **Banking**: ROM/SRAM bank switching is simulated through macros
5. **Interrupts**: Interrupt handling is simplified for the C environment

### Key Differences

- **Performance**: The C version will be slower than native assembly
- **Size**: The compiled ROM will be larger due to C runtime overhead
- **Compatibility**: Some low-level timing dependencies may behave differently
- **Debugging**: C version provides better debugging capabilities with modern tools

### Data Conversion

- Assembly data sections are converted to C arrays and structures
- Text strings are converted from Game Boy character encoding
- Graphics data remains in original format but is accessed through C functions
- Music and sound data is processed through C-based audio functions

## Development Status

This is a work-in-progress conversion. Current status:

- ✅ Basic project structure
- ✅ Core system functions (partial)
- ✅ Memory management framework
- ✅ Build system (Makefile)
- ⏳ Complete data conversion
- ⏳ Engine function implementation
- ⏳ Graphics system integration
- ⏳ Audio system implementation
- ⏳ Testing and debugging

## Contributing

When adding new C code:

1. Follow the existing naming conventions
2. Use the provided macros for hardware access
3. Document any deviations from the original assembly behavior
4. Test with both debug and release builds

## License

This C version maintains the same license as the original Pokemon Yellow Legacy project.


