
termux-setup-storage
apt update
apt upgrade -y

pkg install -y git python python-pip openjdk-17

pip install gdown licensing mysql-connector-python requests

git clone https://github.com/JINN1368/NgocRongTermux
git clone https://github.com/1Tech-X/Tamp
cd Tamp
bash install.sh
curl -LO https://raw.githubusercontent.com/1Tech-X/Tamp/main/update_tamp.sh
bash update_tamp.sh
curl -LO https://raw.githubusercontent.com/1Tech-X/Tamp/main/fix_phpmyadmin.sh
bash fix_phpmyadmin.sh
clear

cd
cd NgocRongTermux 
echo "ĐANG TẢI DỮ LIỆU"
gdown --quiet 1T7uB5HdciSWAvxF9vP_f1wqZXfVz76tc
unzip *.zip
rm -rf *.zip
mv *.sh ~/../usr/bin/
chmod +x ~/../usr/bin/*.sh
cd
clear
jinn1368.sh
