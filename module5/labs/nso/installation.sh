#!/usr/bin/env bash

sudo apt-get install -y openjdk-17-jre-headless
sudo sh nso-5.5.2.1.linux.x86_64.installer.bin --system-install
sudo groupadd ncsadmin
sudo groupadd ncsoper
sudo usermod -a -G ncsadmin osboxes
sudo chmod 777 -R /var/opt/ncs
cd neds
cp -r cisco-ios-cli-6.74/ cisco-iosxr-nc-7.3/ cisco-iosxr-cli-7.33/ /var/opt/ncs/packages

#sudo -s
#source /etc/profile.d/ncs.sh
#source /opt/ncs/ncs-5.5.2.1/ncsrc
#/etc/init.d/ncs start