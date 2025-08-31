;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.2.2 #13350 (Linux)
;--------------------------------------------------------
	.module money_management
	.optsdcc -msm83
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _give_ten_thousand_final
	.globl _give_ten_thousand_bcd
	.globl _give_little_money
	.globl _give_some_money
	.globl _give_lots_of_money
	.globl _give_max_money
	.globl _give_starting_money
	.globl _test_normal_money
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
;c_code/money_management.c:11: void test_normal_money(void) {
;	---------------------------------
; Function test_normal_money
; ---------------------------------
_test_normal_money::
;c_code/money_management.c:12: wPlayerMoney[0] = 0x00;  // Low byte
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:13: wPlayerMoney[1] = 0x30;  // Middle byte (what game normally sets)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x30
;c_code/money_management.c:14: wPlayerMoney[2] = 0x00;  // High byte
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:15: }
	ret
;c_code/money_management.c:18: void give_starting_money(void) {
;	---------------------------------
; Function give_starting_money
; ---------------------------------
_give_starting_money::
;c_code/money_management.c:19: wPlayerMoney[0] = 0x00;  // Low byte
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:20: wPlayerMoney[1] = 0x30;  // Middle byte ($3000)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x30
;c_code/money_management.c:21: wPlayerMoney[2] = 0x00;  // High byte
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:22: }
	ret
;c_code/money_management.c:25: void give_max_money(void) {
;	---------------------------------
; Function give_max_money
; ---------------------------------
_give_max_money::
;c_code/money_management.c:26: wPlayerMoney[0] = 0x99;  // Low byte (99)
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x99
;c_code/money_management.c:27: wPlayerMoney[1] = 0x99;  // Middle byte (99)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x99
;c_code/money_management.c:28: wPlayerMoney[2] = 0x99;  // High byte (99)
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x99
;c_code/money_management.c:29: }
	ret
;c_code/money_management.c:32: void give_lots_of_money(void) {
;	---------------------------------
; Function give_lots_of_money
; ---------------------------------
_give_lots_of_money::
;c_code/money_management.c:33: wPlayerMoney[0] = 0x00;  // Low byte (00)
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x00
;c_code/money_management.c:34: wPlayerMoney[1] = 0x00;  // Middle byte (00)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x00
;c_code/money_management.c:35: wPlayerMoney[2] = 0x10;  // High byte (10 = 100,000)
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x10
;c_code/money_management.c:36: }
	ret
;c_code/money_management.c:39: void give_some_money(void) {
;	---------------------------------
; Function give_some_money
; ---------------------------------
_give_some_money::
;c_code/money_management.c:40: wPlayerMoney[0] = 0x00;  // Low byte
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:41: wPlayerMoney[1] = 0x10;  // Middle byte (trying $10 = 16 in decimal)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x10
;c_code/money_management.c:42: wPlayerMoney[2] = 0x00;  // High byte
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:43: }
	ret
;c_code/money_management.c:46: void give_little_money(void) {
;	---------------------------------
; Function give_little_money
; ---------------------------------
_give_little_money::
;c_code/money_management.c:47: wPlayerMoney[0] = 0x00;  // Low byte (00)
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:48: wPlayerMoney[1] = 0x10;  // Middle byte (10 = 1,000)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x10
;c_code/money_management.c:49: wPlayerMoney[2] = 0x00;  // High byte (00)
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/money_management.c:50: }
	ret
;c_code/money_management.c:53: void give_ten_thousand_bcd(void) {
;	---------------------------------
; Function give_ten_thousand_bcd
; ---------------------------------
_give_ten_thousand_bcd::
;c_code/money_management.c:54: wPlayerMoney[0] = 0x10;  // Low byte (0x10 = 16 in decimal, 16 × 1000 = $16,000)
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x10
;c_code/money_management.c:55: wPlayerMoney[1] = 0x00;  // Middle byte (0x00 = 0 in decimal, 0 × 100 = $0)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x00
;c_code/money_management.c:56: wPlayerMoney[2] = 0x00;  // High byte (0x00 = 0 in decimal, 0 × 1 = $0)
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/money_management.c:57: }
	ret
;c_code/money_management.c:60: void give_ten_thousand_final(void) {
;	---------------------------------
; Function give_ten_thousand_final
; ---------------------------------
_give_ten_thousand_final::
;c_code/money_management.c:61: wPlayerMoney[0] = 0x01;  // Low byte (0x01 = 1 in decimal, 1 × 10,000 = $10,000)
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x01
;c_code/money_management.c:62: wPlayerMoney[1] = 0x00;  // Middle byte (0x00 = 0 in decimal, 0 × 100 = $0)
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x00
;c_code/money_management.c:63: wPlayerMoney[2] = 0x00;  // High byte (0x00 = 0 in decimal, 0 × 1 = $0)
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/money_management.c:64: }
	ret
	.area _CODE
	.area _INITIALIZER
	.area _CABS (ABS)
