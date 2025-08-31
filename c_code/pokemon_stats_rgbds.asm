; Pokemon base stats - Generated from C code
; This file contains Pokemon base stats converted from C

SECTION "PokemonStats", ROMX

; Pikachu base stats
PikachuBaseStats::
	; Pokedex ID
	db $19
	; Base stats: HP, ATK, DEF, SPD, SPC
	db $3C, $37, $32, $5A, $46
	; Types
	db $17, $17
	; Catch rate and base exp
	db $BE
	db $52
	; Growth rate
	db $00

; Pidgey base stats
PidgeyBaseStats::
	; Pokedex ID
	db $18
	; Base stats: HP, ATK, DEF, SPD, SPC
	db $14, $14, $14, $14, $14
	; Types
	db $00, $02
	; Catch rate and base exp
	db $FF
	db $37
	; Growth rate
	db $03

; Rattata base stats
RattataBaseStats::
	; Pokedex ID
	db $13
	; Base stats: HP, ATK, DEF, SPD, SPC
	db $14, $14, $14, $14, $14
	; Types
	db $02, $02
	; Catch rate and base exp
	db $FF
	db $39
	; Growth rate
	db $00
