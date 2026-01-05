#!/bin/bash
echo "=== System Information ==="
echo "Current user: $USER"
echo "Current directory: $(pwd)"
echo "Date and time: $(date)"
echo "Disk usage:"
df -h | head -n 2 
