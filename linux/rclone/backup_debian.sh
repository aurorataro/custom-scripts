#!/bin/bash

rclone copy /mnt/data onedrive:Public/TaroNAS --transfers 8 --progress --filter-from "filter-list.txt" --bwlimit "04:00,off 12:00,1.5M"
