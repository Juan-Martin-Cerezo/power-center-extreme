import re

with open("power-center.py", "r") as f:
    content = f.read()

# I will replace the OPTIONS list and the draw_view_menu with the grouped layout
new_options = """OPTIONS = [
    {
        "category": "CPU & COMPUTE",
        "name": "Active Cores",
        "type": "value",
        "get": lambda: get_cores(),
        "set": lambda v, d: set_cores(v + d),
        "desc": "Limiting cores saves a lot of battery but reduces multitasking performance.",
        "safety": "SAFE"
    },
    {
        "category": "CPU & COMPUTE",
        "name": "CPU Freq (MHz)",
        "type": "value",
        "get": lambda: get_freq_limit(),
        "set": lambda v, d: set_freq_limit(v + (d * 100)),
        "desc": "Maximum processor frequency. A low value (e.g., 1400) saves a lot of energy.",
        "safety": "SAFE"
    },
    {
        "category": "CPU & COMPUTE",
        "name": "Energy Perf Pref",
        "type": "value",
        "get": lambda: get_epp(),
        "set": lambda v, d: set_epp(EPP_PREFERENCES[(EPP_PREFERENCES.index(v) + d) % len(EPP_PREFERENCES)]),
        "desc": "Energy Performance Preference (EPP). 'power' forces the processor to be as efficient as possible.",
        "safety": "SAFE"
    },
    {
        "category": "POWER LIMITS",
        "name": "RAPL PL1 (W)",
        "type": "value",
        "get": lambda: get_rapl_pl1(),
        "set": lambda v, d: set_rapl_pl1(v + d),
        "desc": "Sustained power limit (PL1).",
        "safety": "SAFE"
    },
    {
        "category": "POWER LIMITS",
        "name": "RAPL PL2 (W)",
        "type": "value",
        "get": lambda: get_rapl_pl2(),
        "set": lambda v, d: set_rapl_pl2(v + d),
        "desc": "Turbo power limit (PL2). Restricting it prevents massive heat spikes.",
        "safety": "SAFE"
    },
    {
        "category": "POWER LIMITS",
        "name": "PCIe ASPM Policy",
        "type": "value",
        "get": lambda: get_aspm_policy(),
        "set": lambda v, d: set_aspm_policy(ASPM_POLICIES[(ASPM_POLICIES.index(v) + d) % len(ASPM_POLICIES)]),
        "desc": "PCIe Active State Power Management. 'powersupersave' saves more energy.",
        "safety": "SAFE"
    },
    {
        "category": "CPU & COMPUTE",
        "name": "Turbo Boost",
        "type": "toggle",
        "get": lambda: _get_turbo(),
        "set": lambda s: _set_turbo(s),
        "desc": "Disabling Turbo prevents heat spikes and massive instantaneous power consumption.",
        "safety": "WARN"
    },
    {
        "category": "GPU & DISPLAY",
        "name": "Freq iGPU (MHz)",
        "type": "value",
        "get": lambda: get_gpu_limit(),
        "set": lambda v, d: set_gpu_limit(v + (d * 50)),
        "desc": "Integrated graphics limit. Reducing it saves energy.",
        "safety": "SAFE"
    },
    {
        "category": "GPU & DISPLAY",
        "name": "LCD Brightness (%)",
        "type": "value",
        "get": lambda: int((int(run("brightnessctl g"))/int(run("brightnessctl m")))*100) if run("brightnessctl m") else 0,
        "set": lambda v, d: subprocess.run(f"brightnessctl s {5 if d > 0 else -5}%", shell=True),
        "desc": "The panel is the biggest consumer after the CPU. Keep under 10%.",
        "safety": "SAFE"
    },
    {
        "category": "RADIOS & PERIPHERALS",
        "name": "Keyboard Light",
        "type": "toggle",
        "get": lambda: get_kbd_backlight(),
        "set": lambda s: set_kbd_backlight(s),
        "desc": "Turning off keyboard backlight saves a small fraction of a watt.",
        "safety": "SAFE"
    },
    {
        "category": "GPU & DISPLAY",
        "name": "Hyprland Effects",
        "type": "toggle",
        "get": lambda: get_hypr_animations(),
        "set": lambda s: set_hypr_effects(s),
        "desc": "Disabling animations and blur frees the GPU from unnecessary work.",
        "safety": "SAFE"
    },
    {
        "category": "HARDWARE & RADIOS",
        "name": "Bluetooth",
        "type": "toggle",
        "get": lambda: "Soft blocked: no" in run("rfkill list bluetooth"),
        "set": lambda s: subprocess.run(f"rfkill {'unblock' if s else 'block'} bluetooth", shell=True),
        "desc": "Bluetooth radio cutoff. Prevents the chip from searching for devices.",
        "safety": "SAFE"
    },
    {
        "category": "HARDWARE & RADIOS",
        "name": "WiFi Enable",
        "type": "toggle",
        "get": lambda: "Soft blocked: no" in run("rfkill list wifi"),
        "set": lambda s: subprocess.run(f"rfkill {'unblock' if s else 'block'} wifi", shell=True),
        "desc": "Toggle WiFi radio (rfkill). Disable to save constant radio polling energy.",
        "safety": "SAFE"
    },
    {
        "category": "HARDWARE & RADIOS",
        "name": "WiFi Power Save",
        "type": "toggle",
        "get": lambda: get_wifi_powersave(),
        "set": lambda s: set_wifi_powersave(s),
        "desc": "Activates WiFi card power save mode. Reduces consumption but may increase latency.",
        "safety": "SAFE"
    },
    {
        "category": "HARDWARE & RADIOS",
        "name": "Audio Power Save",
        "type": "toggle",
        "get": lambda: _get_audio_powersave(),
        "set": lambda s: _set_audio_powersave(s),
        "desc": "Suspends audio chip after 1s of inactivity. Prevents static 'pop'.",
        "safety": "SAFE"
    },
    {
        "category": "SYSTEM ACTIONS",
        "name": "Autosuspend PCI/USB",
        "type": "toggle",
        "get": lambda: "auto" in run("cat /sys/bus/pci/devices/*/power/control 2>/dev/null | head -n 1"),
        "set": lambda s: [set_sys_val(p, "auto" if s else "on") for p in glob.glob("/sys/bus/pci/devices/*/power/control")] + [set_sys_val(p, "auto" if s else "on") for p in glob.glob("/sys/bus/usb/devices/*/power/control")],
        "desc": "Suspends inactive USB ports and PCIe lanes. May affect peripherals.",
        "safety": "DANGER"
    },
    {
        "category": "SYSTEM ACTIONS",
        "name": "Watchdog Kernel",
        "type": "toggle",
        "get": lambda: get_sys_val("/proc/sys/kernel/nmi_watchdog") == "1",
        "set": lambda s: set_sys_val("/proc/sys/kernel/nmi_watchdog", "1" if s else "0"),
        "desc": "Disable kernel security interrupts. Reduces CPU wakeups.",
        "safety": "WARN"
    },
    {
        "category": "SYSTEM ACTIONS",
        "name": "VM Writeback (s)",
        "type": "value",
        "get": lambda: int(get_sys_val("/proc/sys/vm/dirty_writeback_centisecs") or 500) // 100,
        "set": lambda v, d: [set_sys_val("/proc/sys/vm/dirty_writeback_centisecs", max(1, v + d) * 100), set_sys_val("/proc/sys/vm/dirty_expire_centisecs", max(1, v + d) * 100)],
        "desc": "Virtual disk save interval. High values reduce SSD usage.",
        "safety": "WARN"
    },
    {
        "category": "SYSTEM ACTIONS",
        "name": "Process Purge",
        "type": "action",
        "exec": lambda: subprocess.run("pkill -f 'brave|discord|telegram|code|electron'", shell=True),
        "desc": "Closes heavy applications (Brave, Code, Discord, etc) to free RAM and CPU.",
        "safety": "DANGER"
    },
    {
        "category": "POWER PROFILES",
        "name": "⚡ PERFORMANCE MODE",
        "type": "action",
        "exec": apply_mode_performance,
        "desc": "TURBO BOOST + all cores + max freq + max GPU. High consumption.",
        "safety": "WARN"
    },
    {
        "category": "POWER PROFILES",
        "name": "🔋 EXTREME MODE",
        "type": "action",
        "exec": apply_mode_extreme,
        "desc": "Only 1 core at 800MHz, min GPU, everything off. Maximum battery savings.",
        "safety": "WARN"
    },
    {
        "category": "POWER PROFILES",
        "name": "⚡ AUTO EXTREME MODE",
        "type": "action",
        "exec": apply_mode_autoextreme,
        "desc": "Extreme baseline + dynamic regulation of cores (1-4) and freq (800-1400MHz) based on load.",
        "safety": "SAFE"
    },
    {
        "category": "POWER PROFILES",
        "name": "♻  RESTORE MODE",
        "type": "action",
        "exec": apply_mode_restore,
        "desc": "Restores balanced default values. 8 cores, normal freq, normal GPU.",
        "safety": "SAFE"
    }
]

def draw_view_menu(stdscr, idx, h, w):
    draw = get_power()
    bat = get_battery()
    temp = get_temp()
    stdscr.addstr(2, 2, "SYSTEM STATUS:", curses.A_BOLD)
    stdscr.addstr(3, 4, f"BATTERY: {bat}%", curses.color_pair(2 if bat and int(bat) > 20 else 4))
    stdscr.addstr(3, 20, f"DRAW: {draw:.2f}W", curses.color_pair(3))
    stdscr.addstr(3, 40, f"TEMP: {temp}°C", curses.color_pair(4 if temp.isdigit() and int(temp) > 80 else 3))
    
    stdscr.addstr(4, 4, f"CORES: {get_cores()}/{get_num_cpus()} | CPU: {get_freq_limit()}MHz | EPP: {get_epp()} | PL1: {get_rapl_pl1()}W")
    mode = get_current_mode()
    mode_str = f" >>> PROFILE: {mode} <<< "
    x_pos = max(4, w - len(mode_str) - 2)
    try:
        stdscr.addstr(4, x_pos, mode_str, curses.color_pair(6 if "AUTO" in mode else 2) | curses.A_REVERSE | curses.A_BOLD)
    except:
        pass

    stdscr.addstr(6, 2, "HARDWARE CONTROLS (Use Arrows / Enter):", curses.A_BOLD | curses.color_pair(6))
    
    y = 8
    current_cat = None
    
    for i, opt in enumerate(OPTIONS):
        if y >= h - 6: break
            
        cat = opt.get("category", "GENERAL")
        if cat != current_cat:
            current_cat = cat
            stdscr.addstr(y, 2, f" {cat} ".center(w-4, "-"), curses.color_pair(1) | curses.A_BOLD)
            y += 1
            if y >= h - 6: break

        is_selected = (i == idx)
        style = curses.color_pair(6) | curses.A_REVERSE if is_selected else curses.A_NORMAL
        prefix = " > " if is_selected else "   "
        
        stdscr.attron(style)
        stdscr.addstr(y, 2, prefix + f"{opt['name']:23} ")
        stdscr.attroff(style)

        if opt["type"] == "value":
            try: val = opt["get"]()
            except: val = "ERR"
            val_str = f" [{str(val):<19}] "
            stdscr.addstr(val_str, curses.color_pair(3))
        elif opt["type"] == "toggle":
            try: state = opt["get"]()
            except: state = False
            color = curses.color_pair(2) if state else curses.color_pair(4)
            val_str = f" [{'ON' if state else 'OFF':<19}] "
            stdscr.addstr(val_str, color)
        elif opt["type"] == "action":
            stdscr.addstr(" [ EXECUTE           ] ", curses.color_pair(6))

        s_color = curses.color_pair(2) if opt.get("safety") == "SAFE" else curses.color_pair(3) if opt.get("safety") == "WARN" else curses.color_pair(4)
        stdscr.addstr(f" {opt.get('safety', ''):>7}", s_color)
        y += 1

    try:
        stdscr.addstr(h-5, 2, "─" * (w-4))
        stdscr.addstr(h-4, 2, "EXPLANATION:", curses.A_BOLD | curses.color_pair(6))
        stdscr.addstr(h-3, 4, OPTIONS[idx].get("desc", "")[:w-8], curses.A_ITALIC)
        stdscr.addstr(h-1, 2, "[↑↓] Navigate | [←→] Adjust | [ENTER] Change/Execute | [TAB] Switch View | [Q] Quit", curses.A_DIM)
    except:
        pass
"""

# Replace in content
start_idx = content.find("OPTIONS = [")
end_idx = content.find("def main(stdscr):")

content = content[:start_idx] + new_options + "\n" + content[end_idx:]

with open("power-center.py", "w") as f:
    f.write(content)
