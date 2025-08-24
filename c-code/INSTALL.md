# Installation Guide - Pokemon Yellow Legacy C Version

## Prerequisites

### GBDK-2020
The C version requires GBDK-2020 for compiling C code to Game Boy ROMs.

1. Download GBDK-2020 from: https://github.com/gbdk-2020/gbdk-2020/releases
2. Extract to a directory (e.g., `/opt/gbdk` or `C:\gbdk`)
3. Set environment variable: `export GBDK_HOME=/path/to/gbdk`

### RGBDS (for final ROM processing)
RGBDS is still needed for final ROM formatting and some graphics processing.

**Ubuntu/Debian:**
```bash
sudo apt install rgbds
```

**macOS:**
```bash
brew install rgbds
```

**Windows:**
Download from: https://github.com/gbdev/rgbds/releases

### Build Tools
Standard build tools are required:
- `make`
- `gcc` (for building tools)

## Building

### Quick Start
```bash
cd c-code
make yellow
```

### Build Options

**Standard build:**
```bash
make yellow                  # Build pokeyellow.gbc
```

**Debug build:**
```bash
make yellow_debug DEBUG=1   # Build with debug symbols
```

**Clean build:**
```bash
make clean                   # Remove all build artifacts
make tidy                    # Remove build artifacts but keep graphics
```

**Build tools:**
```bash
make tools                   # Build required conversion tools
```

### Environment Variables

- `GBDK_HOME` - Path to GBDK-2020 installation (required)
- `RGBDS` - Prefix for RGBDS tools (optional, if not in PATH)
- `DEBUG` - Set to 1 for debug builds

### Example Setup Script

**Linux/macOS:**
```bash
#!/bin/bash
export GBDK_HOME=/opt/gbdk
export PATH=$GBDK_HOME/bin:$PATH
cd c-code
make yellow
```

**Windows (batch file):**
```batch
@echo off
set GBDK_HOME=C:\gbdk
set PATH=%GBDK_HOME%\bin;%PATH%
cd c-code
make yellow
```

## Troubleshooting

### Common Issues

**"lcc: command not found"**
- Ensure GBDK_HOME is set correctly
- Check that `$GBDK_HOME/bin/lcc` exists

**"rgbfix: command not found"**
- Install RGBDS or add it to PATH
- Set RGBDS environment variable to tool prefix

**"No such file or directory" errors**
- Run `make tools` first to build required tools
- Check that all source files are present

**Large ROM size**
- C version will be larger than assembly version
- Use release build (without DEBUG=1) for smaller size

### Build System Details

The build process:
1. Compiles C source files to Game Boy objects using GBDK
2. Links objects into a .gb ROM file
3. Converts .gb to .gbc format using rgbfix
4. Processes graphics and audio data using original tools

### Performance Notes

The C version will have different performance characteristics:
- Slower execution due to C runtime overhead
- Larger ROM size due to compiler-generated code
- Different timing behavior that may affect some game mechanics

For maximum compatibility with original hardware, the assembly version is recommended for final releases.

## Development Setup

### IDE Configuration
For development with modern IDEs:

**VS Code:**
```json
{
    "C_Cpp.includePath": [
        "${workspaceFolder}/c-code",
        "${env:GBDK_HOME}/include"
    ],
    "C_Cpp.defines": [
        "__GBDK__",
        "__TARGET_gb"
    ]
}
```

### Debugging
Use GBDK's debugging features:
```bash
make yellow_debug DEBUG=1
# Use with emulator that supports symbol files
```

## Next Steps

After successful build:
1. Test the ROM in a Game Boy emulator
2. Compare behavior with original assembly version  
3. Report any differences or issues
4. Contribute improvements back to the project


