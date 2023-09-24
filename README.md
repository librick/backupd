# backupd
Bash scripts and systemd units for tracking installed packages on Linux.  

## Install
Read through `install.py` and the other files in this repo.  
When you're confident that you know what these files do, run `sudo ./install.py`.  

The installer script performs the following:  
- Adds scripts to `/usr/local/sbin/`
- Adds scripts to `/usr/local/bin/`
- Adds systemd units to `/etc/systemd/user/`
- Adds systemd units to `/etc/systemd/system/`

In general, the directory structure of this repo should 
directly reflect the directory structure of your system.

## Motivation
These scripts/services create text files in the following locations:
- `/usr/local/share/backups/*.txt`
- `$XDG_CONFIG_HOME/backups/*.txt`

E.g.,
- `/usr/local/share/backups/apt-packages.txt`
- `/usr/local/share/backups/flatpaks.txt`
- `~/.config/backups/flatpaks.txt`

Once these `*.txt` files are in place (and regularly updated via included systemd timers),
they can be tracked with dotfile tools and parsed to provision new machines.
This makes it easy to migrate system installs without the overhead of 
fully-declarative package managers (e.g., Nix).

## What Information is Tracked
These scripts/services track the following (non-exhaustive, read the code):
- Installed apt packages
- Installed flatpak system apps
- Installed flatpak user apps

