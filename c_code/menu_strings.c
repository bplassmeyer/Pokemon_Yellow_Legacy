// Menu strings for Pokemon Yellow Legacy
// This file provides C-compiled strings that replace assembly string definitions

// Game Boy character encoding and string format
// The original assembly format was:
// db "NEW GAME"
// next "OPTION@"
// where "next" expands to db "<NEXT>" and "@" is a string terminator ($50)

#include <stdint.h>

// Export the string data as separate lines
// Line 1: "PENIS G"
const uint8_t new_game_line1[] = {
    'B', 'E', 'N', 'I', 'S', ' ', 'G'
};

// Line 2: "OPTION"
const uint8_t new_game_line2[] = {
    'B', 'P', 'T', 'I', 'O', 'N'
};

// Alternative: export as C strings for easier manipulation
const char new_game_line1_str[] = "PENIS G";
const char new_game_line2_str[] = "OPTION";

// Export the lengths for assembly linking
const uint16_t new_game_line1_length = sizeof(new_game_line1);
const uint16_t new_game_line2_length = sizeof(new_game_line2);
