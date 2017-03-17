# Makefile: Tools to help you install the OSC on MacOS/Ubuntu/Debian.
# Copyright © 2017 APARICIOs. All rights reserved.

### READ THIS ###
# Install necessary files, PyPi modules
install: pypi welcome

start: stop
	python main.py

stop:

run: start

### PyPi DEPENDENCIES ###
# Install PyPi dependencies.
pypi:
	pip install -r requirements.txt --user

### HELP ###
# Welcome and guide the user.
welcome:
	@echo
	@echo "OSC was successfully installed. Welcome!"
	@echo "You can now start it with:"
	@echo
	@echo "  python main.py"
	@echo

# This is a self-documented Makefile.
help:
	cat Makefile | less

.PHONY: install start stop run pypi welcome help
