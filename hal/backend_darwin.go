//go:build darwin
// +build darwin

// Package hal implements hardware abstraction layer controls
package hal

import "runtime" // Used to query Go runtime information like CPU count

// DarwinBackend implements the Backend interface for macOS systems
// Currently, this acts as a stub to allow compilation and basic UI functionality on macOS
// without crashing, although most hardware power features require specific macOS APIs.
type DarwinBackend struct{}

// init automatically registers this backend if compiled on macOS
func init() { CurrentBackend = &DarwinBackend{} }

// GetOS returns the name of the operating system
func (b *DarwinBackend) GetOS() string { return "macOS" }
// GetNumCPUs returns the total number of logical CPUs available on the Mac
func (b *DarwinBackend) GetNumCPUs() int { return runtime.NumCPU() }
// GetCores returns the current number of active online cores (stubbed to total)
func (b *DarwinBackend) GetCores() int { return runtime.NumCPU() }
// SetCores disables or enables CPU cores (Not yet implemented for macOS)
func (b *DarwinBackend) SetCores(n int) {}
// GetFreqLimit returns the max CPU frequency limit (Not yet implemented)
func (b *DarwinBackend) GetFreqLimit() int { return 0 }
// SetFreqLimit sets the max CPU frequency limit
func (b *DarwinBackend) SetFreqLimit(m int) {}
// GetBatteryPercentage returns 100 as a placeholder
func (b *DarwinBackend) GetBatteryPercentage() int { return 100 }
// IsCharging returns true as a placeholder
func (b *DarwinBackend) IsCharging() bool { return true }
// GetBatteryTime returns N/A as a placeholder
func (b *DarwinBackend) GetBatteryTime() string { return "N/A" }
// GetPowerConsumptionWatts returns 0.0 as a placeholder
func (b *DarwinBackend) GetPowerConsumptionWatts() float64 { return 0.0 }
// GetRAPLPL1 returns 0 as a placeholder
func (b *DarwinBackend) GetRAPLPL1() int { return 0 }
// SetRAPLPL1 sets RAPL limit (Not yet implemented)
func (b *DarwinBackend) SetRAPLPL1(w int) {}
// GetRAPLPL2 returns 0 as a placeholder
func (b *DarwinBackend) GetRAPLPL2() int { return 0 }
// SetRAPLPL2 sets RAPL PL2 limit (Not yet implemented)
func (b *DarwinBackend) SetRAPLPL2(w int) {}
// GetTurbo returns true as a placeholder
func (b *DarwinBackend) GetTurbo() bool { return true }
// SetTurbo toggles CPU boost (Not yet implemented)
func (b *DarwinBackend) SetTurbo(e bool) {}
// GetEPP returns default preference
func (b *DarwinBackend) GetEPP() string { return "default" }
// SetEPP sets Energy Performance Preference
func (b *DarwinBackend) SetEPP(p string) {}
// GetGPUFreq returns 0
func (b *DarwinBackend) GetGPUFreq() int { return 0 }
// SetGPUFreq sets max GPU frequency
func (b *DarwinBackend) SetGPUFreq(m int) {}
// GetASPM returns default ASPM policy
func (b *DarwinBackend) GetASPM() string { return "default" }
// SetASPM sets PCIe ASPM policy
func (b *DarwinBackend) SetASPM(p string) {}
// GetWifiPowerSave returns false
func (b *DarwinBackend) GetWifiPowerSave() bool { return false }
// SetWifiPowerSave toggles WiFi power saving
func (b *DarwinBackend) SetWifiPowerSave(e bool) {}
// GetKbdBacklight returns false
func (b *DarwinBackend) GetKbdBacklight() bool { return false }
// SetKbdBacklight toggles keyboard backlight
func (b *DarwinBackend) SetKbdBacklight(e bool) {}
// GetAudioPowerSave returns false
func (b *DarwinBackend) GetAudioPowerSave() bool { return false }
// SetAudioPowerSave toggles audio power saving
func (b *DarwinBackend) SetAudioPowerSave(e bool) {}

// SetBrightnessTarget is a placeholder
func (b *DarwinBackend) SetBrightnessTarget(t string) {}
// SetRefreshRate is a placeholder
func (b *DarwinBackend) SetRefreshRate(t string) {}
// SetHyprEffects is a placeholder
func (b *DarwinBackend) SetHyprEffects(e bool) {}
// SetNMIWatchdog is a placeholder
func (b *DarwinBackend) SetNMIWatchdog(e bool) {}
// SetVMDirty is a placeholder
func (b *DarwinBackend) SetVMDirty(w int, e int) {}

// GetLCDBrightness returns 100%
func (b *DarwinBackend) GetLCDBrightness() int { return 100 }
// SetLCDBrightness sets display brightness
func (b *DarwinBackend) SetLCDBrightness(percent int) {}
// GetBluetooth returns true
func (b *DarwinBackend) GetBluetooth() bool { return true }
// SetBluetooth toggles Bluetooth
func (b *DarwinBackend) SetBluetooth(enabled bool) {}
// GetWifiEnable returns true
func (b *DarwinBackend) GetWifiEnable() bool { return true }
// SetWifiEnable toggles WiFi
func (b *DarwinBackend) SetWifiEnable(enabled bool) {}
// GetAutosuspend returns false
func (b *DarwinBackend) GetAutosuspend() bool { return false }
// SetAutosuspend toggles autosuspend
func (b *DarwinBackend) SetAutosuspend(enabled bool) {}
// GetWatchdog returns true
func (b *DarwinBackend) GetWatchdog() bool { return true }
// SetWatchdog toggles watchdog
func (b *DarwinBackend) SetWatchdog(enabled bool) {}
// GetVMWriteback returns 500
func (b *DarwinBackend) GetVMWriteback() int { return 500 }
// SetVMWriteback sets dirty writeback centisecs
func (b *DarwinBackend) SetVMWriteback(centisecs int) {}
// ProcessPurge is a placeholder
func (b *DarwinBackend) ProcessPurge() {}

// ApplyModePerformance applies high performance mode
func (b *DarwinBackend) ApplyModePerformance() {}
// ApplyModeExtreme applies battery saving mode
func (b *DarwinBackend) ApplyModeExtreme() {}
// ApplyModeRestore restores default settings
func (b *DarwinBackend) ApplyModeRestore() {}

