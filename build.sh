#!/bin/bash
echo "Building Metron OS v1.0..."
dd if=/dev/zero of=metron-os.img bs=1024 count=1440 2>/dev/null
mkfs.fat -F 12 metron-os.img >/dev/null 2>&1
mkdir -p mnt
sudo mount -o loop metron-os.img mnt
sudo cp ../pycorn-core-1.0.img mnt/kernel.bin   # you’ll have this from the next step
sudo cp kernel.py autoexec.txt mnt/
sudo umount mnt && rmdir mnt
echo "Metron OS built! Run:"
echo "qemu-system-i386 -fda metron-os.img -boot a"