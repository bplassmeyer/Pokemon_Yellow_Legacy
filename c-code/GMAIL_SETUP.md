# Gmail App Password Setup Guide

## 🔐 Step 1: Enable 2-Factor Authentication

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **Security** in the left sidebar
3. Under **Signing in to Google**, click **2-Step Verification**
4. Follow the prompts to enable 2FA if not already enabled

## 🔑 Step 2: Generate App Password

1. Still in **Security** → **2-Step Verification**
2. Scroll down to **App passwords** (at the bottom)
3. Click **App passwords**
4. You may need to sign in again
5. Select **Mail** from the dropdown
6. Click **Generate**
7. **Copy the 16-character password** (looks like: `abcd efgh ijkl mnop`)

## 📧 Step 3: Use the Email Script

Run the email script:
```bash
python3 email_rom.py
```

When prompted:
- **Gmail address**: Your full Gmail address (e.g., `your.email@gmail.com`)
- **App Password**: The 16-character password from Step 2 (NOT your regular Gmail password)

## 🎯 What Gets Emailed

The script will automatically find and attach:
- `pokemon_c_fixed.gbc` - Your working C ROM
- `pokemon_c_game.gbc` - Original C ROM  
- `pokemon_new_game_mod.gbc` - Previous ROM mod

## 🔧 Troubleshooting

### "Authentication failed"
- Make sure you're using the **App Password**, not your regular Gmail password
- The App Password should be 16 characters with spaces (like `abcd efgh ijkl mnop`)
- Make sure 2-Factor Authentication is enabled on your Gmail account

### "File not found"
- Run `./build_pokemon_c.sh` first to generate the ROM files
- Check that files exist on your Windows desktop

### "Connection failed"  
- Check your internet connection
- Gmail SMTP might be temporarily unavailable

## 🚀 Quick Commands

```bash
# Build ROMs and email them in one command:
./build_pokemon_c.sh && python3 email_rom.py

# Just email existing ROMs:
python3 email_rom.py
```

## 🔒 Security Notes

- App Passwords are safer than using your main Gmail password
- The script doesn't store your credentials anywhere
- You can revoke App Passwords anytime in your Google Account settings
