#!/bin/bash

if ! [ -x "$(command -v sed)" ]; then
  sudo apt -y update
  sudo apt install wifite
fi

echo -n "Would you specify a WPA crack list (name/n)?"
read -r answer

if [ "$answer" = "n" ]; then
  sudo wifite
  sudo airmon-ng stop wlan0mon
  sudo service NetworkManager start
else
  sudo wifite --wpa --dict "$answer" --kill
  sudo airmon-ng stop wlan0mon
  sudo service NetworkManager start
fi