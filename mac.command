#!/bin/bash
cd "$(dirname "$0")"
python3 pem_generator.py
read -p "Press Enter to continue..." 