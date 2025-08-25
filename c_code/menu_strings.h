#ifndef MENU_STRINGS_H
#define MENU_STRINGS_H

#include <stdint.h>

// External declarations for C-compiled strings
// These replace the assembly NewGameText definition

// Main string data as byte array (matches assembly format exactly)
extern const uint8_t new_game_text_data[];

// Alternative C string format
extern const char new_game_text[];

// Length information for assembly linking
extern const uint16_t new_game_text_length;

#endif // MENU_STRINGS_H
