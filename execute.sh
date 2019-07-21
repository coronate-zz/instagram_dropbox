
#!/usr/bin/env bash

source ./name_Env/bin/activate

echo "Connect to VPN"
nordvpn connect
echo "Connected"

echo "\n\nRUN python script"
cd instagram_dropbox
python3 filesystem_instagram_dropbox.py

#python3