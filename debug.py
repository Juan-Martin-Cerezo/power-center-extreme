import os

def test_write(path, val):
    try:
        with open(path, 'w') as f:
            f.write(str(val) + '\n')
        print(f"OK: Wrote '{val}' to {path}")
        
        try:
            with open(path, 'r') as f:
                current = f.read().strip()
            print(f"   -> Verification: {current}")
        except Exception as e2:
            pass
            
    except Exception as e:
        print(f"FAIL: Could not write '{val}' to {path}. Error: {e}")

print("--- DEBUGGING CPU CORES ---")
test_write("/sys/devices/system/cpu/cpu1/online", "0")

print("\n--- DEBUGGING CPU FREQ ---")
test_write("/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq", "400000")
test_write("/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq", "400000")

print("\n--- DEBUGGING EPP ---")
test_write("/sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference", "power")
