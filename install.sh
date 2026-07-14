#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Please run the installation as root (sudo ./install.sh)"
   exit 1
fi

echo "Installing Power Center Extreme..."

echo "Disabling power managers that may cause conflicts (tlp, auto-cpufreq, etc.)..."
systemctl stop tlp auto-cpufreq power-profiles-daemon thermald system76-power 2>/dev/null
systemctl disable tlp auto-cpufreq power-profiles-daemon thermald system76-power 2>/dev/null

cp power-center.py /usr/local/bin/power-center
chmod +x /usr/local/bin/power-center

echo "Installation completed."
echo "You can run the program by simply typing: power-center"
echo "Other options:"
echo "  sudo power-center mode performance"
echo "  sudo power-center mode extreme"
echo "  sudo power-center mode auto-extreme"
echo "  sudo power-center mode restore"
