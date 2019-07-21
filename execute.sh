
#!/usr/bin/env bash

source ./name_Env/bin/activate

echo "Connect to VPN"
nordvpn connect
echo "Connected"

echo "\n\nRUN python script"
cd /home/alejandrocoronado/Dropbox/Github/instagram_autoai
venv/bin/filesystem_instagram_dropbox.py

#python3