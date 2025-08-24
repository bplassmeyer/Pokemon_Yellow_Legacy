# GBDK Makefile for Pokemon-like Game
# Using the working template approach for Game Boy Color

# GBDK home directory - use the new GBDK 4.1.1 installation
GBDK_HOME = /opt/gbdk

# Compiler
LCC = $(GBDK_HOME)/bin/lcc

# Project name
PROJECTNAME = pokemon_game

# Output files - now Game Boy Color
BINS = $(PROJECTNAME).gbc

# Source files
CSOURCES := $(wildcard src/*.c)

# Compiler flags for Game Boy Color - using the correct flag from Google search
LCCFLAGS = -Wm-yC

# Debug mode (uncomment to enable)
# GBDK_DEBUG = ON
ifdef GBDK_DEBUG
    LCCFLAGS += -debug -v
endif

# Default target
all: $(BINS)

# Compile and link all source files in a single call to LCC
$(BINS): $(CSOURCES)
	$(LCC) $(LCCFLAGS) -o $@ $(CSOURCES)

# Clean build files
clean:
	rm -f *.o *.lst *.map *.gb *.gbc *.ihx *.sym *.cdb *.adb *.asm *.noi *.rst
	rm -f src/*.lst src/*.sym

# Test GBDK installation
test-gbdk:
	@echo "Testing GBDK installation..."
	@echo "GBDK_HOME: $(GBDK_HOME)"
	@echo "LCC: $(LCC)"
	@$(LCC) --version || echo "GBDK compiler not working"

# Help target
help:
	@echo "Available targets:"
	@echo "  all        - Build the GBC ROM"
	@echo "  clean      - Remove build files"
	@echo "  test-gbdk  - Test GBDK installation"
	@echo "  help       - Show this help"

.PHONY: all clean test-gbdk help
