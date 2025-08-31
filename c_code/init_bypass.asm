; Initialization Bypass Functions
SECTION "InitBypass", ROMX

; Function to bypass to after Pikachu has popped out of the Pokeball
; This skips all intro sequences, rival battle, rival exit, and Pikachu escape
; Player ends up in Oak's Lab with Pikachu following them
bypass_to_pikachu_following::
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
    ld a, 1
    ld [wOptionsInitialized], a
    
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
    
    ; Set up the destination map (Oak's Lab)
    ld a, OAKS_LAB
    ld [wDestinationMap], a
    
    ; Set up all the events that should have happened
    SetEvent EVENT_FOLLOWED_OAK_INTO_LAB
    SetEvent EVENT_FOLLOWED_OAK_INTO_LAB_2
    SetEvent EVENT_OAK_ASKED_TO_CHOOSE_MON
    SetEvent EVENT_GOT_STARTER
    SetEvent EVENT_BATTLED_RIVAL_IN_OAKS_LAB
    
    ; Set EVENT_OAK_APPEARED_IN_PALLET to make Oak visible in the lab
    SetEvent EVENT_OAK_APPEARED_IN_PALLET
    
    ; Set events for the starter balls and rival actions
    SetEvent EVENT_PALLET_AFTER_GETTING_POKEBALLS
    SetEvent EVENT_PALLET_AFTER_GETTING_POKEBALLS_2
    SetEvent EVENT_GOT_POKEBALLS_FROM_OAK
    
    ; Set up Pikachu as the starter
    ld a, STARTER_PIKACHU
    ld [wPlayerStarter], a
    
    ; Set up rival starter (assume player won the battle, so Vaporeon)
    ld a, RIVAL_STARTER_VAPOREON
    ld [wRivalStarter], a
    
    ; Use AddPartyMon function to properly create Pikachu
    ; Set up the prerequisites that AddPartyMon needs
    ld a, PIKACHU
    ld [wcf91], a  ; Pokemon ID to add
    
    ld a, 5
    ld [wCurEnemyLVL], a  ; Level for the Pokemon
    
    ld a, 0  ; Set to 0 for player party
    ld [wMonDataLocation], a
    
    ; Initialize party count to 0 before adding
    xor a
    ld [wPartyCount], a
    
    ; Call AddPartyMon to properly create Pikachu
    call AddPartyMon
    
    ; Ensure party count is set to 1 after adding
    ld a, 1
    ld [wPartyCount], a
    
    ; Set Pikachu's nickname to "PIKACHU" after it's added
    ; This ensures the nickname is set even if the prompt was shown
    ld hl, wPartyMon1Nick
    ld a, "P"
    ld [hli], a
    ld a, "I"
    ld [hli], a
    ld a, "K"
    ld [hli], a
    ld a, "A"
    ld [hli], a
    ld a, "C"
    ld [hli], a
    ld a, "H"
    ld [hli], a
    ld a, "U"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    
    ; Set OT name to "TESTER"
    ld hl, wPartyMon1OT
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
    
    ; Set Pikachu's nickname to "PIKACHU"
    ld hl, wPartyMon1Nick
    ld a, "P"
    ld [hli], a
    ld a, "I"
    ld [hli], a
    ld a, "K"
    ld [hli], a
    ld a, "A"
    ld [hli], a
    ld a, "C"
    ld [hli], a
    ld a, "H"
    ld [hli], a
    ld a, "U"
    ld [hli], a
    ld a, "@"  ; String terminator
    ld [hli], a
    
    ; Set Pikachu's special properties
    ld a, LIGHT_BALL_GSC
    ld [wPartyMon1CatchRate], a
    
    ; Set up Pikachu happiness and mood
    ld a, 90 ; initialize happiness to 90
    ld [wPikachuHappiness], a
    ld a, $80
    ld [wPikachuMood], a ; initialize mood
    
    ; Set up Pikachu spawn state (following player)
    ld a, $2
    ld [wPikachuSpawnState], a
    
    ; Set up game progress flags
    ld hl, wd72e
    set 3, [hl]
    
    ; Test our money management system by setting starting money to $10,000 (final correct version)
    call _give_ten_thousand_final
    
    ; Set wOakWalkedToPlayer to 2 to indicate the intro sequence is complete
    ; This prevents Oak from showing the "Hey! Wait! Don't go out!" warning
    ld a, 2
    ld [wOakWalkedToPlayer], a
    
    ; Set up Oak's Lab script state to be at the final NOOP (script 18)
    ; This comes after the Pokedex sequence is completely finished
    ; and is completely independent from all progression chains
    ld a, 18  ; Final SCRIPT_OAKSLAB_NOOP (after Pokedex sequence)
    ld [wOaksLabCurScript], a
    ld [wCurMapScript], a
    
    ; Explicitly clear wJoyIgnore to ensure player input is enabled
    ; This prevents any remaining battle sequences from blocking input
    xor a
    ld [wJoyIgnore], a
    
    ; Set all the event flags that would normally be set during the Pokedex sequence
    ; This ensures the game thinks we've completed the full Oak's Lab story
    SetEvent EVENT_GOT_POKEDEX
    SetEvent EVENT_OAK_GOT_PARCEL
    SetEvent EVENT_1ST_ROUTE22_RIVAL_BATTLE
    SetEvent EVENT_ROUTE22_RIVAL_WANTS_BATTLE
    
    ; Set events that enable wild Pokemon encounters
    SetEvent EVENT_COMPLETED_CATCH_TRAINING_AGAIN
    SetEvent EVENT_INITIAL_CATCH_TRAINING
    
    ; Initialize the bag properly (InitPlayerData2 doesn't do this completely)
    ; The bag structure is BAG_ITEM_CAPACITY * 2 + 1 bytes
    ; Each item takes 2 bytes (ID + quantity) plus a terminator
    xor a
    ld [wNumBagItems], a
    ld hl, wBagItems
    ld bc, BAG_ITEM_CAPACITY * 2 + 1
    ld a, $ff  ; Fill with terminators
    call FillMemory
    
    ; Give the player Pokeballs (normally given during Oak's Lab sequence)
    ld hl, wNumBagItems  ; Point to the bag inventory
    ld a, POKE_BALL
    ld [wcf91], a
    ld a, 5
    ld [wItemQuantity], a
    call AddItemToInventory
    
    ; Set up player sprite data
    xor a
    ldh [hTileAnimations], a
    ld a, PLAYER_DIR_UP
    ld [wPlayerMovingDirection], a
    ld c, 20
    call DelayFrames
    
    ; Ensure proper object visibility for Oak's Lab
    ; Hide the starter balls since rival took them
    ld a, HS_STARTER_BALL_1
    ld [wMissableObjectIndex], a
    predef HideObject
    
    ; Hide the Pokedex objects since we already have them
    ld a, HS_POKEDEX_1
    ld [wMissableObjectIndex], a
    predef HideObject
    
    ld a, HS_POKEDEX_2
    ld [wMissableObjectIndex], a
    predef HideObject
    
    ; Show Oak in the lab (in his final position)
    ld a, HS_OAKS_LAB_OAK_1
    ld [wMissableObjectIndex], a
    predef ShowObject
    
    ; Hide the rival since they've left
    ld a, HS_OAKS_LAB_RIVAL
    ld [wMissableObjectIndex], a
    predef HideObject
    
    ; Call PrepareForSpecialWarp to set up the warp data properly
    call PrepareForSpecialWarp
    
    ; Jump directly to SpecialEnterMap, which will put us in Oak's Lab
    jp SpecialEnterMap
