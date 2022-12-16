#!/bin/bash

if ! command -v python3 &> /dev/null || ! command -v python &> /dev/null
  then 
    echo "You don't have python installed. Please check out https://installpython3.com/'"
    exit
fi

if command -v python3 &> /dev/null
  then
    python3 -m venv app-venv
    source app-venv/bin/activate
    pip install -r requirements.txt
fi

if command -v python &> /dev/null
  then
    python -m venv app-venv
    source app-venv/bin/activate
    pip install -r requirements.txt
fi

python3 main.py
