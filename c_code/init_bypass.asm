; Initialization Bypass Functions
; This file provides functions to bypass the difficulty, gender, and name selection menus
; while preserving the natural graphics cleanup from Oak speech

SECTION "InitBypass", ROMX

; Function to bypass all initialization menus
; This sets up the variables and lets OakSpeech handle the graphics cleanup
bypass_init_menus::
    ; Set difficulty to normal (0)
    ld a, 0
    ld [wDifficulty], a
    
    ; Set gender to boy (0)
    ld a, 0
    ld [wPlayerGender], a
    
    ; Set player name to "TESTER"
    ld hl, wPlayerName
    ld a, "T"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "S"
    ld [hli], a
    ld a, "T"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "R"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set rival name to "DEBUG"
    ld hl, wRivalName
    ld a, "D"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "B"
    ld [hli], a
    ld a, "U"
    ld [hli], a
    ld a, "G"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set options initialized to 1 (skip options initialization)
    ; This flag will make OakSpeech jump to .skipSpeech
    ld a, 1
    ld [wOptionsInitialized], a
    
    ; Set default options
    ; Text speed will be set by set_slow_text_speed() call below
    
    ; Set game options to development-friendly settings
    call set_slow_text_speed      ; Set text speed to SLOW
    call set_battle_style_shift  ; Set battle style to SHIFT
    call enable_battle_animations ; Enable battle animations
    
    ld a, 64 ; Default printer settings
    ld [wPrinterSettings], a
    
    ret

; Alternative function for girl gender
bypass_init_menus_girl::
    ; Set difficulty to normal (0)
    ld a, 0
    ld [wDifficulty], a
    
    ; Set gender to girl (1)
    ld a, 1
    ld [wPlayerGender], a
    
    ; Set player name to "GREEN"
    ld hl, wPlayerName
    ld a, "G"
    ld [hli], a
    ld a, "R"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "N"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set rival name to "DEBUG"
    ld hl, wRivalName
    ld a, "D"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "B"
    ld [hli], a
    ld a, "U"
    ld [hli], a
    ld a, "G"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set options initialized to 1 (skip options initialization)
    ; This flag will make OakSpeech jump to .skipSpeech
    ld a, 1
    ld [wOptionsInitialized], a
    
    ; Set default options
    ; Text speed will be set by set_slow_text_speed() call below
    
    ; Set game options to development-friendly settings
    call set_slow_text_speed      ; Set text speed to SLOW
    call set_battle_style_shift  ; Set battle style to SHIFT
    call enable_battle_animations ; Enable battle animations
    
    ld a, 64 ; Default printer settings
    ld [wPrinterSettings], a
    
    ret

; Function to bypass ALL initialization including graphics cleanup
; This completely skips OakSpeech and goes straight to the map
bypass_graphics_cleanup::
    ; Set difficulty to normal (0)
    ld a, 0
    ld [wDifficulty], a
    
    ; Set gender to boy (0)
    ld a, 0
    ld [wPlayerGender], a
    
    ; Set player name to "TESTER"
    ld hl, wPlayerName
    ld a, "T"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "S"
    ld [hli], a
    ld a, "T"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "R"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set rival name to "DEBUG"
    ld hl, wRivalName
    ld a, "D"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "B"
    ld [hli], a
    ld a, "U"
    ld [hli], a
    ld a, "G"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set options initialized to 1 (skip options initialization)
    ; This flag will make OakSpeech jump to .skipSpeech
    ld a, 1
    ld [wOptionsInitialized], a
    
    ; Set default options
    ; Text speed will be set by set_slow_text_speed() call below
    
    ; Set game options to development-friendly settings
    call set_slow_text_speed      ; Set text speed to SLOW
    call set_battle_style_shift  ; Set battle style to SHIFT
    call enable_battle_animations ; Enable battle animations
    
    ld a, 64 ; Default printer settings
    ld [wPrinterSettings], a
    
    ; Set up player data and inventory like OakSpeech would
    predef InitPlayerData2
    ld hl, wNumBoxItems
    ld a, POTION
    ld [wcf91], a
    ld a, 1
    ld [wItemQuantity], a
    call AddItemToInventory
    
    ; Set up the destination map
    ld a, [wDefaultMap]
    ld [wDestinationMap], a
    call PrepareForSpecialWarp
    
    ; Set up player sprite data
    xor a
    ldh [hTileAnimations], a
    ld a, $8
    ld [wPlayerMovingDirection], a
    ld c, 20
    call DelayFrames
    
    ; Jump directly to SpecialEnterMap, bypassing all graphics cleanup
    jp SpecialEnterMap

; Alternative function for girl gender (graphics bypass)
bypass_graphics_cleanup_girl::
    ; Set difficulty to normal (0)
    ld a, 0
    ld [wDifficulty], a
    
    ; Set gender to girl (1)
    ld a, 1
    ld [wPlayerGender], a
    
    ; Set player name to "GREEN"
    ld hl, wPlayerName
    ld a, "G"
    ld [hli], a
    ld a, "R"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "N"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set rival name to "DEBUG"
    ld hl, wRivalName
    ld a, "D"
    ld [hli], a
    ld a, "E"
    ld [hli], a
    ld a, "B"
    ld [hli], a
    ld a, "U"
    ld [hli], a
    ld a, "G"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    ; Fill remaining bytes with 0
    xor a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    
    ; Set options initialized to 1 (skip options initialization)
    ; This flag will make OakSpeech jump to .skipSpeech
    ld a, 1
    ld [wOptionsInitialized], a
    
    ; Set default options
    ; Text speed will be set by set_slow_text_speed() call below
    
    ; Set game options to development-friendly settings
    call set_slow_text_speed      ; Set text speed to SLOW
    call set_battle_style_shift  ; Set battle style to SHIFT
    call enable_battle_animations ; Enable battle animations
    
    ld a, 64 ; Default printer settings
    ld [wPrinterSettings], a
    
    ; Set up player data and inventory like OakSpeech would
    predef InitPlayerData2
    ld hl, wNumBoxItems
    ld a, POTION
    ld [wcf91], a
    ld a, 1
    ld [wItemQuantity], a
    call AddItemToInventory
    
    ; Set up the destination map
    ld a, [wDefaultMap]
    ld [wDestinationMap], a
    call PrepareForSpecialWarp
    
    ; Set up player sprite data
    xor a
    ldh [hTileAnimations], a
    ld a, $8
    ld [wPlayerMovingDirection], a
    ld c, 20
    call DelayFrames
    
    ; Jump directly to SpecialEnterMap, bypassing all graphics cleanup
    jp SpecialEnterMap
