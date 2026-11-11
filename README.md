# runx - Detached Process Launcher for Debian Linux

`runx` is a lightweight Python-based command-line tool designed for Debian Linux to launch any GUI application or CLI command, detaching it completely from the terminal session.

## Project Structure

```text
runx/
├── runx.py         # Core Python CLI implementation
├── test_runx.py    # Unit tests for verification
├── pyproject.toml  # Modern Python packaging configuration
└── README.md       # Documentation and installation instructions
```

## Features

1. **Complete Terminal Detachment:** Uses `subprocess.Popen` with `start_new_session=True` (calling `os.setsid()` under the hood) to create a new session and process group.
2. **SIGHUP Immunity:** Closing the terminal where `runx` was executed does **not** terminate or kill the spawned application.
3. **Immediate Unblocking:** The original terminal prompt returns immediately without waiting for the launched application to finish.
4. **Clean I/O Handling:** Redirects `stdin`, `stdout`, and `stderr` to `DEVNULL` to prevent hanging on terminal closure or pipe blocks.
5. **Universal Support:** Works for both GUI applications (e.g., `mousepad`, `firefox`, `vlc`) and background CLI services/scripts.

---

## Usage Syntax

```bash
runx <command> [arguments...]
```

### Examples

- **Launch a GUI text editor with a file:**
  ```bash
  runx mousepad notes.txt
  ```
- **Launch a web browser:**
  ```bash
  runx firefox https://debian.org
  ```
- **Launch a media player:**
  ```bash
  runx vlc video.mp4
  ```

---

## Installation & Setup Instructions

### Option 1: Install via Pip (Recommended)
From within the `runx` directory containing `pyproject.toml`:

```bash
pip install --user .
```
*(Ensure `~/.local/bin` is in your `PATH`)*

### Option 2: Manual Installation to `/usr/local/bin`
Copy `runx.py` directly as `runx`:

```bash
sudo cp runx.py /usr/local/bin/runx
sudo chmod +x /usr/local/bin/runx
```

---

## Running Tests

To verify correctness:

```bash
python3 test_runx.py
```
