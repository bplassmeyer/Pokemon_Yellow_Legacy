// Menu strings for Pokemon Yellow Legacy
// This file provides C-compiled strings that replace assembly string definitions

// Game Boy character encoding and string format
// The original assembly format was:
// db "NEW GAME"
// next "OPTION@"
// where "next" inserts a newline character and "@" is a string terminator ($50)

#include <stdint.h>

// Export the string data as a byte array that can be linked with assembly
// This creates the exact same byte sequence as the original assembly
const uint8_t new_game_text_data[] = {
    'P', 'e', 'n', 'i', 's', 'U', 'T', 'T',
    0x4E,
    'O', 'P', 'T', 'I', 'O', 'N',
    0x50
};

// Alternative: export as a C string for easier manipulation
const char new_game_text[] = "CUSTOM G\nOPTION\x50";

// Export the length for assembly linking
const uint16_t new_game_text_length = sizeof(new_game_text_data);
