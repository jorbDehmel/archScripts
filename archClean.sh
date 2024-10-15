#!/bin/bash
df -h
yay -Qdtq | yay -Rs - --noconfirm
yay -Scc --noconfirm
pacman -Scc --noconfirm
docker system prune -af
sudo trash-empty --all-users -f
npm cache clean --force
df -h
