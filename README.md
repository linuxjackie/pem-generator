# PEM Key Generator

A simple tool to generate PEM key files using OpenSSL.

## Requirements

- Python 3.x
- OpenSSL

## Usage

### Windows Users
- Double click `windows.bat` to run the program

### Mac Users
1. First time setup:
   ```bash
   chmod +x mac.command
   ```
2. Then double click `mac.command` to run the program

### Linux Users
1. First time setup:
   ```bash
   chmod +x linux.sh
   chmod +x linux.desktop
   ```
2. Then double click `linux.desktop` to run the program

## Features

- Generates 2048-bit RSA key in PEM format
- Sets appropriate file permissions (600) for security
- Simple one-click execution for all major operating systems
- No password protection by default (can be modified if needed)

## Output

The program will:
1. Ask you for a filename
2. Generate a PEM key file with the specified name
3. Set appropriate file permissions
4. Save the file in the same directory

## Note

Make sure OpenSSL is installed on your system before running the program. 