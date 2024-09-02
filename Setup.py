#!/usr/bin/env python3
# TO START SETUP RUN THE FILE WITH THE TERMINAL IN THE SAME DIRECTORY AS Setup.py AND MPS FOLDER USING python3 Setup.py
from shutil import move
from os import getlogin
move('MPS',f'/home/{getlogin()}/.local/share/applications/')
fil=open(f'/home/{getlogin()}/.local/share/applications/MPS.desktop','w')
fil.write('[Desktop Entry]\nName=MountainProjectSearch\nType=Application\nTerminal=False\n')
fil.write(f'Icon=/home/{getlogin()}/.local/share/applications/MPS/MountainProject.png\nExec=/home/{getlogin()}/.local/share/applications/MPS/Search.pyw')
fil.close()
