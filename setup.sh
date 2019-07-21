
#!/usr/bin/env bash
sudo apt-get install python3-pip
pip install -r requirements.txt 
#InstagramAPI
pip install git+git://github.com/coronate/Instagram-API-python.git

#NordVPN install
sudo apt install wget apt-transport-https
wget --directory-prefix /tmp https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
sudo apt-get install /tmp/nordvpn-release_1.0.0_all.deb
sudo apt-get update
sudo apt-get install nordvpn
sudo apt-get update

nordvpn login
