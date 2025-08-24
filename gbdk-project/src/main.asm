;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler
; Version 4.5.1 #15267 (Linux)
;--------------------------------------------------------
	.module main
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _main
	.globl _update_game
	.globl _init_game
	.globl _set_sprite_data
	.globl _wait_vbl_done
	.globl _joypad
	.globl _delay
	.globl _player_sprite
	.globl _game_state
	.globl _player_y
	.globl _player_x
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
_player_x::
	.ds 1
_player_y::
	.ds 1
_game_state::
	.ds 1
_player_sprite::
	.ds 8
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
;src/main.c:14: void init_game(void) {
;	---------------------------------
; Function init_game
; ---------------------------------
_init_game::
;src/main.c:16: DISPLAY_ON;
	ldh	a, (_LCDC_REG + 0)
	or	a, #0x80
	ldh	(_LCDC_REG + 0), a
;src/main.c:17: SHOW_SPRITES;
	ldh	a, (_LCDC_REG + 0)
	or	a, #0x02
	ldh	(_LCDC_REG + 0), a
;src/main.c:18: SHOW_BKG;
	ldh	a, (_LCDC_REG + 0)
	or	a, #0x01
	ldh	(_LCDC_REG + 0), a
;src/main.c:21: BGP_REG = 0xE4;  // Light green background
	ld	a, #0xe4
	ldh	(_BGP_REG + 0), a
;src/main.c:24: set_sprite_data(0, 1, player_sprite);
	ld	de, #_player_sprite
	push	de
	xor	a, a
	inc	a
	push	af
	call	_set_sprite_data
	add	sp, #4
;/home/brennan/.local/gbdk/include/gb/gb.h:1887: shadow_OAM[nb].tile=tile;
	ld	hl, #(_shadow_OAM + 2)
;src/main.c:26: move_sprite(0, player_x, player_y);
;/home/brennan/.local/gbdk/include/gb/gb.h:1973: OAM_item_t * itm = &shadow_OAM[nb];
	xor	a, a
	ld	(hl-), a
	dec	hl
	ld	a, (_player_y)
	ld	b, a
	ld	a, (_player_x)
	ld	c, a
;/home/brennan/.local/gbdk/include/gb/gb.h:1974: itm->y=y, itm->x=x;
	ld	a, b
	ld	(hl+), a
	ld	(hl), c
;src/main.c:29: game_state = 1;
	ld	hl, #_game_state
	ld	(hl), #0x01
;src/main.c:30: }
	ret
;src/main.c:32: void update_game(void) {
;	---------------------------------
; Function update_game
; ---------------------------------
_update_game::
;src/main.c:34: UINT8 keys = joypad();
	call	_joypad
	ld	c, a
;src/main.c:36: if (keys & J_LEFT && player_x > 0) {
	bit	1, c
	jr	Z, 00102$
	ld	hl, #_player_x
	ld	a, (hl)
	or	a, a
	jr	Z, 00102$
;src/main.c:37: player_x -= 2;
	ld	a, (hl)
	add	a, #0xfe
	ld	(hl), a
;src/main.c:38: move_sprite(0, player_x, player_y);
	ld	a, (_player_y)
	ld	e, a
	ld	b, (hl)
;/home/brennan/.local/gbdk/include/gb/gb.h:1973: OAM_item_t * itm = &shadow_OAM[nb];
	ld	hl, #_shadow_OAM
;/home/brennan/.local/gbdk/include/gb/gb.h:1974: itm->y=y, itm->x=x;
	ld	a, e
	ld	(hl+), a
	ld	(hl), b
;src/main.c:38: move_sprite(0, player_x, player_y);
00102$:
;src/main.c:40: if (keys & J_RIGHT && player_x < 160) {
	bit	0, c
	jr	Z, 00105$
	ld	hl, #_player_x
	ld	a, (hl)
	sub	a, #0xa0
	jr	NC, 00105$
;src/main.c:41: player_x += 2;
	ld	a, (hl)
	add	a, #0x02
	ld	(hl), a
;src/main.c:42: move_sprite(0, player_x, player_y);
	ld	a, (_player_y)
	ld	e, a
	ld	b, (hl)
;/home/brennan/.local/gbdk/include/gb/gb.h:1973: OAM_item_t * itm = &shadow_OAM[nb];
	ld	hl, #_shadow_OAM
;/home/brennan/.local/gbdk/include/gb/gb.h:1974: itm->y=y, itm->x=x;
	ld	a, e
	ld	(hl+), a
	ld	(hl), b
;src/main.c:42: move_sprite(0, player_x, player_y);
00105$:
;src/main.c:44: if (keys & J_UP && player_y > 0) {
	bit	2, c
	jr	Z, 00108$
	ld	hl, #_player_y
	ld	a, (hl)
	or	a, a
	jr	Z, 00108$
;src/main.c:45: player_y -= 2;
	ld	a, (hl)
	add	a, #0xfe
	ld	(hl), a
;src/main.c:38: move_sprite(0, player_x, player_y);
	ld	e, (hl)
;src/main.c:46: move_sprite(0, player_y, player_y);
	ld	b, e
;/home/brennan/.local/gbdk/include/gb/gb.h:1973: OAM_item_t * itm = &shadow_OAM[nb];
	ld	hl, #_shadow_OAM
;/home/brennan/.local/gbdk/include/gb/gb.h:1974: itm->y=y, itm->x=x;
	ld	a, e
	ld	(hl+), a
	ld	(hl), b
;src/main.c:46: move_sprite(0, player_y, player_y);
00108$:
;src/main.c:48: if (keys & J_DOWN && player_y < 144) {
	bit	3, c
	jr	Z, 00114$
	ld	hl, #_player_y
	ld	a, (hl)
	sub	a, #0x90
	jr	NC, 00114$
;src/main.c:49: player_y += 2;
	ld	a, (hl)
	add	a, #0x02
	ld	(hl), a
;src/main.c:50: move_sprite(0, player_x, player_y);
	ld	b, (hl)
	ld	a, (_player_x)
	ld	c, a
;/home/brennan/.local/gbdk/include/gb/gb.h:1973: OAM_item_t * itm = &shadow_OAM[nb];
	ld	hl, #_shadow_OAM
;/home/brennan/.local/gbdk/include/gb/gb.h:1974: itm->y=y, itm->x=x;
	ld	a, b
	ld	(hl+), a
	ld	(hl), c
;src/main.c:54: if (player_x < 0) player_x = 0;
00114$:
;src/main.c:55: if (player_x > 160) player_x = 160;
	ld	a, #0xa0
	ld	hl, #_player_x
	sub	a, (hl)
	jr	NC, 00118$
	ld	(hl), #0xa0
;src/main.c:56: if (player_y < 0) player_y = 0;
00118$:
;src/main.c:57: if (player_y > 144) player_y = 144;
	ld	a, #0x90
	ld	hl, #_player_y
	sub	a, (hl)
	ret	NC
	ld	(hl), #0x90
;src/main.c:58: }
	ret
;src/main.c:60: void main(void) {
;	---------------------------------
; Function main
; ---------------------------------
_main::
;src/main.c:62: init_game();
	call	_init_game
;src/main.c:65: while (1) {
00102$:
;src/main.c:67: wait_vbl_done();
	call	_wait_vbl_done
;src/main.c:70: update_game();
	call	_update_game
;src/main.c:73: delay(50);
	ld	de, #0x0032
	call	_delay
;src/main.c:75: }
	jr	00102$
	.area _CODE
	.area _INITIALIZER
__xinit__player_x:
	.db #0x50	; 80	'P'
__xinit__player_y:
	.db #0x48	; 72	'H'
__xinit__game_state:
	.db #0x00	; 0
__xinit__player_sprite:
	.db #0x3c	; 60
	.db #0x3c	; 60
	.db #0x7e	; 126
	.db #0x7e	; 126
	.db #0xff	; 255
	.db #0xff	; 255
	.db #0x7e	; 126
	.db #0x3c	; 60
	.area _CABS (ABS)
