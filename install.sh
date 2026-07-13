#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Por favor ejecuta la instalación como root (sudo ./install.sh)"
   exit 1
fi

echo "Instalando Power Center Extreme..."

cp power-center.py /usr/local/bin/power-center
chmod +x /usr/local/bin/power-center

echo "Instalación completada."
echo "Puedes ejecutar el programa simplemente escribiendo: power-center"
echo "Otras opciones:"
echo "  sudo power-center mode performance"
echo "  sudo power-center mode extreme"
echo "  sudo power-center mode auto-extreme"
echo "  sudo power-center mode restore"
