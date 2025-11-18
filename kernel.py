# kernel.py - Metron OS v1.0
# AI-Powered Offensive Security OS • Built with Python • T4z4r • 2025

import sys
import time
import os

def big_banner():
    print("\033[96m")  # Cyan color
    print("███╗   ███╗███████╗████████╗██████╗  ██████╗ ███╗   ██╗")
    print("████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║")
    print("██╔████╔██║█████╗     ██║   ██████╔╝██║   ██║██╔██╗ ██║")
    print("██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║")
    print("██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║")
    print("╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\033[0m")
    print("          \033[95mAI-Powered Offensive Security OS Built with Python • T4z4r • 2025\033[0m")
    print()

def banner():
    big_banner()
    print(f"\033[90mMetron OS v1.0 • Python {sys.version.split()[0]} • Offensive Security Edition\033[0m")
    print("Type 'help' for command list • 'reboot' to restart • Ctrl+C twice to force reboot\n")

def help():
    print("""
\033[93mOffensive Security Commands:\033[0m
  help        show this menu
  dir         list filesystem
  cat <file>  view file
  run <file>  execute Python payload
  clear       wipe screen
  time        system uptime
  mem         memory status
  reboot      restart Metron OS
  \033[91m> exec any raw Python directly\033[0m
""")

banner()

while True:
    try:
        # cSpell:ignore metron
        cmd = input("\033[96mmetron>\033[0m ").strip()
        if not cmd:
            continue

        parts = cmd.split()
        action = parts[0].lower()
        args = parts[1:]

        if action in ("help", "?"):
            help()
        elif action == "dir":
            for f in sorted(os.listdir()):
                print("  " + f)
        elif action == "cat" and args:
            try:
                with open(args[0]) as f: print(f.read())
            except: print("\033[91m[!] File not found or access denied\033[0m")
        elif action == "run" and args:
            try:
                with open(args[0]) as f:
                    print(f"\033[93m[+] Executing {args[0]}...\033[0m")
                    exec(f.read())
                print("\033[92m[+] Payload completed\033[0m")
            except Exception as e:
                print(f"\033[91m[!] Exploit failed: {e}\033[0m")
        elif action == "clear":
            print("\033[2J\033[H", end="")
            banner()
        elif action == "time":
            print(f"Uptime: {time.ticks_ms() // 1000} seconds")
        elif action == "mem" and 'gc' in globals():
            print(f"Free: {gc.mem_free()//1024} KB • Used: {gc.mem_alloc()//1024} KB")
        elif action == "reboot":
            print("\033[91m[!!!] Metron OS initiating reboot sequence...\033[0m")
            time.sleep(1.8)
            import machine
            machine.reset()
        else:
            try:
                exec(cmd)
            except Exception as e:
                print(f"\033[91m[!] Execution error: {e}\033[0m")

    except KeyboardInterrupt:
        print("\n\033[91mInterrupted. Type 'reboot' or press Ctrl+C again.\033[0m")