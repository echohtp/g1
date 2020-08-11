sudo apt-get update -y 
sudo apt-get install git python3 python3-pip screen -y 
git clone https://github.com/echohtp/g1.git
cd g1
python3 -m pip install -r requirements.txt
screen run.sh

