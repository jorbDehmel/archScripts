#!/usr/bin/python

import sys
import os

if __name__ == '__main__':
    # Settings variables
    check_pacman: bool = False
    fail: bool = False
    
    # Stats variables
    ignored: int = 0
    main_repos: int = 0
    aur_repos: int = 0
    installed: int = 0

    # Check dependencies (pacman and git)
    if os.system('pacman --version > /dev/null && git --version > /dev/null') != 0:
        print('ERROR: Unmet software dependencies (git or pacman)')
        exit(4)

    # Initial setup
    os.system('mkdir -p ~/.aurman')

    if len(sys.argv) == 1:
        print('ERROR: Please supply at least one argument. (--help for a list)')
        exit(3)

    for pac in sys.argv[1:]:
        # Check for any setting arguments
        if pac == '--clean':
            print('Cleaning ~/.aurman')
            os.system('du -sh ~/.aurman ; rm -rf ~/.aurman/* ; du -sh ~/.aurman')
            continue
        elif pac == '--install':
            os.system('sudo cp aurman.py /usr/bin/aurman')
            print('Installed.')
            continue
        elif pac == '--pacman':
            check_pacman = True
            print('Enabled pre-aur pacman check.')
            continue
        elif pac == '--uninstall':
            os.system('sudo rm -rf /usr/bin/aurman ~/.aurman')
            print('Uninstalled.')
            continue
        elif pac == '--fail':
            print('All warnings will now be errors.')
            fail = True
            continue
        elif pac == '--help':
            print('aurman: an AUR package manager.')
            print('Options:')
            print('--clean cleans all existing aur files')
            print('--install instals aurman as an executable')
            print('--uninstall removes aurman as an executable')
            print('--pacman checks pacman for a package before AUR')
            print('--fail turns warnings into errors')
            print('--help lists this page')
            print('Otherwise, just list packages as arguments.')
            print('Jordan Dehmel, 2023, GPLv3, jdehmel@outlook.com')
            continue            

        # Check for already installed packages
        if os.system('pacman -Q ' + pac + ' > /dev/null') == 0:
            print('Package \'' + pac + '\' is already installed. Skipping.')
            ignored += 1
            continue

        # If enabled, check pacman before the AUR
        if check_pacman:
            pacman_result: int = os.system('sudo pacman -S --noconfirm ' + pac)

            if pacman_result == 0:
                print('Package was installed via pacman. Passing over AUR check.')
                main_repos += 1
                installed += 1
                continue
            else:
                print('Pacman check failed. Checking AUR.')

        # Try the AUR
        git_result: int = os.system('git clone https://aur.archlinux.org/' + pac + ' ~/.aurman/' + pac)

        '''
        # This section not very usable
        if git_result != 0:
            print('Could not find package \'' + pac + '\' on the AUR. Trying github...')
            git_result = os.system('git clone https://github.com/' + pac + ' ~/.aurman/' + pac)
        '''

        # Error handling for AUR packages
        if git_result != 0:
            print('WARNING: Package \'' + pac + '\' could not be cloned. Skipping.')

            if fail:
                exit(2)

            ignored += 1
            continue

        aur_repos += 1

        # Install cloned package using makepkg
        install_result: int = os.system('(cd ~/.aurman/' + pac + ' && pwd && makepkg -si)')

        # Error handling for install
        if install_result != 0:
            print('WARNING: Package \'' + pac + '\' had a non-zero installation status of '
                  + str(install_result))

            if fail:
                exit(1)

            ignored += 1
            continue

        installed += 1

    if installed != 0:
        print('Installed:\t' + str(installed))
    
    if ignored != 0:
        print('Ignored:\t' + str(ignored))
    
    if main_repos != 0:
        print('Main repos:\t' + str(main_repos))
    
    if aur_repos != 0:
        print('AUR repos:\t' + str(aur_repos))

    exit(0)
