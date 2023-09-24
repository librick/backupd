#!/bin/bash
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

/usr/bin/dpkg --list > /usr/local/share/backupd/apt-packages.txt
