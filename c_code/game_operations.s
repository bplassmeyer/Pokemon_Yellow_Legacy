;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.2.2 #13350 (Linux)
;--------------------------------------------------------
	.module game_operations
	.optsdcc -msm83
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _give_master_kit
	.globl _give_battle_kit
	.globl _give_starter_kit
	.globl _give_max_revives
	.globl _give_revives
	.globl _give_full_restores
	.globl _give_hyper_potions
	.globl _give_super_potions
	.globl _give_potions
	.globl _give_ultra_balls
	.globl _give_great_balls
	.globl _give_lots_of_pokeballs
	.globl _give_pokeballs
	.globl _clear_bag
	.globl _give_twenty_five_thousand
	.globl _give_fifteen_thousand
	.globl _give_nine_thousand
	.globl _give_five_thousand
	.globl _give_one_thousand
	.globl _give_hundred_thousand
	.globl _give_fifty_thousand
	.globl _give_ten_thousand
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
;c_code/game_operations.c:19: void give_ten_thousand(void) {
;	---------------------------------
; Function give_ten_thousand
; ---------------------------------
_give_ten_thousand::
;c_code/game_operations.c:20: wPlayerMoney[0] = 0x01;  // 1 × 10,000 = $10,000
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x01
;c_code/game_operations.c:21: wPlayerMoney[1] = 0x00;  // 0 × 100 = $0
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x00
;c_code/game_operations.c:22: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/game_operations.c:23: }
	ret
;c_code/game_operations.c:26: void give_fifty_thousand(void) {
;	---------------------------------
; Function give_fifty_thousand
; ---------------------------------
_give_fifty_thousand::
;c_code/game_operations.c:27: wPlayerMoney[0] = 0x05;  // 5 × 10,000 = $50,000
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x05
;c_code/game_operations.c:28: wPlayerMoney[1] = 0x00;  // 0 × 100 = $0
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x00
;c_code/game_operations.c:29: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/game_operations.c:30: }
	ret
;c_code/game_operations.c:33: void give_hundred_thousand(void) {
;	---------------------------------
; Function give_hundred_thousand
; ---------------------------------
_give_hundred_thousand::
;c_code/game_operations.c:34: wPlayerMoney[0] = 0x0A;  // 10 × 10,000 = $100,000
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x0a
;c_code/game_operations.c:35: wPlayerMoney[1] = 0x00;  // 0 × 100 = $0
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x00
;c_code/game_operations.c:36: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/game_operations.c:37: }
	ret
;c_code/game_operations.c:40: void give_one_thousand(void) {
;	---------------------------------
; Function give_one_thousand
; ---------------------------------
_give_one_thousand::
;c_code/game_operations.c:41: wPlayerMoney[0] = 0x00;  // 0 × 10,000 = $0
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/game_operations.c:42: wPlayerMoney[1] = 0x0A;  // 10 × 100 = $1,000
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x0a
;c_code/game_operations.c:43: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/game_operations.c:44: }
	ret
;c_code/game_operations.c:47: void give_five_thousand(void) {
;	---------------------------------
; Function give_five_thousand
; ---------------------------------
_give_five_thousand::
;c_code/game_operations.c:48: wPlayerMoney[0] = 0x00;  // 0 × 10,000 = $0
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/game_operations.c:49: wPlayerMoney[1] = 0x32;  // 50 × 100 = $5,000
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x32
;c_code/game_operations.c:50: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/game_operations.c:51: }
	ret
;c_code/game_operations.c:54: void give_nine_thousand(void) {
;	---------------------------------
; Function give_nine_thousand
; ---------------------------------
_give_nine_thousand::
;c_code/game_operations.c:55: wPlayerMoney[0] = 0x00;  // 0 × 10,000 = $0
	ld	bc, #_wPlayerMoney+0
	xor	a, a
	ld	(bc), a
;c_code/game_operations.c:56: wPlayerMoney[1] = 0x5A;  // 90 × 100 = $9,000
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x5a
;c_code/game_operations.c:57: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	inc	bc
	inc	bc
	xor	a, a
	ld	(bc), a
;c_code/game_operations.c:58: }
	ret
;c_code/game_operations.c:61: void give_fifteen_thousand(void) {
;	---------------------------------
; Function give_fifteen_thousand
; ---------------------------------
_give_fifteen_thousand::
;c_code/game_operations.c:62: wPlayerMoney[0] = 0x01;  // 1 × 10,000 = $10,000
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x01
;c_code/game_operations.c:63: wPlayerMoney[1] = 0x32;  // 50 × 100 = $5,000
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x32
;c_code/game_operations.c:64: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/game_operations.c:65: }
	ret
;c_code/game_operations.c:68: void give_twenty_five_thousand(void) {
;	---------------------------------
; Function give_twenty_five_thousand
; ---------------------------------
_give_twenty_five_thousand::
;c_code/game_operations.c:69: wPlayerMoney[0] = 0x02;  // 2 × 10,000 = $20,000
	ld	hl, #_wPlayerMoney
	ld	(hl), #0x02
;c_code/game_operations.c:70: wPlayerMoney[1] = 0x32;  // 50 × 100 = $5,000
	ld	hl, #(_wPlayerMoney + 1)
	ld	(hl), #0x32
;c_code/game_operations.c:71: wPlayerMoney[2] = 0x00;  // 0 × 1 = $0
	ld	hl, #(_wPlayerMoney + 2)
	ld	(hl), #0x00
;c_code/game_operations.c:72: }
	ret
;c_code/game_operations.c:79: void clear_bag(void) {
;	---------------------------------
; Function clear_bag
; ---------------------------------
_clear_bag::
;c_code/game_operations.c:80: wNumBagItems = 0;
	ld	hl, #_wNumBagItems
	ld	(hl), #0x00
;c_code/game_operations.c:81: }
	ret
;c_code/game_operations.c:84: void give_pokeballs(void) {
;	---------------------------------
; Function give_pokeballs
; ---------------------------------
_give_pokeballs::
;c_code/game_operations.c:88: }
	ret
;c_code/game_operations.c:91: void give_lots_of_pokeballs(void) {
;	---------------------------------
; Function give_lots_of_pokeballs
; ---------------------------------
_give_lots_of_pokeballs::
;c_code/game_operations.c:92: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:93: wBagItems[wNumBagItems * 2] = 0x04;      // POKE_BALL item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x04
;c_code/game_operations.c:94: wBagItems[wNumBagItems * 2 + 1] = 10;    // Quantity: 10
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x0a
;c_code/game_operations.c:95: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:97: }
	ret
;c_code/game_operations.c:100: void give_great_balls(void) {
;	---------------------------------
; Function give_great_balls
; ---------------------------------
_give_great_balls::
;c_code/game_operations.c:101: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:102: wBagItems[wNumBagItems * 2] = 0x03;      // GREAT_BALL item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x03
;c_code/game_operations.c:103: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:104: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:106: }
	ret
;c_code/game_operations.c:109: void give_ultra_balls(void) {
;	---------------------------------
; Function give_ultra_balls
; ---------------------------------
_give_ultra_balls::
;c_code/game_operations.c:110: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:111: wBagItems[wNumBagItems * 2] = 0x02;      // ULTRA_BALL item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x02
;c_code/game_operations.c:112: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:113: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:115: }
	ret
;c_code/game_operations.c:118: void give_potions(void) {
;	---------------------------------
; Function give_potions
; ---------------------------------
_give_potions::
;c_code/game_operations.c:119: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:120: wBagItems[wNumBagItems * 2] = 0x14;      // POTION item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x14
;c_code/game_operations.c:121: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:122: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:124: }
	ret
;c_code/game_operations.c:127: void give_super_potions(void) {
;	---------------------------------
; Function give_super_potions
; ---------------------------------
_give_super_potions::
;c_code/game_operations.c:128: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:129: wBagItems[wNumBagItems * 2] = 0x13;      // SUPER_POTION item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x13
;c_code/game_operations.c:130: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:131: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:133: }
	ret
;c_code/game_operations.c:136: void give_hyper_potions(void) {
;	---------------------------------
; Function give_hyper_potions
; ---------------------------------
_give_hyper_potions::
;c_code/game_operations.c:137: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:138: wBagItems[wNumBagItems * 2] = 0x12;      // HYPER_POTION item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x12
;c_code/game_operations.c:139: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:140: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:142: }
	ret
;c_code/game_operations.c:145: void give_full_restores(void) {
;	---------------------------------
; Function give_full_restores
; ---------------------------------
_give_full_restores::
;c_code/game_operations.c:146: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:147: wBagItems[wNumBagItems * 2] = 0x10;      // FULL_RESTORE item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x10
;c_code/game_operations.c:148: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:149: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:151: }
	ret
;c_code/game_operations.c:154: void give_revives(void) {
;	---------------------------------
; Function give_revives
; ---------------------------------
_give_revives::
;c_code/game_operations.c:155: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:156: wBagItems[wNumBagItems * 2] = 0x35;      // REVIVE item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x35
;c_code/game_operations.c:157: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:158: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:160: }
	ret
;c_code/game_operations.c:163: void give_max_revives(void) {
;	---------------------------------
; Function give_max_revives
; ---------------------------------
_give_max_revives::
;c_code/game_operations.c:164: if (wNumBagItems < 59) {
	ld	hl, #_wNumBagItems
	ld	a, (hl)
	sub	a, #0x3b
	ret	NC
;c_code/game_operations.c:165: wBagItems[wNumBagItems * 2] = 0x36;      // MAX_REVIVE item ID
	ld	bc, #_wBagItems+0
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	add	hl, bc
	ld	(hl), #0x36
;c_code/game_operations.c:166: wBagItems[wNumBagItems * 2 + 1] = 5;     // Quantity: 5
	ld	hl, #_wNumBagItems
	ld	l, (hl)
;	spillPairReg hl
;	spillPairReg hl
	ld	h, #0x00
;	spillPairReg hl
;	spillPairReg hl
	add	hl, hl
	inc	hl
	add	hl, bc
	ld	(hl), #0x05
;c_code/game_operations.c:167: wNumBagItems++;
	ld	hl, #_wNumBagItems
	inc	(hl)
;c_code/game_operations.c:169: }
	ret
;c_code/game_operations.c:172: void give_starter_kit(void) {
;	---------------------------------
; Function give_starter_kit
; ---------------------------------
_give_starter_kit::
;c_code/game_operations.c:173: give_pokeballs();
	call	_give_pokeballs
;c_code/game_operations.c:174: give_potions();
;c_code/game_operations.c:175: }
	jp	_give_potions
;c_code/game_operations.c:178: void give_battle_kit(void) {
;	---------------------------------
; Function give_battle_kit
; ---------------------------------
_give_battle_kit::
;c_code/game_operations.c:179: give_great_balls();
	call	_give_great_balls
;c_code/game_operations.c:180: give_super_potions();
	call	_give_super_potions
;c_code/game_operations.c:181: give_revives();
;c_code/game_operations.c:182: }
	jp	_give_revives
;c_code/game_operations.c:185: void give_master_kit(void) {
;	---------------------------------
; Function give_master_kit
; ---------------------------------
_give_master_kit::
;c_code/game_operations.c:186: give_ultra_balls();
	call	_give_ultra_balls
;c_code/game_operations.c:187: give_hyper_potions();
	call	_give_hyper_potions
;c_code/game_operations.c:188: give_max_revives();
;c_code/game_operations.c:189: }
	jp	_give_max_revives
	.area _CODE
	.area _INITIALIZER
	.area _CABS (ABS)
