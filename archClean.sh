#!/bin/bash
df -h
yay -Qdtq | yay -Rs -
yay -Scc --noconfirm
docker system prune -af
df -h
