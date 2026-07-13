# Power Center Extreme

Una herramienta definitiva para gestión y monitoreo de energía en Linux, especialmente diseñada para laptops y entornos como Hyprland. Unifica panel de control y monitorización en tiempo real.

## Características

- **Panel de control unificado (TUI)**
- **Monitor de consumo en vivo** con gráficos y listado de procesos
- **Regulación dinámica de cores y frecuencias**
- Modos preestablecidos:
  - **Performance:** Máximo rendimiento
  - **Extreme:** Máximo ahorro de batería fijo
  - **Auto Extreme:** Regulación inteligente según uso de CPU (Súper eficiente)
  - **Restore:** Restaura valores por defecto

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Otorga permisos de ejecución al instalador y ejecútalo como root:

```bash
sudo ./install.sh
```

## Uso

Para abrir el panel interactivo:
```bash
power-center
```
*(Puedes presionar la tecla Tabulador dentro del panel para alternar entre los controles de energía y el monitor en vivo)*

Para activar los modos directamente desde la terminal (requiere root):
```bash
sudo power-center mode performance
sudo power-center mode extreme
sudo power-center mode auto-extreme
sudo power-center mode restore
```

Para abrir el monitor en vivo directamente:
```bash
power-center --monitor
```
