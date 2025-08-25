; Bridge file to connect C-compiled strings with assembly code
; This file imports symbols from the C-compiled object file

SECTION "Menu Strings Bridge", ROMX

; Import the C-compiled string data
extern new_game_text_data
extern new_game_text_length

; Export the label that the main menu expects
NewGameText::
    ; This will be replaced by the linker with the C-compiled data
    ; The linker will resolve new_game_text_data to the actual data
    ; and place it at the NewGameText label location
