# Power Center Extreme ⚡

Welcome to **Power Center Extreme**! This project provides a powerful, adaptive, and lightning-fast Terminal User Interface (TUI) to take absolute control of your computer's hardware power limits and performance.

Designed from the ground up to be lightweight, efficient, and heavily optimized, it completely removes the need for bloated graphical managers or slow Python scripts. We built this entirely in **Go (Golang)** for maximum efficiency.

## 🌟 Why Power Center Extreme?
- **Unleash or Constrain**: Push your CPU/GPU to absolute maximum performance, or cap it heavily to save incredible amounts of battery using our dedicated **Extreme Mode**.
- **Universal Adaptability**: Dynamically detects your system hardware limits (CPU cores, turbo boost, Intel RAPL package limits, GPU boundaries) and adapts the interface to precisely what your hardware supports.
- **Cross-Platform**: Designed for seamless hardware abstraction. Supports Linux out of the box with `sysfs` access. Future modules target seamless macOS and Windows capability.
- **Live Monitoring**: See your active battery drain (in Watts), charge state, and battery time left directly inside the TUI via a responsive ASCII bar graph.
- **Auto Daemon**: Set it and forget it. The daemon watches your battery state and seamlessly applies performance when plugged in, restores defaults when unplugged, and goes Extreme when battery drops below 20%.

## 🚀 Installation & Usage

### 1. Prerequisites
- [Go](https://golang.org/doc/install) 1.20 or higher.
- `root` or `sudo` privileges (required to write to hardware `/sys/` interfaces).

### 2. Build from Source
```bash
git clone https://github.com/Juan-Martin-Cerezo/power-center-extreme.git
cd power-center-extreme
go build -o power-center
```

### 3. Run
Because the program directly controls hardware boundaries, run it with `sudo`:
```bash
sudo ./power-center
```

**Run in Daemon Mode without UI:**
```bash
sudo ./power-center --daemon
```

## ⌨️ TUI Controls
- **Up/Down or W/S**: Navigate the menu options.
- **Left/Right or A/D**: Adjust the specific hardware limit/value (increase or decrease).
- **Enter**: Apply the highlighted mode (like Performance, Restore, Extreme).
- **+ / -**: Speed up or slow down the live power graph refresh rate.
- **R**: Hotkey to instantly restore system defaults.
- **Q / Esc**: Quit the application.

## 🤝 Open Source Culture
We strictly abide by modern, highly optimized open source engineering principles:
- **No bloat:** Zero tolerance for legacy Python or slow bridging scripts. Only native Go.
- **Adaptable UI:** The interface shifts layout depending on your terminal size (stacked vs side-by-side mode) and never overflows.
- **Self-Documenting:** Our entire codebase is heavily documented line-by-line. If you want to learn how hardware manipulation works, just read the code!
- **Contributions Welcome**: Found a bug or want to implement the macOS backend? We gladly accept PRs!

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
