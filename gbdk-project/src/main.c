#include <gb/gb.h>
#include <gb/cgb.h>
#include <stdint.h>

// Game state variables
UINT8 player_x = 80;
UINT8 player_y = 72;

// Full 16x16 Abra sprite data split into 4 tiles (2x2)
// This is the actual Abra sprite data from the Pokemon Yellow ROM
// Split into 4 tiles of 32 bytes each for 4 sprites
UINT8 abra_tiles[] = {
    // Tile 0 (top-left) - 32 bytes
    0x00, 0x00, 0x03, 0x03, 0x3d, 0x3e, 0x3b, 0x24,
    0x2f, 0x30, 0x1f, 0x10, 0x2f, 0x3c, 0x2f, 0x32,
    0x00, 0x00, 0xe0, 0xe0, 0xde, 0x3e, 0xee, 0x12,
    0xfa, 0x06, 0xfc, 0x04, 0xfa, 0x1e, 0xfa, 0x26,
    
    // Tile 1 (top-right) - 32 bytes
    0x1f, 0x18, 0x3f, 0x26, 0x25, 0x3f, 0x19, 0x1f,
    0x74, 0x6f, 0x67, 0x5c, 0x33, 0x3f, 0x0c, 0x0c,
    0xfc, 0x0c, 0xfe, 0x32, 0xd2, 0xfe, 0x4c, 0xfc,
    0x97, 0xfb, 0xf3, 0x9d, 0xe6, 0xfe, 0x18, 0x18,
    
    // Tile 2 (bottom-left) - 32 bytes
    0x00, 0x00, 0x00, 0x00, 0x03, 0x03, 0x3d, 0x3e,
    0x3b, 0x24, 0x2f, 0x30, 0x1f, 0x10, 0x2f, 0x3c,
    0x00, 0x00, 0x00, 0x00, 0xe0, 0xe0, 0xde, 0x3e,
    0xee, 0x12, 0xfa, 0x06, 0xfc, 0x04, 0xfa, 0x1e,
    
    // Tile 3 (bottom-right) - 32 bytes
    0x2f, 0x32, 0x1f, 0x18, 0x3f, 0x26, 0x25, 0x3f,
    0x7c, 0x7f, 0x67, 0x5c, 0x33, 0x3f, 0x0c, 0x0c,
    0xfa, 0x26, 0xfc, 0x0c, 0xfe, 0x32, 0xd2, 0xfe,
    0x9f, 0xff, 0xf3, 0x9d, 0xe6, 0xfe, 0x18, 0x18
};

// Abra color palette - trying to match the PNG colors
// Looking at the PNG, Abra appears to have:
// - Light yellow/cream body
// - Darker brown details
// - Some darker shading
const UWORD abra_palette[] = {
    RGB(31, 31, 31),  // Index 0: White (transparent)
    RGB(31, 28, 20),  // Index 1: Light cream/yellow (main body)
    RGB(20, 15, 8),   // Index 2: Dark brown (details)
    RGB(15, 10, 5)    // Index 3: Darker brown (shading)
};

void main(void)
{
    // Now let's display Abra in a single 8x8 sprite!
    
    // Initialize the Game Boy Color
    DISPLAY_ON;
    SHOW_SPRITES;
    SHOW_BKG;
    
    // Wait for VBLANK
    wait_vbl_done();
    
    // Set the sprite palette for Abra
    set_sprite_palette(0, 1, abra_palette);
    
    // Wait another frame
    wait_vbl_done();
    
    // Load the full Abra sprite (4 tiles = 128 bytes)
    set_sprite_data(4, 4, abra_tiles);  // Use sprite slots 4-7 with 4 tiles
    
    // Set up the 4 sprites to form the 16x16 Abra
    set_sprite_tile(4, 4);  // Top-left
    set_sprite_tile(5, 5);  // Top-right  
    set_sprite_tile(6, 6);  // Bottom-left
    set_sprite_tile(7, 7);  // Bottom-right
    
    // Use palette 0 for all sprites
    set_sprite_prop(4, 0);
    set_sprite_prop(5, 0);
    set_sprite_prop(6, 0);
    set_sprite_prop(7, 0);
    
    // Wait a frame to ensure palette is applied
    wait_vbl_done();
    
    // Position the 4 sprites to form the 16x16 Abra
    move_sprite(4, player_x, player_y);      // Top-left
    move_sprite(5, player_x + 8, player_y); // Top-right
    move_sprite(6, player_x, player_y + 8); // Bottom-left
    move_sprite(7, player_x + 8, player_y + 8); // Bottom-right
    
    // Wait another frame to ensure everything is set up
    wait_vbl_done();
    
    // Main game loop
    while(1) {
        // Handle input
        UINT8 keys = joypad();
        
        if (keys & J_LEFT && player_x > 0) {
            player_x -= 2;
            move_sprite(4, player_x, player_y);
            move_sprite(5, player_x + 8, player_y);
            move_sprite(6, player_x, player_y + 8);
            move_sprite(7, player_x + 8, player_y + 8);
        }
        if (keys & J_RIGHT && player_x < 152) {
            player_x += 2;
            move_sprite(4, player_x, player_y);
            move_sprite(5, player_x + 8, player_y);
            move_sprite(6, player_x, player_y + 8);
            move_sprite(7, player_x + 8, player_y + 8);
        }
        if (keys & J_UP && player_y > 0) {
            player_y -= 2;
            move_sprite(4, player_x, player_y);
            move_sprite(5, player_x + 8, player_y);
            move_sprite(6, player_x, player_y + 8);
            move_sprite(7, player_x + 8, player_y + 8);
        }
        if (keys & J_DOWN && player_y < 136) {
            player_y += 2;
            move_sprite(4, player_x, player_y);
            move_sprite(5, player_x + 8, player_y);
            move_sprite(6, player_x, player_y + 8);
            move_sprite(7, player_x + 8, player_y + 8);
        }
        
        // Simple collision detection
        if (player_x < 0) player_x = 0;
        if (player_x > 152) player_x = 0;
        if (player_y < 0) player_y = 0;
        if (player_y > 136) player_y = 136;
        
        // Wait for VBLANK
        wait_vbl_done();
    }
}
