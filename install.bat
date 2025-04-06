@echo off

choco install -y python3 7z wget

wget https://github.com/libusb/libusb/releases/download/v1.0.28/libusb-1.0.28.7z -O libusb.7z
7z x libusb.7z -olibusb
xcopy /Y libusb\MS64\dll\libusb-1.0.dll C:\Windows\System32

wget https://github.com/pbatard/libwdi/releases/download/v1.5.1/zadig-2.9.exe -O zadig.exe

py -m venv env
call .\env\Scripts\activate.bat
pip install -r requirements.txt

echo Done!