;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.2.2 #13350 (Linux)
;--------------------------------------------------------
	.module menu_strings
	.optsdcc -msm83
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _new_game_line2_length
	.globl _new_game_line1_length
	.globl _new_game_line2_str
	.globl _new_game_line1_str
	.globl _new_game_line2
	.globl _new_game_line1
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
	.area _CODE
_new_game_line1:
	.db #0x42	; 66	'B'
	.db #0x45	; 69	'E'
	.db #0x4e	; 78	'N'
	.db #0x49	; 73	'I'
	.db #0x53	; 83	'S'
	.db #0x20	; 32
	.db #0x47	; 71	'G'
_new_game_line2:
	.db #0x42	; 66	'B'
	.db #0x50	; 80	'P'
	.db #0x54	; 84	'T'
	.db #0x49	; 73	'I'
	.db #0x4f	; 79	'O'
	.db #0x4e	; 78	'N'
_new_game_line1_str:
	.ascii "PENIS G"
	.db 0x00
_new_game_line2_str:
	.ascii "OPTION"
	.db 0x00
_new_game_line1_length:
	.dw #0x0007
_new_game_line2_length:
	.dw #0x0006
	.area _INITIALIZER
	.area _CABS (ABS)
