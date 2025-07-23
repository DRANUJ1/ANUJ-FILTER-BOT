#!/bin/bash

# Clone repo only if UPSTREAM_REPO is set
if [ -z "$UPSTREAM_REPO" ]; then
  echo "Cloning main Repository"
  git clone https://github.com/DRANUJ1/ANUJ-FILTER-BOT /Anuj-filter-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO"
  git clone "$UPSTREAM_REPO" /Anuj-filter-bot
fi

# Go to repo directory
cd /Anuj-filter-bot || exit

# Install dependencies
pip3 install -U -r requirements.txt

# Start bot
echo "Starting Anuj filter bot...."
python3 bot.py
