#!/bin/bash

rm -rf build
rm -rf dist
sudo apt install python3-scapy
pip3 install pyinstaller

python3 -m PyInstaller --onefile ktotu.py
python3 -m PyInstaller --onefile mac_addresses_scanner.py
python3 -m PyInstaller --onefile install.py