# ⚡ Power Center Extreme

**Power Center Extreme** es una herramienta TUI (Terminal User Interface) y un demonio en segundo plano diseñado para el control total y la monitorización en vivo del consumo energético de tu computadora Linux. Fue construido pensando en portabilidad, eficiencia extrema, y adaptabilidad para cualquier distribución de Linux.

![Power Center Extreme](https://img.shields.io/badge/Linux-🐧-blue) ![Python](https://img.shields.io/badge/Python-3.x-green)

---

## 🌟 Características

* **Monitor de Energía en Vivo:** Visualiza en un gráfico dinámico (dibujado con braille) el historial de milivatios, además de los procesos más hambrientos y el porcentaje de batería en tiempo real.
* **Control Completo del Hardware:** Ajusta con las flechas del teclado los límites térmicos (PL1 y PL2 en Watts), el brillo máximo, y habilita/deshabilita componentes clave.
* **Compatibilidad Universal:** Funciona sin importar tu fabricante (Intel/AMD) ni modelo, auto-detectando rutas dinámicas en `/sys/` para el controlador RAPL, Turbo Boost, Backlight del teclado/pantalla, y Power Save de Audio.
* **Integración Opcional con Hyprland:** Si utilizas el gestor de ventanas Hyprland, `power-center` detectará tu monitor primario y ajustará la frecuencia de actualización (Hz) dinámicamente según el perfil elegido para ahorrar batería.
* **Modos Preconfigurados (Daemon):** Un clic para aplicar reglas del sistema, incluyendo modos como *Auto-Extreme*, *Performance* o *Extreme Battery*.

---

## ⚙️ Requisitos Previos

- Python 3.x
- Permisos de `sudo` (requerido únicamente para aplicar los perfiles de energía, ya que se modifican rutas de `/sys/`).
- Opcional pero recomendado: Estar bajo el entorno `Hyprland` y tener `brightnessctl` instalado.

---

## 🚀 Instalación (1 Comando)

Descarga el repositorio y ejecuta el script de instalación para alojarlo globalmente en tu sistema:

```bash
git clone https://github.com/Juan-Martin-Cerezo/power-center-extreme.git
cd power-center-extreme
sudo ./install.sh
```
*(Esto copiará el programa a tu `$PATH` como `power-center`)*

### Notas de Instalación Local
Si prefieres no instalarlo a nivel de todo el sistema operativo, puedes simplemente moverlo a tu directorio personal:
```bash
mkdir -p ~/.local/bin
cp power-center.py ~/.local/bin/power-center
chmod +x ~/.local/bin/power-center
```
*(Asegúrate de que `~/.local/bin` esté en tu variable `$PATH`)*

---

## 🎮 Cómo Usarlo

### 1. Interfaz de Monitorización TUI (Sin permisos especiales)
Puedes revisar el consumo energético actual o abrir la configuración sin aplicar comandos abriéndolo directamente:
```bash
power-center
```
* **Flechas `↑` `↓`**: Moverse por el panel principal.
* **Flechas `←` `→`**: Alterar valores numéricos de hardware (ej: límite de Watts).
* **`Tabulador`**: Cambiar entre el "Panel de Control" y el "Monitor de Energía (Gráfico)".
* **`Q`**: Salir de forma segura.

### 2. Panel de Control y Modos Especiales (Requiere `sudo`)
Para que los cambios de voltaje o de modos surtan efecto, necesitas privilegios de root:
```bash
sudo power-center
```
Selecciona el modo deseado dentro de la interfaz, presiona `ENTER`, y `power-center` ejecutará todos los ajustes de fondo.

### 3. Cambio de Modos Directo desde la Consola
Si quieres cambiar la configuración al instante (útil para alias o atajos de teclado de tu Window Manager), puedes enviar los comandos directamente:

* **Modo Ahorro Extremo:** 
  ```bash
  sudo power-center mode extreme
  ```
* **Modo Rendimiento Máximo:**
  ```bash
  sudo power-center mode performance
  ```
* **Modo Inteligente Automático:** Ajusta el rendimiento y el brillo dinámicamente según lo que estés haciendo.
  ```bash
  sudo power-center mode auto-extreme
  ```
* **Modo Restauración:**
  ```bash
  sudo power-center mode restore
  ```

### 4. Monitor Gráfico Exclusivo
Si tienes otra terminal abierta y solo quieres dejar el gráfico corriendo:
```bash
power-center --monitor
```

---

## 🛠️ Contribuciones y Hardware Especial
Dado que el programa ha sido refactorizado para utilizar `glob` para descubrir componentes de hardware, siéntete libre de abrir un **Pull Request** si notas que tu placa base o controlador en particular (`/sys/...`) no es detectado correctamente.
