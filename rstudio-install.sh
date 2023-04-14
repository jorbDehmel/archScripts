git clone https://aur.archlinux.org/rstudio-desktop-bin.git
cd rstudio-desktop-bin
makepkg -si
sudo pacman -Syu texlive-most
echo "alias rstudio='/usr/lib/rstudio/rstudio &'" >> ~/.bashrc
