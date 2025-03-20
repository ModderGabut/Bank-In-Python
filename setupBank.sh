#!/bin/bash

clear
pkg update && pkg upgrade
pkg install python3 -y
pip install colorama

echo 'Installed Succesfully'

clear
