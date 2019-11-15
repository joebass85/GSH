#!/bin/bash

if [ ! -d ~/Desktop ]; then
    echo
    echo "Please create a Desktop folder in the home directory."
    echo
    exit
fi

sudo apt install python3-tk python3-pip
sudo pip3 install pyautogui
pushd ~
mkdir .gsh
cp ~/GSH/gsh.py ~/.gsh/gsh.py
pushd ~/Desktop
cp ~/GSH/icon.sh ~/Desktop/gsh.sh
popd
