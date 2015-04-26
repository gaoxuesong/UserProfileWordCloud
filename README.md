User Profile Word Cloud -- UPWC
==========
Creates user profile by word cloud generator (https://github.com/amueller/word_cloud) in Python.


On Ubuntu 14.04
## Preinstallation
sudo apt-get update

sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git

sudo apt-get install libgtk2.0-dev

sudo apt-get install glade

## installation freetype
wget http://download.savannah.gnu.org/releases/freetype/freetype-2.4.10.tar.gz

tar zxvf freetype-2.4.10.tar.gz

cd freetype-2.4.10/

mkdir /usr/local/freetype

 ./configure --prefix=/usr/local/freetype
 
make 

make install

## installation libpng
sudo apt-get install zlib1g-dev

wget http://prdownloads.sourceforge.net/libpng/libpng-1.6.17.tar.gz?download

tar xzf libpng-1.6.17.tar.gz

cd libpng-1.6.17

mkdir /usr/local/libpng

./configure --prefix=/usr/local/libpng

make 

make install

## add requirements via pip
sudo pip install Theano

sudo pip install Cython

sudo pip install Django

sudo pip install Image

sudo pip install imgurpython

sudo pip install matplotlib

sudo pip install oauthlib

sudo pip install Pillow

sudo pip install pyparsing

sudo pip install python-dateutil

sudo pip install pytz

sudo pip install requests

sudo pip install requests-oauthlib

sudo pip install six

sudo pip install scikit-image


sudo pip install git+git://github.com/gaoxuesong/word_cloud.git

## Installation UPWC
git clone https://github.com/gaoxuesong/UserPorfileWordCloud.git 

cd UserProfileWordCloud

## set FONT_PATH
### Add FONT_PATH in /etc/profile
vi /etc/profile
#### For Ubuntu 12.04
FONT_PATH=/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf

#### For Ubuntu 14.04
FONT_PATH=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf

export FONT_PATH

### source /etc/profile
source /etc/profile

echo $FONT_PATH

## Running
python userprofile.py

[website]: http://amueller.github.io/word_cloud/
