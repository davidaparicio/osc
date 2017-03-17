# Makefile: Tools to help you install the OSC on MacOS/Ubuntu/Debian.
# Copyright © 2017 APARICIOs. All rights reserved.
# The following code is covered by the AGPL-3.0 license.

### READ THIS ###

# Install necessary files, npm modules, and certificates.
install: pypi welcome

start: stop
	python main.py
	#node app >> janitor.log 2>&1 & [ $$! -ne "0" ] && printf "$$!\n" > janitor.pid

stop:


### PyPi DEPENDENCIES ###
# Install PyPi dependencies.
pypi:
	pip install -r requirements.txt

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

.PHONY: install start stop welcome help
