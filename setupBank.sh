#!/bin/bash

clear
pkg update && pkg upgrade
pkg install python3 -y
pip install colorama
gem install lolcat
pkg install cowsay
pkg install figlet

echo 'Installed Succesfully'

clear
