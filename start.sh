#!/bin/bash
# cd /  <-- Is line ko hata dein ya comment kar dein

echo "Updating dependencies..."
pip3 install -U -r requirements.txt

echo "Starting Anuj filter bot...."
python3 bot.py
