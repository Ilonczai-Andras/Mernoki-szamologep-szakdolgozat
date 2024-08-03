#!/bin/bash

# Define the path to the Python script
PYTHON_SCRIPT="C:/Users/kille/OneDrive/Mernoki-szamologep-szakdolgozat/Engineering calculator/icon.ico/Main.py"

# Run the Python script using python3
python3 "$PYTHON_SCRIPT"

# Optionally, check if the script executed successfully
if [ $? -eq 0 ]; then
  echo "Python script executed successfully."
else
  echo "Python script failed to execute."
fi
