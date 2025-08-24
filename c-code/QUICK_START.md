# Quick Start - Pokemon Yellow Legacy C Version

## One-Command Setup

```bash
cd c-code
./install_gbdk.sh && source ~/.bashrc && ./build.sh
```

## Step-by-Step (If Above Fails)

### 1. Install GBDK-2020
```bash
# Download latest GBDK-2020
wget https://github.com/gbdk-2020/gbdk-2020/releases/download/4.4.0/gbdk-linux64.tar.gz

# Extract
tar -xzf gbdk-linux64.tar.gz

# Install to system location
sudo mv gbdk /opt/gbdk

# Set environment variables
export GBDK_HOME=/opt/gbdk
export PATH=$GBDK_HOME/bin:$PATH

# Make permanent
echo 'export GBDK_HOME=/opt/gbdk' >> ~/.bashrc
echo 'export PATH=$GBDK_HOME/bin:$PATH' >> ~/.bashrc
```

### 2. Build Pokemon Yellow
```bash
cd c-code
make yellow
```

### 3. Test Your ROM
```bash
# Your ROM is ready!
ls -la pokeyellow.gbc

# Test in emulator (if installed)
# visualboyadvance pokeyellow.gbc
# or load in any Game Boy emulator
```

## Troubleshooting

**Error: "lcc: command not found"**
```bash
export GBDK_HOME=/opt/gbdk
export PATH=$GBDK_HOME/bin:$PATH
```

**Error: "404 Not Found"**
- The installer now uses the correct GBDK-2020 v4.4.0 URL
- Run `./install_gbdk.sh` again

**Error: "No such file or directory"**
```bash
# Ensure tools are present
ls -la tools/scan_includes
# If missing, copy from parent directory
cp -r ../tools/* tools/
```

**Error: "Permission denied"**
```bash
# Make scripts executable
chmod +x install_gbdk.sh build.sh
```

## Alternative: Use Package Manager

**Ubuntu/Debian:**
```bash
# Install from package manager (if available)
sudo apt update
sudo apt install gbdk-2020
```

**If package not available, use manual installation above**

## Expected Result

After successful build:
- ✅ `pokeyellow.gbc` - Playable Pokemon Yellow ROM
- ✅ `pokeyellow.map` - Memory layout
- ✅ `pokeyellow.sym` - Debug symbols

The ROM should be functionally identical to the original assembly version!


