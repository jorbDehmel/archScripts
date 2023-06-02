# Jordan Dehmel, jdehmel@outlook.com, 2023, github.com/jorbDehmel

# How to generate / update packages.txt:
# pacman -Qqe > packages.txt

echo "This script meant to install arch with my preferences."

sudo pacman --needed -Syu $(cat packages.txt) python git

# AUR packages
./aurman.py --clean write_stylus tlpui unityhub visual-studio-code-bin minecraft-launcher lammps google-chrome globus-connect-personal --clean --install

# Dirs
mkdir -p ~/Programs

# Start services
sudo systemctl enable tlp NetworkManager gdm
sudo systemctl start NetworkManager gdm

echo "It is probably a good idea to reboot now."
