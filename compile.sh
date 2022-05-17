#!/bin/bash

# rm -rf ./exe
# mkdir ./exe
# cd ./exe
# chmod 755 ../words.txt


# pyinstaller.exe --clean --onefile --icon=../jg.ico -n JumbleGame --add-data="../words.txt;."  --windowed ../app.py

pyinstaller.exe JumbleGame.spec