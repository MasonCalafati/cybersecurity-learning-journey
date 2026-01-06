#!/bin/bash
echo "Starting long process..."
for i in {1..30}
do
    echo "Working... $i"
    sleep 2
done
echo "Done!"
