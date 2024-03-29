#!/bin/bash

# Set the niceness value to -10 and run the Python script
nohup python3 matches.py >> matches.log 2>&1 &
