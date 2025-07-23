if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  https://github.com/DRANUJ1/ANUJ-FILTER-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Anuj-filter-bot
fi
cd /Edith-JFBdec
pip3 install -U -r requirements.txt
echo "Starting Anuj filter bot...."
python3 bot.py
