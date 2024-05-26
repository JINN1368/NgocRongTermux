#!/bin/bash

# Retrieve Android version and clear terminal
android_version=$(getprop ro.build.version.release)
version_number=${android_version%%.*}
clear

# Setup Termux storage and update system
termux-setup-storage
apt update && apt upgrade -y

# Install required packages
pkg install -y git python python-pip openjdk-17
pip install gdown licensing mysql-connector-python requests

# Clone the NgocRongTermux repository
git clone https://github.com/JINN1368/NgocRongTermux

# Remove unnecessary files
echo "TIẾN HÀNH XOÁ TỆP THỪA"
sleep 2
cd NgocRongTermux
rm -rf *.md

# Download and set up the environment based on Android version
if [ "$version_number" -gt 11 ]; then
    echo "CÀI ĐẶT SERVER"
    
    # Clone and install Tamp
    cd ~
    git clone https://github.com/1Tech-X/Tamp
    cd Tamp
    
    # Run installation scripts with error handling
    bash install.sh || { echo "Install script failed"; exit 1; }
    curl -LO https://raw.githubusercontent.com/1Tech-X/Tamp/main/update_tamp.sh
    bash update_tamp.sh || { echo "Update script failed"; exit 1; }
    curl -LO https://raw.githubusercontent.com/1Tech-X/Tamp/main/fix_phpmyadmin.sh
    bash fix_phpmyadmin.sh || { echo "Fix phpMyAdmin script failed"; exit 1; }

    clear
    echo "ĐANG TẢI DỮ LIỆU"
    
    # Download and unzip data
    gdown --quiet 1T7uB5HdciSWAvxF9vP_f1wqZXfVz76tc
    unzip -q '*.zip'
    rm -rf *.zip
    
    # Move scripts to /usr/bin
    cd ~/NgocRongTermux
    mv *.sh ~/../usr/bin/
    chmod +x ~/../usr/bin/*.sh
    
    clear
    jinn1368.sh

else
    echo "ĐANG TẢI DỮ LIỆU"
    
    # Download and unzip data
    gdown --quiet 1T7uB5HdciSWAvxF9vP_f1wqZXfVz76tc
    unzip -q '*.zip'
    rm -rf *.zip
    
    # Move scripts to /usr/bin
    cd ~/NgocRongTermux
    mv *.sh ~/../usr/bin/
    chmod +x ~/../usr/bin/*.sh
    
    echo "PHIÊN BẢN ANDROID CỦA BẠN KHÔNG HỖ TRỢ TAMPP, VUI LÒNG SETUP KSWEB."
    jinn1368.sh
fi

clear
