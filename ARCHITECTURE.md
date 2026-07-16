# System Architecture ⚙️

Power Center Extreme uses a highly modular, decoupled architecture focused on performance, maintainability, and cross-platform compatibility.

## Core Design Principles

1. **Strict Decoupling**: The User Interface (`ui/`) has absolutely zero knowledge of how hardware limits are actually enforced. It merely calls interface methods.
2. **Hardware Abstraction Layer (HAL)**: All hardware interactions are routed through a unified interface (`hal/backend.go`). This allows the system to easily adapt to Windows, macOS, or Linux.
3. **No External Dependencies for Hardware**: We avoid third-party libraries for hardware access. On Linux, this is achieved by reading and writing directly to the kernel's `/sys/` pseudo-filesystem.

## Directory Structure

```
power-center-extreme/
├── main.go               # Entry point, parses flags (like --daemon) and injects backend
├── hal/                  # Hardware Abstraction Layer
│   ├── backend.go        # Defines the `Backend` interface that all OS-specific files must implement
│   ├── backend_linux.go  # Linux implementation using sysfs
│   ├── backend_darwin.go # macOS stub implementation
│   └── backend_windows.go# Windows stub implementation
└── ui/                   # Terminal User Interface
    └── cli.go            # Draws the TUI, manages state, handles user input using `tcell`
```

## How It Works

### The Hardware Abstraction Layer (HAL)
The `Backend` interface dictates what actions a platform *must* support, such as:
- `GetNumCPUs() int`
- `SetFreqLimit(mhz int)`
- `GetBatteryPercentage() int`
- `ApplyModeExtreme()`

When the application boots, `hal.CurrentBackend` is populated automatically thanks to Go's build tags (`//go:build linux`). This means the `main.go` file doesn't even need to know what OS it is running on.

### The User Interface (UI)
The `ui.Dashboard` struct handles the presentation layer using `tcell`.
It constructs a dynamic list of `MenuItem` objects, which wire up the UI text to the underlying `hal.Backend` methods.

**Dynamic Layout Engine:**
The UI dynamically detects terminal sizes on every redraw event:
- If the terminal is wider than 130 columns, it splits the menu and the graph side-by-side.
- If narrower, it stacks the graph on top of the menu and calculates visible list items, adding a visual scrollbar.

### Auto Daemon
The `hal` implementation contains a background process called the Auto Extreme Daemon. When triggered (either via UI or CLI `--daemon`), it spins up a Goroutine that wakes up every 10 seconds. It monitors:
- Plugged in status (applies Maximum Performance).
- Battery Critical status (applies Extreme Mode).
- Normal Battery status (applies Default OS limits).
