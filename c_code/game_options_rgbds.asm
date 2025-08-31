; Game Options Control Functions
; This file provides functions to control game options like text speed, battle style, and animations
; Generated from C code by convert_game_options.py

SECTION "GameOptions", ROMX

; Function to set text speed to FAST
set_fast_text_speed::
	ld hl, wOptions
	ld a, [hl]
	and a, $F8
	or a, $01
	ld [hl], a
	ret

; Function to set text speed to MEDIUM
set_medium_text_speed::
	ld hl, wOptions
	ld a, [hl]
	and a, $F8
	or a, $03
	ld [hl], a
	ret

; Function to set text speed to SLOW
set_slow_text_speed::
	ld hl, wOptions
	ld a, [hl]
	and a, $F8
	or a, $05
	ld [hl], a
	ret

; Function to set battle style to SHIFT
set_battle_style_shift::
	ld hl, wOptions
	ld a, [hl]
	and a, $BF
	ld [hl], a
	ret

; Function to set battle style to SET
set_battle_style_set::
	ld hl, wOptions
	ld a, [hl]
	res 6, a
	or a, $40
	ld [hl], a
	ret

; Function to enable battle animations
enable_battle_animations::
	ld hl, wOptions
	ld a, [hl]
	and a, $7F
	ld [hl], a
	ret

; Function to disable battle animations
disable_battle_animations::
	ld hl, wOptions
	ld a, [hl]
	res 7, a
	or a, $80
	ld [hl], a
	ret

; Function to set all options to development settings
set_dev_options::
	ld hl, wOptions
	ld [hl], $01
	ret

; Function to set all options to testing settings
set_test_options::
	ld hl, wOptions
	ld [hl], $81
	ret

; Export constants for assembly linking
fast_text::
	db $01

medium_text::
	db $03

slow_text::
	db $05

shift_style::
	db $00

set_style::
	db $40

anim_on::
	db $00

anim_off::
	db $80

dev_preset::
	db $01

test_preset::
	db $81
