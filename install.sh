#!/bin/bash

android_version=$(getprop ro.build.version.release)
version_number=${android_version%%.*}
clear

termux-setup-storage
apt update
apt upgrade -y

pkg install -y git python python-pip openjdk-17

pip install gdown licensing mysql-connector-python requests

git clone https://github.com/JINN1368/NgocRongTermux
echo "TIẾN HÀNH XOÁ TỆP THỪA"
sleep 2

cd NgocRongTermux
rm -rf *.md

if [ "$version_number" -gt 11 ]; then
    echo "CÀI ĐẶT SERVER"
    git clone https://github.com/1Tech-X/Tamp
    cd Tamp
    bash install.sh
    curl -LO https://raw.githubusercontent.com/1Tech-X/Tamp/main/update_tamp.sh
    bash update_tamp.sh
    curl -LO https://raw.githubusercontent.com/1Tech-X/Tamp/main/fix_phpmyadmin.sh
    bash fix_phpmyadmin.sh
    clear
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
else
    echo "ĐANG TẢI DỮ LIỆU"
    gdown --quiet 1T7uB5HdciSWAvxF9vP_f1wqZXfVz76tc
    unzip *.zip
    rm -rf *.zip
    cd
    cd NgocRongTermux
    mv *.sh ~/../usr/bin/
    chmod +x ~/../usr/bin/*.sh
    cd
    read -p "PHIÊN BẢN ANDROID CỦA BẠN KHÔNG HỖ TRỢ TAMPP, VUI LÒNG SETUP KSWEB."
    jinn1368.sh
fi

clear
