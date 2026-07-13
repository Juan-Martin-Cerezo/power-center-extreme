# ⚡ VoltTamer (formerly Power Center Extreme)

**VoltTamer** is a highly efficient TUI (Terminal User Interface) and background daemon designed for total control and live monitoring of your Linux computer's energy consumption. Built with portability, extreme efficiency, and adaptability in mind, it's designed to work flawlessly across any Linux distribution and hardware setup.

![Linux](https://img.shields.io/badge/Linux-🐧-blue) ![Python](https://img.shields.io/badge/Python-3.x-green) ![Open Source](https://img.shields.io/badge/Open_Source-❤️-orange)

---

## 🌟 Key Features

* **Live Energy Monitor:** Visualize historical power consumption in milliwatts via an interactive braille graph, alongside real-time battery percentage and a live list of the most power-hungry processes.
* **Full Hardware Control:** Use your keyboard arrows to seamlessly tweak thermal limits (PL1 and PL2 in Watts), maximum screen brightness, and toggle key hardware components.
* **Universal Compatibility:** VoltTamer auto-detects dynamic paths in `/sys/` (using `glob`), making it inherently compatible with Intel, AMD, and various OEM backlight implementations (screen and keyboard).
* **Optional Hyprland Integration:** If you are running the Hyprland Wayland compositor, VoltTamer detects your primary monitor and scales the refresh rate (Hz) dynamically based on the active power profile.
* **Pre-configured Daemon Modes:** Instantly apply system-wide rules with a single click or command. Profiles include *Auto-Extreme*, *Performance*, and *Extreme Battery*.

---

## ⚙️ Prerequisites

- Python 3.x
- `sudo` privileges (required to apply power profiles, as it alters kernel `/sys/` parameters).
- *Optional but recommended:* Hyprland (for dynamic Hz scaling) and `brightnessctl` (for reliable screen brightness control fallback).

---

## 🚀 Installation (1-Command)

Clone the repository and run the installation script to make it globally available on your system:

```bash
git clone https://github.com/Juan-Martin-Cerezo/power-center-extreme.git
cd power-center-extreme
sudo ./install.sh
```
*(This will install the script to `/usr/local/bin/power-center` / `volt-tamer`)*

### Local Installation (No Root)
If you prefer not to install it globally, you can easily deploy it to your local user binary directory:
```bash
mkdir -p ~/.local/bin
cp power-center.py ~/.local/bin/power-center
chmod +x ~/.local/bin/power-center
```
*(Ensure `~/.local/bin` is added to your `$PATH`)*

---

## 🎮 How to Use

### 1. Interactive TUI Monitor (No special permissions needed)
You can check current energy consumption or browse hardware specs by launching the UI directly:
```bash
power-center
```
* **Arrows `↑` `↓`**: Navigate the main control panel.
* **Arrows `←` `→`**: Adjust hardware numerical values (e.g., Watt limits).
* **`Tab`**: Switch between the "Control Panel" and the "Live Energy Graph Monitor".
* **`Q`**: Exit safely.

### 2. Control Panel & Special Modes (Requires `sudo`)
For voltage limits and daemon modes to take effect, you must launch the TUI as root:
```bash
sudo power-center
```
Select your desired mode in the UI, press `ENTER`, and VoltTamer will apply the kernel tweaks in the background.

### 3. Headless CLI Control (Direct Commands)
If you want to map power modes to your Window Manager keybindings or run them from a shell script, you can trigger modes directly:

* **Extreme Battery Saver Mode:** Cuts resources aggressively for maximum battery life.
  ```bash
  sudo power-center mode extreme
  ```
* **Maximum Performance Mode:** Releases all hardware limits for gaming or compiling.
  ```bash
  sudo power-center mode performance
  ```
* **Auto-Extreme Mode:** Dynamically scales performance and brightness based on your real-time workload.
  ```bash
  sudo power-center mode auto-extreme
  ```
* **Restore Default State:**
  ```bash
  sudo power-center mode restore
  ```

### 4. Graph-Only View
Launch directly into the real-time consumption graph:
```bash
power-center --monitor
```

---

## 🤝 How to Contribute

We actively welcome contributions to make VoltTamer even more universal! Whether you're fixing a bug, adding support for a niche piece of hardware, or improving the UI, your help is appreciated.

### Contribution Guidelines:
1. **Fork the Repository:** Create a personal fork of the project on GitHub.
2. **Create a Branch:** Work your magic in a dedicated feature branch (`git checkout -b feature/amd-gpu-support`).
3. **Commit your Changes:** Write clear, concise commit messages.
4. **Test Thoroughly:** Ensure that your changes do not break compatibility with standard Intel/AMD hardware paths. Since VoltTamer uses generic `glob` lookups for `/sys/` paths, please try to maintain that philosophy instead of hardcoding OEM-specific strings.
5. **Open a Pull Request (PR):** Submit your PR against the `master` branch. Please include a description of the hardware you tested it on!

### Where we need help:
* Expanding CPU governor support (e.g., `amd_pstate_epp`).
* Adding dedicated GPU power limiting (NVIDIA/AMD).
* Translating the Python UI into English or supporting multi-language (i18n).
* Optimizing the Braille rendering engine for older terminal emulators.

---
*Created and maintained by Juan Martin Cerezo*
