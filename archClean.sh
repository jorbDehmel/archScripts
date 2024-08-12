#!/bin/bash
df -h
yay -Qdtq | yay -Rs -
yay -Scc --noconfirm
pacman -Scc
docker system prune -af
sudo trash-empty
npm cache clean --force
df -h
