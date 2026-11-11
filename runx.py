#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
runx - A robust CLI tool for Debian Linux to launch GUI and CLI applications
completely detached from the terminal session.
"""

import sys
import os
import subprocess

def print_help():
    print("Usage: runx <command> [arguments...]")
    print("Example:")
    print("  runx mousepad document.txt")
    print("  runx firefox https://example.com")
    print("  runx vlc video.mp4")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 1)

    cmd_args = sys.argv[1:]

    try:
        # Spawn the process detached from the current terminal session.
        # start_new_session=True calls os.setsid() in the child process, creating
        # a new session and process group. This prevents SIGHUP when the parent terminal closes.
        # Redirection of stdin, stdout, and stderr to DEVNULL prevents I/O blocks
        # and terminal clutter.
        process = subprocess.Popen(
            cmd_args,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
    except FileNotFoundError:
        print(f"Error: Command not found: {cmd_args[0]}", file=sys.stderr)
        sys.exit(127)
    except Exception as e:
        print(f"Error launching command: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
