#!/bin/bash
df -h
sudo pacman -Qdtq | sudo pacman -Rs -
sudo pacman -Scc --noconfirm
yay -Sc --noconfirm
df -h
