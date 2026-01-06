#!/bin/bash


echo "===================================="
echo "     SYSTEM MONITORING REPORT"
echo "===================================="
echo ""

echo "Date: $(date)"
echo ""

echo "System Uptime:"
uptime
echo ""

echo "Memory Usage:"
free -h
echo ""

echo "Disk Usage:"
df -h | head -n 5
echo ""

echo "Top 5 CPU Processes:"
ps aux | sort -nrk 3,3 | head -n 6
echo ""

echo "Logged in users:"
who
echo ""

echo "========================================="
echo "Report generated successfully!"
echo "========================================="
