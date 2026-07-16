//go:build windows
// +build windows

// Package hal implements hardware abstraction layer controls
package hal

import "runtime" // Used to query Go runtime information like CPU count

// WindowsBackend implements the Backend interface for Windows systems
// Currently, this acts as a stub to allow compilation and basic UI functionality on Windows
// without crashing, although most hardware power features require specific Windows APIs.
type WindowsBackend struct{}

// init automatically registers this backend if compiled on Windows
func init() { CurrentBackend = &WindowsBackend{} }

// GetOS returns the name of the operating system
func (b *WindowsBackend) GetOS() string { return "Windows" }
// GetNumCPUs returns the total number of logical CPUs available on Windows
func (b *WindowsBackend) GetNumCPUs() int { return runtime.NumCPU() }
// GetCores returns the current number of active online cores (stubbed to total)
func (b *WindowsBackend) GetCores() int { return runtime.NumCPU() }
// SetCores disables or enables CPU cores (Not yet implemented for Windows)
func (b *WindowsBackend) SetCores(n int) {}
// GetFreqLimit returns the max CPU frequency limit (Not yet implemented)
func (b *WindowsBackend) GetFreqLimit() int { return 0 }
// SetFreqLimit sets the max CPU frequency limit
func (b *WindowsBackend) SetFreqLimit(m int) {}
// GetBatteryPercentage returns 100 as a placeholder
func (b *WindowsBackend) GetBatteryPercentage() int { return 100 }
// IsCharging returns true as a placeholder
func (b *WindowsBackend) IsCharging() bool { return true }
// GetBatteryTime returns N/A as a placeholder
func (b *WindowsBackend) GetBatteryTime() string { return "N/A" }
// GetPowerConsumptionWatts returns 0.0 as a placeholder
func (b *WindowsBackend) GetPowerConsumptionWatts() float64 { return 0.0 }
// GetRAPLPL1 returns 0 as a placeholder
func (b *WindowsBackend) GetRAPLPL1() int { return 0 }
// SetRAPLPL1 sets RAPL limit (Not yet implemented)
func (b *WindowsBackend) SetRAPLPL1(w int) {}
// GetRAPLPL2 returns 0 as a placeholder
func (b *WindowsBackend) GetRAPLPL2() int { return 0 }
// SetRAPLPL2 sets RAPL PL2 limit (Not yet implemented)
func (b *WindowsBackend) SetRAPLPL2(w int) {}
// GetTurbo returns true as a placeholder
func (b *WindowsBackend) GetTurbo() bool { return true }
// SetTurbo toggles CPU boost (Not yet implemented)
func (b *WindowsBackend) SetTurbo(e bool) {}
// GetEPP returns default preference
func (b *WindowsBackend) GetEPP() string { return "default" }
// SetEPP sets Energy Performance Preference
func (b *WindowsBackend) SetEPP(p string) {}
// GetGPUFreq returns 0
func (b *WindowsBackend) GetGPUFreq() int { return 0 }
// SetGPUFreq sets max GPU frequency
func (b *WindowsBackend) SetGPUFreq(m int) {}
// GetASPM returns default ASPM policy
func (b *WindowsBackend) GetASPM() string { return "default" }
// SetASPM sets PCIe ASPM policy
func (b *WindowsBackend) SetASPM(p string) {}
// GetWifiPowerSave returns false
func (b *WindowsBackend) GetWifiPowerSave() bool { return false }
// SetWifiPowerSave toggles WiFi power saving
func (b *WindowsBackend) SetWifiPowerSave(e bool) {}
// GetKbdBacklight returns false
func (b *WindowsBackend) GetKbdBacklight() bool { return false }
// SetKbdBacklight toggles keyboard backlight
func (b *WindowsBackend) SetKbdBacklight(e bool) {}
// GetAudioPowerSave returns false
func (b *WindowsBackend) GetAudioPowerSave() bool { return false }
// SetAudioPowerSave toggles audio power saving
func (b *WindowsBackend) SetAudioPowerSave(e bool) {}

// SetBrightnessTarget is a placeholder
func (b *WindowsBackend) SetBrightnessTarget(t string) {}
// SetRefreshRate is a placeholder
func (b *WindowsBackend) SetRefreshRate(t string) {}
// SetHyprEffects is a placeholder
func (b *WindowsBackend) SetHyprEffects(e bool) {}
// SetNMIWatchdog is a placeholder
func (b *WindowsBackend) SetNMIWatchdog(e bool) {}
// SetVMDirty is a placeholder
func (b *WindowsBackend) SetVMDirty(w int, e int) {}

// GetLCDBrightness returns 100%
func (b *WindowsBackend) GetLCDBrightness() int { return 100 }
// SetLCDBrightness sets display brightness
func (b *WindowsBackend) SetLCDBrightness(percent int) {}
// GetBluetooth returns true
func (b *WindowsBackend) GetBluetooth() bool { return true }
// SetBluetooth toggles Bluetooth
func (b *WindowsBackend) SetBluetooth(enabled bool) {}
// GetWifiEnable returns true
func (b *WindowsBackend) GetWifiEnable() bool { return true }
// SetWifiEnable toggles WiFi
func (b *WindowsBackend) SetWifiEnable(enabled bool) {}
// GetAutosuspend returns false
func (b *WindowsBackend) GetAutosuspend() bool { return false }
// SetAutosuspend toggles autosuspend
func (b *WindowsBackend) SetAutosuspend(enabled bool) {}
// GetWatchdog returns true
func (b *WindowsBackend) GetWatchdog() bool { return true }
// SetWatchdog toggles watchdog
func (b *WindowsBackend) SetWatchdog(enabled bool) {}
// GetVMWriteback returns 500
func (b *WindowsBackend) GetVMWriteback() int { return 500 }
// SetVMWriteback sets dirty writeback centisecs
func (b *WindowsBackend) SetVMWriteback(centisecs int) {}
// ProcessPurge is a placeholder
func (b *WindowsBackend) ProcessPurge() {}

// ApplyModePerformance applies high performance mode
func (b *WindowsBackend) ApplyModePerformance() {}
// ApplyModeExtreme applies battery saving mode
func (b *WindowsBackend) ApplyModeExtreme() {}
// ApplyModeRestore restores default settings
func (b *WindowsBackend) ApplyModeRestore() {}
// StartAutoExtremeDaemon starts auto adjustment daemon
func (b *WindowsBackend) StartAutoExtremeDaemon() {}
// StopDaemon stops the background daemon
func (b *WindowsBackend) StopDaemon() {}
