;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.2.2 #13350 (Linux)
;--------------------------------------------------------
	.module pokemon_stats
	.optsdcc -msm83
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _rattata_stats_size
	.globl _pidgey_stats_size
	.globl _pikachu_stats_size
	.globl _eevee_growth_rate
	.globl _eevee_base_exp
	.globl _eevee_catch_rate
	.globl _eevee_type2
	.globl _eevee_type1
	.globl _eevee_spc
	.globl _eevee_spd
	.globl _eevee_def
	.globl _eevee_atk
	.globl _eevee_hp
	.globl _eevee_dex_id
	.globl _rattata_growth_rate
	.globl _rattata_base_exp
	.globl _rattata_catch_rate
	.globl _rattata_type2
	.globl _rattata_type1
	.globl _rattata_spc
	.globl _rattata_spd
	.globl _rattata_def
	.globl _rattata_atk
	.globl _rattata_hp
	.globl _rattata_dex_id
	.globl _pidgey_growth_rate
	.globl _pidgey_base_exp
	.globl _pidgey_catch_rate
	.globl _pidgey_type2
	.globl _pidgey_type1
	.globl _pidgey_spc
	.globl _pidgey_spd
	.globl _pidgey_def
	.globl _pidgey_atk
	.globl _pidgey_hp
	.globl _pidgey_dex_id
	.globl _pikachu_growth_rate
	.globl _pikachu_base_exp
	.globl _pikachu_catch_rate
	.globl _pikachu_type2
	.globl _pikachu_type1
	.globl _pikachu_spc
	.globl _pikachu_spd
	.globl _pikachu_def
	.globl _pikachu_atk
	.globl _pikachu_hp
	.globl _pikachu_dex_id
	.globl _eevee_stats
	.globl _rattata_stats
	.globl _pidgey_stats
	.globl _pikachu_stats
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
_pikachu_stats:
	.db #0x19	; 25
	.db #0x3c	; 60
	.db #0x37	; 55	'7'
	.db #0x32	; 50	'2'
	.db #0x5a	; 90	'Z'
	.db #0x46	; 70	'F'
	.db #0x17	; 23
	.db #0x17	; 23
	.db #0xbe	; 190
	.db #0x52	; 82	'R'
	.db #0x00	; 0
_pidgey_stats:
	.db #0x18	; 24
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x00	; 0
	.db #0x02	; 2
	.db #0xff	; 255
	.db #0x37	; 55	'7'
	.db #0x03	; 3
_rattata_stats:
	.db #0x13	; 19
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x14	; 20
	.db #0x02	; 2
	.db #0x02	; 2
	.db #0xff	; 255
	.db #0x39	; 57	'9'
	.db #0x00	; 0
_eevee_stats:
	.db #0x85	; 133
	.db #0x37	; 55	'7'
	.db #0x37	; 55	'7'
	.db #0x32	; 50	'2'
	.db #0x37	; 55	'7'
	.db #0x41	; 65	'A'
	.db #0x02	; 2
	.db #0x02	; 2
	.db #0x2d	; 45
	.db #0x5c	; 92
	.db #0x00	; 0
_pikachu_dex_id:
	.byte (_pikachu_stats + 0)
_pikachu_hp:
	.byte (_pikachu_stats + 1)
_pikachu_atk:
	.byte (_pikachu_stats + 2)
_pikachu_def:
	.byte (_pikachu_stats + 3)
_pikachu_spd:
	.byte (_pikachu_stats + 4)
_pikachu_spc:
	.byte (_pikachu_stats + 5)
_pikachu_type1:
	.byte (_pikachu_stats + 6)
_pikachu_type2:
	.byte (_pikachu_stats + 7)
_pikachu_catch_rate:
	.byte (_pikachu_stats + 8)
_pikachu_base_exp:
	.byte (_pikachu_stats + 9)
_pikachu_growth_rate:
	.byte (_pikachu_stats + 10)
_pidgey_dex_id:
	.byte (_pidgey_stats + 0)
_pidgey_hp:
	.byte (_pidgey_stats + 1)
_pidgey_atk:
	.byte (_pidgey_stats + 2)
_pidgey_def:
	.byte (_pidgey_stats + 3)
_pidgey_spd:
	.byte (_pidgey_stats + 4)
_pidgey_spc:
	.byte (_pidgey_stats + 5)
_pidgey_type1:
	.byte (_pidgey_stats + 6)
_pidgey_type2:
	.byte (_pidgey_stats + 7)
_pidgey_catch_rate:
	.byte (_pidgey_stats + 8)
_pidgey_base_exp:
	.byte (_pidgey_stats + 9)
_pidgey_growth_rate:
	.byte (_pidgey_stats + 10)
_rattata_dex_id:
	.byte (_rattata_stats + 0)
_rattata_hp:
	.byte (_rattata_stats + 1)
_rattata_atk:
	.byte (_rattata_stats + 2)
_rattata_def:
	.byte (_rattata_stats + 3)
_rattata_spd:
	.byte (_rattata_stats + 4)
_rattata_spc:
	.byte (_rattata_stats + 5)
_rattata_type1:
	.byte (_rattata_stats + 6)
_rattata_type2:
	.byte (_rattata_stats + 7)
_rattata_catch_rate:
	.byte (_rattata_stats + 8)
_rattata_base_exp:
	.byte (_rattata_stats + 9)
_rattata_growth_rate:
	.byte (_rattata_stats + 10)
_eevee_dex_id:
	.byte (_eevee_stats + 0)
_eevee_hp:
	.byte (_eevee_stats + 1)
_eevee_atk:
	.byte (_eevee_stats + 2)
_eevee_def:
	.byte (_eevee_stats + 3)
_eevee_spd:
	.byte (_eevee_stats + 4)
_eevee_spc:
	.byte (_eevee_stats + 5)
_eevee_type1:
	.byte (_eevee_stats + 6)
_eevee_type2:
	.byte (_eevee_stats + 7)
_eevee_catch_rate:
	.byte (_eevee_stats + 8)
_eevee_base_exp:
	.byte (_eevee_stats + 9)
_eevee_growth_rate:
	.byte (_eevee_stats + 10)
_pikachu_stats_size:
	.dw #0x000b
_pidgey_stats_size:
	.dw #0x000b
_rattata_stats_size:
	.dw #0x000b
	.area _INITIALIZER
	.area _CABS (ABS)
