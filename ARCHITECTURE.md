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
│   ├── backend_darwin.go # macOS native implementation (pmset)
│   └── backend_windows.go# Windows native implementation (powercfg, WMI)
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

Cuando la aplicación arranca, `hal.CurrentBackend` es inyectado gracias a los build tags de Go (`//go:build linux`, `//go:build windows`, `//go:build darwin`). Esto significa que `main.go` y la Interfaz Gráfica (`ui/cli.go`) nunca necesitan saber en qué sistema operativo están corriendo.

### The User Interface (UI)
The `ui.Dashboard` struct handles the presentation layer using `tcell`.
Contruye una lista de `MenuItem` que conecta la interfaz gráfica a los métodos de la interfaz `hal.Backend`. Dependiendo del OS devuelto por `b.GetOS()`, los menús ocultan opciones no soportadas nativamente por el SO anfitrión, garantizando que todos los botones funcionales hagan lo prometido sin generar errores silenciosos.

**Dynamic Layout Engine:**
The UI dynamically detects terminal sizes on every redraw event:
- If the terminal is wider than 130 columns, it splits the menu and the graph side-by-side.
- If narrower, it stacks the graph on top of the menu and calculates visible list items, adding a visual scrollbar.

### Auto Daemon
La implementación en `hal` posee un proceso en segundo plano (Goroutine) llamado "Auto Extreme Daemon". Cuando está habilitado, monitorea la carga en el CPU (loadavg en Unix/Mac o typeperf en Windows) cada 10 segundos.
- Si está conectada a la corriente, aplica Máximo Rendimiento.
- Si está con batería, calcula un factor normalizado matemático (`discretePower`), y ajusta los límites de hardware (brillo de pantalla, frecuencias, limits de acelerador) proporcionalmente a la carga de procesamiento, logrando un ahorro de batería ultra fino sin congelar la PC durante picos de trabajo.
