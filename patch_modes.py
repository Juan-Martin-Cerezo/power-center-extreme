import re

with open("power-center.py", "r") as f:
    content = f.read()

# 1. Remove Hyprland Effects from OPTIONS
content = re.sub(r'\s*\{\s*"category": "GPU & DISPLAY",\s*"name": "Hyprland Effects",.*?"safety": "SAFE"\s*\},', '', content, flags=re.DOTALL)

# 2. Update apply_mode_performance
perf_new = """def apply_mode_performance():
    stop_daemon()
    _set_hypr_monitor(60)
    set_cores(get_num_cpus())
    set_freq_limit(999999)
    set_rapl_pl1(250)
    set_rapl_pl2(250)
    set_epp("performance")
    set_aspm_policy("performance")
    _set_turbo(True)
    set_gpu_limit(2500)
    _set_brightness_pct(100)
    set_kbd_backlight(True)
    run("rfkill unblock wifi")
    set_wifi_powersave(False)
    run("rfkill unblock bluetooth")
    _set_audio_powersave(False)
    for p in __import__("glob").glob("/sys/bus/pci/devices/*/power/control"): set_sys_val(p, "on")
    for p in __import__("glob").glob("/sys/bus/usb/devices/*/power/control"): set_sys_val(p, "on")
    set_sys_val("/proc/sys/kernel/nmi_watchdog", "1")
    set_sys_val("/proc/sys/vm/dirty_writeback_centisecs", 500)
    set_sys_val("/proc/sys/vm/dirty_expire_centisecs", 500)"""

content = re.sub(r'def apply_mode_performance\(\):.*?run\("rfkill unblock bluetooth"\)', perf_new, content, flags=re.DOTALL)

# 3. Remove set_hypr_effects from other modes
content = re.sub(r'set_hypr_effects\(.*?\)\n', '', content)

with open("power-center.py", "w") as f:
    f.write(content)
