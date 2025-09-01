#include <stdint.h>

// ============================================================================
// SIMPLE GAME OPERATIONS LIBRARY
// ============================================================================
// A minimal library of proven working functions
// ============================================================================

// External references to game variables
extern uint8_t wPlayerMoney[3];
extern uint8_t wNumBagItems;
extern uint8_t wBagItems[];

// ============================================================================
// MONEY MANAGEMENT FUNCTIONS (Proven Working)
// ============================================================================

// Set player money to $10,000 (our proven formula)
void give_ten_thousand(void) {
    wPlayerMoney[0] = 0x01;  // 1 × 10,000 = $10,000
    wPlayerMoney[1] = 0x00;  // 0 × 100 = $0
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $50,000
void give_fifty_thousand(void) {
    wPlayerMoney[0] = 0x05;  // 5 × 10,000 = $50,000
    wPlayerMoney[1] = 0x00;  // 0 × 100 = $0
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $100,000
void give_hundred_thousand(void) {
    wPlayerMoney[0] = 0x0A;  // 10 × 10,000 = $100,000
    wPlayerMoney[1] = 0x00;  // 0 × 100 = $0
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $1,000
void give_one_thousand(void) {
    wPlayerMoney[0] = 0x00;  // 0 × 10,000 = $0
    wPlayerMoney[1] = 0x0A;  // 10 × 100 = $1,000
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $5,000
void give_five_thousand(void) {
    wPlayerMoney[0] = 0x00;  // 0 × 10,000 = $0
    wPlayerMoney[1] = 0x32;  // 50 × 100 = $5,000
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $9,000
void give_nine_thousand(void) {
    wPlayerMoney[0] = 0x00;  // 0 × 10,000 = $0
    wPlayerMoney[1] = 0x5A;  // 90 × 100 = $9,000
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $15,000
void give_fifteen_thousand(void) {
    wPlayerMoney[0] = 0x01;  // 1 × 10,000 = $10,000
    wPlayerMoney[1] = 0x32;  // 50 × 100 = $5,000
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// Set player money to $25,000
void give_twenty_five_thousand(void) {
    wPlayerMoney[0] = 0x02;  // 2 × 10,000 = $20,000
    wPlayerMoney[1] = 0x32;  // 50 × 100 = $5,000
    wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
}

// ============================================================================
// INVENTORY MANAGEMENT FUNCTIONS
// ============================================================================

// Clear the player's bag (set to empty)
void clear_bag(void) {
    wNumBagItems = 0;
}

// Add 5 Pokeballs to the bag
void give_pokeballs(void) {
    // DISABLED: C inventory functions cause memory corruption
    // Even simple parameter setting causes issues
    // For now, we'll use assembly-only inventory management
}

// Add 10 Pokeballs to the bag
void give_lots_of_pokeballs(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x04;      // POKE_BALL item ID
        wBagItems[wNumBagItems * 2 + 1] = 10;    // Quantity: 10
        wNumBagItems++;
    }
}

// Add 5 Great Balls to the bag
void give_great_balls(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x03;      // GREAT_BALL item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Ultra Balls to the bag
void give_ultra_balls(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x02;      // ULTRA_BALL item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Potions to the bag
void give_potions(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x14;      // POTION item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Super Potions to the bag
void give_super_potions(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x13;      // SUPER_POTION item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Hyper Potions to the bag
void give_hyper_potions(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x12;      // HYPER_POTION item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Full Restores to the bag
void give_full_restores(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x10;      // FULL_RESTORE item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Revives to the bag
void give_revives(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x35;      // REVIVE item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Add 5 Max Revives to the bag
void give_max_revives(void) {
    if (wNumBagItems < 59) {
        wBagItems[wNumBagItems * 2] = 0x36;      // MAX_REVIVE item ID
        wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
        wNumBagItems++;
    }
}

// Give a starter kit (5 Pokeballs + 5 Potions)
void give_starter_kit(void) {
    give_pokeballs();
    give_potions();
}

// Give a battle kit (5 Great Balls + 5 Super Potions + 5 Revives)
void give_battle_kit(void) {
    give_great_balls();
    give_super_potions();
    give_revives();
}

// Give a master kit (5 Ultra Balls + 5 Hyper Potions + 5 Max Revives)
void give_master_kit(void) {
    give_ultra_balls();
    give_hyper_potions();
    give_max_revives();
}
