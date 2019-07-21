
#!/usr/bin/env bash

pip install -r requirements.txt 
#InstagramAPI
pip install git+git://github.com/coronate/Instagram-API-python.git

#NordVPN install
sudo apt install wget apt-transport-https
wget --directory-prefix /tmp https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
sudo apt install /tmp/nordvpn-release_1.0.0_all.deb
sudo apt-get update

python3 filesystem_instagram_dropbox.py

