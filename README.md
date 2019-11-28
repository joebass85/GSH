# GSH - A GUI ssh frontend
This is a graphical front-end to the openSSH protocol.
GSH seeks to provide an easy-to-use graphical user interface for openSSH.

You must provide a password in the terminal, if necessary according to your ssh config.


## This program depends on:
```
  ---------------------
  | subprocess module |
  ---------------------
  | time module       |
  ---------------------
  | Tkinter module    |
  ---------------------
  | pyautogui module  |
  ---------------------  
```  
GSH can be run from the terminal with the command `python3 gsh.py`,
run from a keybinding, or launched from the gsh.sh icon on the Desktop (if you have an
active desktop).

To run the install script, cd into the GSH directory, 
change the permissions on the setup.sh script to allow it to be executable,
and then run the command `./setup-arch.sh` or `./setup-ubuntu.sh`
to install the program.

`Note:`
The scripts are distro-specific, working for any Arch-based or
Debian/Ubuntu-based distros.
