#!/bin/bash

termux-setup-storage
apt update
apt upgrade -y

pkg install -y git python python-pip openjdk-17

pip install gdown licensing mysql-connector-python requests

git clone https://github.com/JINN1368/NgocRongTermux
clear
echo "CÀI ĐẶT SERVER"
git clone https://github.com/1Tech-X/Tamp
cd Tamp
bash install.sh

echo "ĐANG TẢI DỮ LIỆU"
gdown --quiet 1T7uB5HdciSWAvxF9vP_f1wqZXfVz76tc
unzip *.zip
rm -rf *.zip
cd
cd NgocRongTermux
mv *.sh ~/../usr/bin/
chmod +x ~/../usr/bin/*.sh
cd
clear
jinn1368.sh
