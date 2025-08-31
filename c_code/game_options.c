#include <stdint.h>

// Game options constants
#define TEXT_DELAY_FAST   0x01
#define TEXT_DELAY_MEDIUM 0x03
#define TEXT_DELAY_SLOW   0x05

#define BATTLE_STYLE_SHIFT 0x00
#define BATTLE_STYLE_SET   0x40

#define BATTLE_ANIMATION_ON  0x00
#define BATTLE_ANIMATION_OFF 0x80

// Function to set fast text speed
void set_fast_text_speed(void) {
    extern uint8_t wOptions;
    
    // Clear text speed bits (0-2) and set to FAST
    wOptions = (wOptions & 0xF8) | TEXT_DELAY_FAST;
}

// Function to set medium text speed
void set_medium_text_speed(void) {
    extern uint8_t wOptions;
    
    // Clear text speed bits (0-2) and set to MEDIUM
    wOptions = (wOptions & 0xF8) | TEXT_DELAY_MEDIUM;
}

// Function to set slow text speed
void set_slow_text_speed(void) {
    extern uint8_t wOptions;
    
    // Clear text speed bits (0-2) and set to SLOW
    wOptions = (wOptions & 0xF8) | TEXT_DELAY_SLOW;
}

// Function to set battle style to SHIFT
void set_battle_style_shift(void) {
    extern uint8_t wOptions;
    
    // Clear battle style bit (6) and set to SHIFT
    wOptions = (wOptions & 0xBF) | BATTLE_STYLE_SHIFT;
}

// Function to set battle style to SET
void set_battle_style_set(void) {
    extern uint8_t wOptions;
    
    // Set battle style bit (6) to SET
    wOptions = (wOptions & 0xBF) | BATTLE_STYLE_SET;
}

// Function to enable battle animations
void enable_battle_animations(void) {
    extern uint8_t wOptions;
    
    // Clear battle animation bit (7) to enable
    wOptions = (wOptions & 0x7F) | BATTLE_ANIMATION_ON;
}

// Function to disable battle animations
void disable_battle_animations(void) {
    extern uint8_t wOptions;
    
    // Set battle animation bit (7) to disable
    wOptions = (wOptions & 0x7F) | BATTLE_ANIMATION_OFF;
}

// Function to set all options to recommended development settings
void set_dev_options(void) {
    extern uint8_t wOptions;
    
    // Set to FAST text, SHIFT battle style, animations ON
    wOptions = TEXT_DELAY_FAST | BATTLE_STYLE_SHIFT | BATTLE_ANIMATION_ON;
}

// Function to set all options to recommended testing settings
void set_test_options(void) {
    extern uint8_t wOptions;
    
    // Set to FAST text, SHIFT battle style, animations OFF (faster battles)
    wOptions = TEXT_DELAY_FAST | BATTLE_STYLE_SHIFT | BATTLE_ANIMATION_OFF;
}

// Export individual values for assembly linking
const uint8_t game_options_fast_text = TEXT_DELAY_FAST;
const uint8_t game_options_medium_text = TEXT_DELAY_MEDIUM;
const uint8_t game_options_slow_text = TEXT_DELAY_SLOW;
const uint8_t game_options_shift_style = BATTLE_STYLE_SHIFT;
const uint8_t game_options_set_style = BATTLE_STYLE_SET;
const uint8_t game_options_anim_on = BATTLE_ANIMATION_ON;
const uint8_t game_options_anim_off = BATTLE_ANIMATION_OFF;
const uint8_t game_options_dev_preset = TEXT_DELAY_FAST | BATTLE_STYLE_SHIFT | BATTLE_ANIMATION_ON;
const uint8_t game_options_test_preset = TEXT_DELAY_FAST | BATTLE_STYLE_SHIFT | BATTLE_ANIMATION_OFF;
