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
    ld a, 1  ; Fast text
    ld [wLetterPrintingDelayFlags], a
    
    ld a, 0  ; Medium text delay
    ld [wOptions], a
    
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
    ld a, 1  ; Fast text
    ld [wLetterPrintingDelayFlags], a
    
    ld a, 0  ; Medium text delay
    ld [wOptions], a
    
    ld a, 64 ; Default printer settings
    ld [wPrinterSettings], a
    
    ret
