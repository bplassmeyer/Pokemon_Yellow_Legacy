#include <stdint.h>

// Simple Money Management Functions
// These functions directly manipulate the wPlayerMoney array
// They generate clean assembly without complex SDCC operations

// External reference to the player's money (3 bytes in BCD format)
extern uint8_t wPlayerMoney[3];

// Test function: set money to exactly what the game normally sets for $3000
void test_normal_money(void) {
    wPlayerMoney[0] = 0x00;  // Low byte
    wPlayerMoney[1] = 0x30;  // Middle byte (what game normally sets)
    wPlayerMoney[2] = 0x00;  // High byte
}

// Give player starting money ($3000)
void give_starting_money(void) {
    wPlayerMoney[0] = 0x00;  // Low byte
    wPlayerMoney[1] = 0x30;  // Middle byte ($3000)
    wPlayerMoney[2] = 0x00;  // High byte
}

// Give player maximum money (999,999 in BCD)
void give_max_money(void) {
    wPlayerMoney[0] = 0x99;  // Low byte (99)
    wPlayerMoney[1] = 0x99;  // Middle byte (99)
    wPlayerMoney[2] = 0x99;  // High byte (99)
}

// Give player a lot of money (100,000 in BCD)
void give_lots_of_money(void) {
    wPlayerMoney[0] = 0x00;  // Low byte (00)
    wPlayerMoney[1] = 0x00;  // Middle byte (00)
    wPlayerMoney[2] = 0x10;  // High byte (10 = 100,000)
}

// Give player some money (10,000 - trying different format)
void give_some_money(void) {
    wPlayerMoney[0] = 0x00;  // Low byte
    wPlayerMoney[1] = 0x10;  // Middle byte (trying $10 = 16 in decimal)
    wPlayerMoney[2] = 0x00;  // High byte
}

// Give player a little money (1,000 in BCD)
void give_little_money(void) {
    wPlayerMoney[0] = 0x00;  // Low byte (00)
    wPlayerMoney[1] = 0x10;  // Middle byte (10 = 1,000)
    wPlayerMoney[2] = 0x00;  // High byte (00)
}

// Set money to $10,000 using valid BCD values only
void give_ten_thousand_bcd(void) {
    wPlayerMoney[0] = 0x10;  // Low byte (0x10 = 16 in decimal, 16 × 1000 = $16,000)
    wPlayerMoney[1] = 0x00;  // Middle byte (0x00 = 0 in decimal, 0 × 100 = $0)
    wPlayerMoney[2] = 0x00;  // High byte (0x00 = 0 in decimal, 0 × 1 = $0)
}

// Correctly set money to $10,000 using 0x01 (1 × 10,000 = $10,000)
void give_ten_thousand_final(void) {
    wPlayerMoney[0] = 0x01;  // Low byte (0x01 = 1 in decimal, 1 × 10,000 = $10,000)
    wPlayerMoney[1] = 0x00;  // Middle byte (0x00 = 0 in decimal, 0 × 100 = $0)
    wPlayerMoney[2] = 0x00;  // High byte (0x00 = 0 in decimal, 0 × 1 = $0)
}
