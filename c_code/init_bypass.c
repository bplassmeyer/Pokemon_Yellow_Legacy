#include <stdint.h>

// Game constants
#define DIFFICULTY_NORMAL 0
#define DIFFICULTY_HARD 1
#define GENDER_BOY 0
#define GENDER_GIRL 1

// Default names (max 11 characters including null terminator)
#define DEFAULT_PLAYER_NAME "TESTER"
#define DEFAULT_RIVAL_NAME "DEBUG"

// Function to bypass all initialization menus
// This replaces the OakSpeech function call
void bypass_init_menus(void) {
    // Set difficulty to normal
    extern uint8_t wDifficulty;
    wDifficulty = DIFFICULTY_NORMAL;
    
    // Set gender to boy (0)
    extern uint8_t wPlayerGender;
    wPlayerGender = GENDER_BOY;
    
    // Set player name to default
    extern uint8_t wPlayerName[11];
    const char* player_name = DEFAULT_PLAYER_NAME;
    for (int i = 0; i < 11; i++) {
        if (i < 6) { // Length of "TESTER"
            wPlayerName[i] = player_name[i];
        } else {
            wPlayerName[i] = 0x50; // '@' terminator
        }
    }
    
    // Set rival name to default
    extern uint8_t wRivalName[11];
    const char* rival_name = DEFAULT_RIVAL_NAME;
    for (int i = 0; i < 11; i++) {
        if (i < 5) { // Length of "RIVAL"
            wRivalName[i] = rival_name[i];
        } else {
            wRivalName[i] = 0x50; // '@' terminator
        }
    }
    
    // Set other initialization variables
    extern uint8_t wOptionsInitialized;
    wOptionsInitialized = 1; // Skip options initialization
    
    // Set default options
    extern uint8_t wLetterPrintingDelayFlags;
    wLetterPrintingDelayFlags = 0x01; // Fast text
    
    extern uint8_t wOptions;
    wOptions = 0x00; // Medium text delay
    
    extern uint8_t wPrinterSettings;
    wPrinterSettings = 0x40; // Default printer settings
}

// Alternative function for girl gender
void bypass_init_menus_girl(void) {
    // Set difficulty to normal
    extern uint8_t wDifficulty;
    wDifficulty = DIFFICULTY_NORMAL;
    
    // Set gender to girl (1)
    extern uint8_t wPlayerGender;
    wPlayerGender = GENDER_GIRL;
    
    // Set player name to default girl name
    extern uint8_t wPlayerName[11];
    const char* player_name = "TESTER"; // Use same name for consistency
    for (int i = 0; i < 11; i++) {
        if (i < 6) { // Length of "TESTER"
            wPlayerName[i] = player_name[i];
        } else {
            wPlayerName[i] = 0x50; // '@' terminator
        }
    }
    
    // Set rival name to default
    extern uint8_t wRivalName[11];
    const char* rival_name = DEFAULT_RIVAL_NAME;
    for (int i = 0; i < 11; i++) {
        if (i < 5) { // Length of "RIVAL"
            wRivalName[i] = rival_name[i];
        } else {
            wRivalName[i] = 0x50; // '@' terminator
        }
    }
    
    // Set other initialization variables
    extern uint8_t wOptionsInitialized;
    wOptionsInitialized = 1; // Skip options initialization
    
    // Set default options
    extern uint8_t wLetterPrintingDelayFlags;
    wLetterPrintingDelayFlags = 0x01; // Fast text
    
    extern uint8_t wOptions;
    wOptions = 0x00; // Medium text delay
    
    extern uint8_t wPrinterSettings;
    wPrinterSettings = 0x40; // Default printer settings
}

// Export individual values for assembly linking
const uint8_t init_bypass_difficulty = DIFFICULTY_NORMAL;
const uint8_t init_bypass_gender_boy = GENDER_BOY;
const uint8_t init_bypass_gender_girl = GENDER_GIRL;
const uint8_t init_bypass_options_initialized = 1;
const uint8_t init_bypass_text_delay = 0x01;
const uint8_t init_bypass_options = 0x00;
const uint8_t init_bypass_printer = 0x40;
