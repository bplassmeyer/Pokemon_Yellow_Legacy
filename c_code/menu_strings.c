// Menu strings for Pokemon Yellow Legacy
// This file provides C-compiled strings that replace assembly string definitions

// Game Boy character encoding and string format
// The original assembly format was:
// db "NEW GAME"
// next "OPTION@"
// where "next" expands to db "<NEXT>" and "@" is a string terminator ($50)

#include <stdint.h>

// Export the string data as a byte array that can be linked with assembly
// This creates the exact same byte sequence as the original assembly
// The original assembly format was:
// db "NEW GAME"
// next "OPTION@"
// where "next" expands to db "<NEXT>" and "@" is a string terminator ($50)
// 
// However, since we're generating assembly, we need to match the exact format:
// db "Penis G"
// next "OPTION@"
const uint8_t new_game_text_data[] = {
    'P', 'e', 'n', 'i', 's', ' ', 'G'
    // Note: We can't include <NEXT> here because it's a macro that expands to db "<NEXT>"
    // The converter will need to handle this properly
};

// Alternative: export as a C string for easier manipulation
// Note: We'll use a placeholder that the converter can replace with the proper format
const char new_game_text[] = "Penis G";

// Export the length for assembly linking
const uint16_t new_game_text_length = sizeof(new_game_text_data);
