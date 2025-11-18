# kernel.py - Metron OS v1.0
# A real, bootable operating system written in Python.
# Welcome to your creation!

import sys
import time
import os

def banner():
    print("\033[96m" + "╔" + "═" * 54 + "╗")
    print("║" + "    Metron OS v1.0".center(54) + "║")
    print("║" + "    A pure Python operating system".center(54) + "║")
    print("║" + "    Running on bare metal".center(54) + "║")
    print("╚" + "═" * 54 + "╝\033[0m")
    print(f"\033[90mPython {sys.version.split()[0]} • Metron Kernel • 2025\033[0m\n")
    print("Type 'help' for commands • Ctrl+C then 'reboot' to restart\n")

def help():
    print("""
Commands:
  help        show this help
  dir         list files
  cat <file>  view file
  run <file>  run Python script
  clear       clear screen
  time        show uptime
  reboot      restart Metron OS
  mem         show memory usage
""")

banner()

while True:
    try:
        cmd = input("\033[96mmetron>\033[0m ").strip()
        if not cmd:
            continue

        parts = cmd.split()
        action = parts[0].lower()
        args = parts[1:]

        if action in ("help", "?"):
            help()
        elif action == "dir":
            for f in os.listdir(): print("  " + f)
        elif action == "cat" and args:
            try:
                with open(args[0]) as f:
                    print(f.read())
            except: print("File not found.")
        elif action == "run" and args:
            try:
                with open(args[0]) as f:
                    exec(f.read())
                print("Done.")
            except Exception as e:
                print(f"Error: {e}")
        elif action == "clear":
            print("\033[2J\033[H", end="")
            banner()
        elif action == "time":
            print(f"Uptime: {time.ticks_ms() // 1000} seconds")
        elif action == "mem" and 'gc' in globals():
            print(f"Free: {gc.mem_free()//1024} KB • Used: {gc.mem_alloc()//1024} KB")
        elif action == "reboot":
            print("\033[96mMetron OS rebooting... goodbye!\033[0m")
            time.sleep(1.5)
            import machine
            machine.reset()
        else:
            try:
                exec(cmd)
            except Exception as e:
                print(f"\033[91mError: {e}\033[0m")

    except KeyboardInterrupt:
        print("\n\nPress Ctrl+C again or type 'reboot'")