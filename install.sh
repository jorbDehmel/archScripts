# Jordan Dehmel, jdehmel@outlook.com, 2023, github.com/jorbDehmel

# How to generate / update packages.txt:
# pacman -Qqe > packages.txt

echo "This script meant to install arch with my preferences."

sudo pacman --needed -Syu python git

# AUR packages
./aurman.py --pacman --clean $(cat packages.txt) --clean --install

# Dirs
mkdir -p ~/Programs

# Start services
sudo systemctl enable tlp NetworkManager gdm
sudo systemctl start NetworkManager gdm

echo "It is probably a good idea to reboot now."
