// Pokemon base stats - C to assembly conversion
// This file defines Pokemon base stats that will be converted to RGBASM format

#include <stdint.h>

// Pokemon type constants (matching the assembly constants)
#define TYPE_NORMAL     0
#define TYPE_FIGHTING   1
#define TYPE_FLYING     2
#define TYPE_POISON     3
#define TYPE_GROUND     4
#define TYPE_ROCK       5
#define TYPE_BIRD       6
#define TYPE_BUG        7
#define TYPE_GHOST      8
#define TYPE_FIRE       20
#define TYPE_WATER      21
#define TYPE_GRASS      22
#define TYPE_ELECTRIC   23
#define TYPE_PSYCHIC    24
#define TYPE_ICE        25
#define TYPE_DRAGON     26

// Growth rate constants
#define GROWTH_MEDIUM_FAST  0
#define GROWTH_ERRATIC      1
#define GROWTH_FLUCTUATING  2
#define GROWTH_MEDIUM_SLOW  3
#define GROWTH_FAST         4
#define GROWTH_SLOW         5

// Pokemon base stats structure
typedef struct {
    uint8_t dex_id;
    uint8_t hp;
    uint8_t atk;
    uint8_t def;
    uint8_t spd;
    uint8_t spc;
    uint8_t type1;
    uint8_t type2;
    uint8_t catch_rate;
    uint8_t base_exp;
    uint8_t growth_rate;
} PokemonStats;

// Pikachu base stats (DEX_PIKACHU = 25)
const PokemonStats pikachu_stats = {
    .dex_id = 25,        // PIKACHU
    .hp = 60,
    .atk = 55,
    .def = 50,
    .spd = 90,
    .spc = 70,
    .type1 = TYPE_ELECTRIC,
    .type2 = TYPE_ELECTRIC,
    .catch_rate = 190,
    .base_exp = 82,
    .growth_rate = GROWTH_MEDIUM_FAST
};

// Pidgey base stats (DEX_PIDGEY = 24) - All stats set to 20 for testing
const PokemonStats pidgey_stats = {
    .dex_id = 24,        // PIDGEY
    .hp = 20,
    .atk = 20,
    .def = 20,
    .spd = 20,
    .spc = 20,
    .type1 = TYPE_NORMAL,
    .type2 = TYPE_FLYING,
    .catch_rate = 255,
    .base_exp = 55,
    .growth_rate = GROWTH_MEDIUM_SLOW
};

// Rattata base stats (DEX_RATTATA = 19) - All stats set to 20 for testing
const PokemonStats rattata_stats = {
    .dex_id = 19,        // RATTATA
    .hp = 20,
    .atk = 20,
    .def = 20,
    .spd = 20,
    .spc = 20,
    .type1 = TYPE_FLYING,
    .type2 = TYPE_FLYING,
    .catch_rate = 255,
    .base_exp = 57,
    .growth_rate = GROWTH_MEDIUM_FAST
};

// Export individual values for assembly linking - Pikachu
const uint8_t pikachu_dex_id = pikachu_stats.dex_id;
const uint8_t pikachu_hp = pikachu_stats.hp;
const uint8_t pikachu_atk = pikachu_stats.atk;
const uint8_t pikachu_def = pikachu_stats.def;
const uint8_t pikachu_spd = pikachu_stats.spd;
const uint8_t pikachu_spc = pikachu_stats.spc;
const uint8_t pikachu_type1 = pikachu_stats.type1;
const uint8_t pikachu_type2 = pikachu_stats.type2;
const uint8_t pikachu_catch_rate = pikachu_stats.catch_rate;
const uint8_t pikachu_base_exp = pikachu_stats.base_exp;
const uint8_t pikachu_growth_rate = pikachu_stats.growth_rate;

// Export individual values for assembly linking - Pidgey
const uint8_t pidgey_dex_id = pidgey_stats.dex_id;
const uint8_t pidgey_hp = pidgey_stats.hp;
const uint8_t pidgey_atk = pidgey_stats.atk;
const uint8_t pidgey_def = pidgey_stats.def;
const uint8_t pidgey_spd = pidgey_stats.spd;
const uint8_t pidgey_spc = pidgey_stats.spc;
const uint8_t pidgey_type1 = pidgey_stats.type1;
const uint8_t pidgey_type2 = pidgey_stats.type2;
const uint8_t pidgey_catch_rate = pidgey_stats.catch_rate;
const uint8_t pidgey_base_exp = pidgey_stats.base_exp;
const uint8_t pidgey_growth_rate = pidgey_stats.growth_rate;

// Export individual values for assembly linking - Rattata
const uint8_t rattata_dex_id = rattata_stats.dex_id;
const uint8_t rattata_hp = rattata_stats.hp;
const uint8_t rattata_atk = rattata_stats.atk;
const uint8_t rattata_def = rattata_stats.def;
const uint8_t rattata_spd = rattata_stats.spd;
const uint8_t rattata_spc = rattata_stats.spc;
const uint8_t rattata_type1 = rattata_stats.type1;
const uint8_t rattata_type2 = rattata_stats.type2;
const uint8_t rattata_catch_rate = rattata_stats.catch_rate;
const uint8_t rattata_base_exp = rattata_stats.base_exp;
const uint8_t rattata_growth_rate = rattata_stats.growth_rate;

// Export the lengths for assembly linking
const uint16_t pikachu_stats_size = sizeof(pikachu_stats);
const uint16_t pidgey_stats_size = sizeof(pidgey_stats);
const uint16_t rattata_stats_size = sizeof(rattata_stats);
