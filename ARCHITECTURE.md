# VoltTamer Architecture & Design Decisions

This document serves as a persistent record of the core design philosophies and engineering decisions made during the development of VoltTamer, specifically focusing on the `Auto Extreme` mode and hardware-agnostic capabilities.

## 1. Hardware-Agnostic Philosophy
- **Dynamic Bounds over Hardcoded Values:** The system must *never* rely on hardcoded hardware limits (e.g., assuming a CPU maxes at 4000MHz or minimums at 800MHz). 
- **Proportional Scaling:** Instead of setting fixed values, the program calculates the absolute minimum and maximum bounds of the specific machine it is running on (using `get_cpu_freq_bounds`, `get_gpu_bounds`, `get_num_cpus`, etc.) and scales proportionally based on load.

## 2. Auto Extreme Daemon - Core Mechanics
The `Auto Extreme` mode is designed to be the ultimate battery-saving daemon without starving the user of performance when needed.
- **Desensitization via `/proc/loadavg`:** To prevent the daemon from overreacting to micro-spikes (like opening a menu or compiling a single file), the daemon reads the 1-minute load average instead of instantaneous `/proc/stat`. This guarantees a "lazy" but deliberate scaling response.
- **Quantized Power Steps:** The power scaling is strictly forced into 4 distinct levels (0%, 33%, 66%, 100%). This eliminates the possibility of micro-fluctuations (e.g., shifting from 800MHz to 850MHz back and forth). Hardware states are only modified if the system crosses these massive statistical thresholds.
- **Fixed EPP in Auto Extreme:** Even under load, the Energy Performance Preference (EPP) is locked to `power` during Auto Extreme. This ensures the CPU's internal governor favors efficiency at all times, relying on our daemon to manually unlock cores and frequencies.
- **Focus-Aware Brightness:** Brightness is scaled proportionally (10% to 30%), but the upper bound is only permitted if a "heavy" UI application (like Chrome, VSCode, Firefox) is currently focused, detected natively via `Hyprland` or `xdotool`.

## 3. Zero-Overhead Execution
- **Native Python Writes:** The daemon completely avoids the use of `subprocess.run("echo ... > /sys/...")` or shell `for` loops. Creating subprocesses inside a tight loop causes severe CPU stress. Instead, VoltTamer uses native Python file I/O (`open().write()`) and `glob.glob()` to manipulate `/sys/` nodes. This results in virtually 0.00% CPU overhead during background monitoring and execution.
- **Environment Caching:** Checks that require subprocesses (like `pgrep` to check if Hyprland is running) are executed exactly once when the daemon starts and cached in memory to avoid repetitive CPU spikes.
- **Slow Polling:** The daemon sleeps for 10 seconds between checks. Combined with the 1-minute load average, the daemon is practically invisible to the CPU scheduler.

## 4. English Technical Standard
All documentation, UI elements (Curses), and comments within the source code must strictly use Technical English to maintain a professional, open-source standard for the global community.

---
*Persisted for future agent contexts.*
