#!/usr/bin/env python3
"""
ROM Email Sender - Automatically email ROM files to yourself via Gmail
Requires Gmail App Password for authentication
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import getpass
from datetime import datetime

class ROMEmailer:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = None
        self.app_password = None
        
    def setup_credentials(self):
        """Get Gmail credentials from user"""
        print("🔐 Gmail Setup")
        print("==============")
        print("")
        print("You'll need:")
        print("1. Your Gmail address")
        print("2. Gmail App Password (NOT your regular password)")
        print("")
        print("📝 If you don't have an App Password yet:")
        print("   1. Go to myaccount.google.com")
        print("   2. Security → 2-Step Verification → App passwords")
        print("   3. Generate password for 'Mail'")
        print("   4. Use that 16-character password below")
        print("")
        
        self.sender_email = input("Enter your Gmail address: ").strip()
        self.app_password = getpass.getpass("Enter your Gmail App Password (hidden): ").strip()
        
        if not self.sender_email or not self.app_password:
            raise ValueError("Email and password are required!")
            
    def create_email(self, recipient_email, rom_files):
        """Create email with ROM attachments"""
        msg = MIMEMultipart()
        
        # Email headers
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Pokemon C ROM Files - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        # Email body
        body = f"""
🎮 Pokemon C ROM Files
=====================

Hi! Your Pokemon C ROM files are attached.

Files included:
"""
        
        for rom_file in rom_files:
            if os.path.exists(rom_file):
                size_mb = os.path.getsize(rom_file) / 1024 / 1024
                body += f"• {os.path.basename(rom_file)} ({size_mb:.1f} MB)\n"
        
        body += f"""
📅 Generated: {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}
🔧 Built with: Pokemon C Build System
🎯 Compatible with: Delta emulator and other Game Boy emulators

To use:
1. Download the attachments
2. Load the .gbc file in your Game Boy emulator
3. Look for "POKEMON C WORLD" title screen
4. Menu shows "MOD GAME" instead of "NEW GAME"

Enjoy your custom Pokemon ROM! 🎉
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach ROM files
        for rom_file in rom_files:
            if os.path.exists(rom_file):
                print(f"📎 Attaching: {os.path.basename(rom_file)}")
                
                with open(rom_file, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(rom_file)}'
                )
                msg.attach(part)
            else:
                print(f"⚠️  File not found: {rom_file}")
        
        return msg
        
    def send_email(self, recipient_email, rom_files):
        """Send email with ROM attachments"""
        try:
            print("📧 Preparing email...")
            msg = self.create_email(recipient_email, rom_files)
            
            print("🔗 Connecting to Gmail...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Enable TLS encryption
            
            print("🔐 Authenticating...")
            server.login(self.sender_email, self.app_password)
            
            print("📤 Sending email...")
            text = msg.as_string()
            server.sendmail(self.sender_email, recipient_email, text)
            server.quit()
            
            print("✅ Email sent successfully!")
            print(f"📬 Sent to: {recipient_email}")
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed!")
            print("🔧 Check your Gmail App Password")
            print("💡 Make sure you're using an App Password, not your regular password")
            
        except Exception as e:
            print(f"❌ Error sending email: {e}")
            
def main():
    print("📧 Pokemon ROM Email Sender")
    print("============================")
    print("")
    
    # ROM files to send
    rom_files = [
        "/mnt/c/Users/b_pla/Desktop/pokemon_c_fixed.gbc",
        "pokemon_c_game.gbc",  # Original C ROM
        "/mnt/c/Users/b_pla/Desktop/pokemon_new_game_mod.gbc"  # Previous mod
    ]
    
    # Filter to only existing files
    existing_files = [f for f in rom_files if os.path.exists(f)]
    
    if not existing_files:
        print("❌ No ROM files found!")
        print("🔧 Make sure you've built the ROMs first:")
        print("   ./build_pokemon_c.sh")
        return
        
    print("📁 Found ROM files:")
    for rom_file in existing_files:
        size_mb = os.path.getsize(rom_file) / 1024 / 1024
        print(f"  • {os.path.basename(rom_file)} ({size_mb:.1f} MB)")
    print("")
    
    try:
        emailer = ROMEmailer()
        emailer.setup_credentials()
        
        # Default to sending to same email address
        recipient = input(f"Send to ({emailer.sender_email}): ").strip()
        if not recipient:
            recipient = emailer.sender_email
            
        print("")
        emailer.send_email(recipient, existing_files)
        
    except KeyboardInterrupt:
        print("\n❌ Cancelled by user")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
