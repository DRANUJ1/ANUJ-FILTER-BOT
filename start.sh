#!/bin/bash

# Go to repo directory
cd /Anuj-filter-bot || exit

# Install dependencies
pip3 install -U -r requirements.txt

# Start bot
echo "Starting Anuj filter bot...."
python3 bot.py
