;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.2.2 #13350 (Linux)
;--------------------------------------------------------
	.module game_options
	.optsdcc -msm83
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _game_options_test_preset
	.globl _game_options_dev_preset
	.globl _game_options_anim_off
	.globl _game_options_anim_on
	.globl _game_options_set_style
	.globl _game_options_shift_style
	.globl _game_options_slow_text
	.globl _game_options_medium_text
	.globl _game_options_fast_text
	.globl _set_test_options
	.globl _set_dev_options
	.globl _disable_battle_animations
	.globl _enable_battle_animations
	.globl _set_battle_style_set
	.globl _set_battle_style_shift
	.globl _set_slow_text_speed
	.globl _set_medium_text_speed
	.globl _set_fast_text_speed
;--------------------------------------------------------
; special function registers
;--------------------------------------------------------
;--------------------------------------------------------
; ram data
;--------------------------------------------------------
	.area _DATA
;--------------------------------------------------------
; ram data
;--------------------------------------------------------
	.area _INITIALIZED
;--------------------------------------------------------
; absolute external ram data
;--------------------------------------------------------
	.area _DABS (ABS)
;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
	.area _HOME
	.area _GSINIT
	.area _GSFINAL
	.area _GSINIT
;--------------------------------------------------------
; Home
;--------------------------------------------------------
	.area _HOME
	.area _HOME
;--------------------------------------------------------
; code
;--------------------------------------------------------
	.area _CODE
;c_code/game_options.c:15: void set_fast_text_speed(void) {
;	---------------------------------
; Function set_fast_text_speed
; ---------------------------------
_set_fast_text_speed::
;c_code/game_options.c:19: wOptions = (wOptions & 0xF8) | TEXT_DELAY_FAST;
	ld	hl, #_wOptions
	ld	a, (hl)
	and	a, #0xf8
	or	a, #0x01
	ld	(hl), a
;c_code/game_options.c:20: }
	ret
;c_code/game_options.c:23: void set_medium_text_speed(void) {
;	---------------------------------
; Function set_medium_text_speed
; ---------------------------------
_set_medium_text_speed::
;c_code/game_options.c:27: wOptions = (wOptions & 0xF8) | TEXT_DELAY_MEDIUM;
	ld	hl, #_wOptions
	ld	a, (hl)
	and	a, #0xf8
	or	a, #0x03
	ld	(hl), a
;c_code/game_options.c:28: }
	ret
;c_code/game_options.c:31: void set_slow_text_speed(void) {
;	---------------------------------
; Function set_slow_text_speed
; ---------------------------------
_set_slow_text_speed::
;c_code/game_options.c:35: wOptions = (wOptions & 0xF8) | TEXT_DELAY_SLOW;
	ld	hl, #_wOptions
	ld	a, (hl)
	and	a, #0xf8
	or	a, #0x05
	ld	(hl), a
;c_code/game_options.c:36: }
	ret
;c_code/game_options.c:39: void set_battle_style_shift(void) {
;	---------------------------------
; Function set_battle_style_shift
; ---------------------------------
_set_battle_style_shift::
;c_code/game_options.c:43: wOptions = (wOptions & 0xBF) | BATTLE_STYLE_SHIFT;
	ld	hl, #_wOptions
	ld	a, (hl)
	and	a, #0xbf
	ld	(hl), a
;c_code/game_options.c:44: }
	ret
;c_code/game_options.c:47: void set_battle_style_set(void) {
;	---------------------------------
; Function set_battle_style_set
; ---------------------------------
_set_battle_style_set::
;c_code/game_options.c:51: wOptions = (wOptions & 0xBF) | BATTLE_STYLE_SET;
	ld	hl, #_wOptions
	ld	a, (hl)
	res	6, a
	or	a, #0x40
	ld	(hl), a
;c_code/game_options.c:52: }
	ret
;c_code/game_options.c:55: void enable_battle_animations(void) {
;	---------------------------------
; Function enable_battle_animations
; ---------------------------------
_enable_battle_animations::
;c_code/game_options.c:59: wOptions = (wOptions & 0x7F) | BATTLE_ANIMATION_ON;
	ld	hl, #_wOptions
	ld	a, (hl)
	and	a, #0x7f
	ld	(hl), a
;c_code/game_options.c:60: }
	ret
;c_code/game_options.c:63: void disable_battle_animations(void) {
;	---------------------------------
; Function disable_battle_animations
; ---------------------------------
_disable_battle_animations::
;c_code/game_options.c:67: wOptions = (wOptions & 0x7F) | BATTLE_ANIMATION_OFF;
	ld	hl, #_wOptions
	ld	a, (hl)
	res	7, a
	or	a, #0x80
	ld	(hl), a
;c_code/game_options.c:68: }
	ret
;c_code/game_options.c:71: void set_dev_options(void) {
;	---------------------------------
; Function set_dev_options
; ---------------------------------
_set_dev_options::
;c_code/game_options.c:75: wOptions = TEXT_DELAY_FAST | BATTLE_STYLE_SHIFT | BATTLE_ANIMATION_ON;
	ld	hl, #_wOptions
	ld	(hl), #0x01
;c_code/game_options.c:76: }
	ret
;c_code/game_options.c:79: void set_test_options(void) {
;	---------------------------------
; Function set_test_options
; ---------------------------------
_set_test_options::
;c_code/game_options.c:83: wOptions = TEXT_DELAY_FAST | BATTLE_STYLE_SHIFT | BATTLE_ANIMATION_OFF;
	ld	hl, #_wOptions
	ld	(hl), #0x81
;c_code/game_options.c:84: }
	ret
	.area _CODE
_game_options_fast_text:
	.db #0x01	; 1
_game_options_medium_text:
	.db #0x03	; 3
_game_options_slow_text:
	.db #0x05	; 5
_game_options_shift_style:
	.db #0x00	; 0
_game_options_set_style:
	.db #0x40	; 64
_game_options_anim_on:
	.db #0x00	; 0
_game_options_anim_off:
	.db #0x80	; 128
_game_options_dev_preset:
	.db #0x01	; 1
_game_options_test_preset:
	.db #0x81	; 129
	.area _INITIALIZER
	.area _CABS (ABS)
