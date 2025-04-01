#!/bin/bash
df -h
yay -Qdtq | yay -Rs - --noconfirm
yay -Scc --noconfirm
pacman -Scc --noconfirm
docker system prune -af
podman system prune --all --force && podman rmi --all
sudo trash-empty --all-users -f
npm cache clean --force
sudo journalctl --vacuum-time=1week
df -h
