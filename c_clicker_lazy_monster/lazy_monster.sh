#!/bin/bash

echo "Stopping activity_monitor.service..."
sudo systemctl stop activity_monitor.service

echo "Starting lazy_monster.elf..."
sudo /usr/local/bin/lazy_monster.elf --start 100 > /var/log/lazy_monster.log &

echo "Start activity_monitor.service..."
sudo systemctl start activity_monitor.service
