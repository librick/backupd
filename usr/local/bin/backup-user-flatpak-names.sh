#!/bin/bash
if [[ $EUID -eq 0 ]]; then
	echo "This script must NOT be run as root" 1>&2
	exit 1
fi

if [[ $EUID -ge 1000 ]]; then
	mkdir -p $XDG_CONFIG_HOME/backupd
	/usr/bin/flatpak list --app > $XDG_CONFIG_HOME/backupd/flatpaks.txt
fi

