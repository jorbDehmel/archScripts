#!/usr/bin/python

import sys
import os

if __name__ == '__main__':
    os.system('mkdir -p ~/.aurman')

    if len(sys.argv) == 1:
        print('ERROR: Please supply at least one argument. (--help for a list)')

    for pac in sys.argv[1:]:
        if pac == '--clean':
            print('Cleaning ~/.aurman')
            os.system('du -sh ~/.aurman')
            os.system('rm -rf ~/.aurman/*')
            continue
        elif pac == '--install':
            os.system('sudo cp aurman.py /usr/bin/aurman')
            print('Installed.')
            continue
        elif pac == '--uninstall':
            os.system('sudo rm -rf /usr/bin/aurman ~/.aurman')
            print('Uninstalled.')
            continue
        elif pac == '--help':
            print('aurman: an AUR package manager.')
            print('Options:')
            print('--clean cleans all existing aur files')
            print('--install instals aurman as an executable')
            print('--uninstall removes aurman as an executable')
            print('--help lists this page')
            print('Otherwise, just list packages as arguments.')
            print('Jordan Dehmel, 2023, GPLv3, jdehmel@outlook.com')

        if os.system('pacman -Q ' + pac) == 0:
            print('Package \'' + pac + '\' is already installed. Skipping.')
            continue

        git_result: int = os.system('git clone https://aur.archlinux.org/' + pac + ' ~/.aurman/' + pac)

        if git_result != 0:
            print('Could not find package \'' + pac + '\' on the AUR. Trying github...')
            git_result = os.system('git clone https://github.com/' + pac + ' ~/.aurman/' + pac)

        if git_result != 0:
            print('WARNING: Package \'' + pac + '\' could not be cloned. Skipping.')
            continue

        install_result: int = os.system('(cd ~/.aurman/' + pac + ' && pwd && makepkg -si)')

        if install_result != 0:
            print('WARNING: Package \'' + pac + '\' had a non-zero installation status of '
                  + str(install_result))
