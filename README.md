# PEM Key Generator

A simple tool to generate PEM key files using Python.

[![GitHub license](https://img.shields.io/github/license/linuxjackie/pem-generator)](https://github.com/linuxjackie/pem-generator)
[![GitHub issues](https://img.shields.io/github/issues/linuxjackie/pem-generator)](https://github.com/linuxjackie/pem-generator/issues)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

## Version
**1.0.0** - See [Changelog](#changelog) for details

## Requirements

- Python 3.x

All other dependencies (pyOpenSSL, cryptography, etc.) will be automatically installed on first run.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/linuxjackie/pem-generator.git
cd pem-generator

# Run the appropriate script for your OS
```

## Usage

### Windows Users
- Double click `windows.bat` to run the program
- On first run, it will automatically:
  1. Create Python virtual environment (.venv)
  2. Install required packages
  3. Run the PEM generator

### Mac Users
1. First time setup:
   ```bash
   chmod +x mac.command
   chmod +x mac.sh
   ```
2. Double click `mac.command` to run the program
3. On first run, it will automatically:
   1. Create Python virtual environment (.venv)
   2. Install required packages
   3. Run the PEM generator

### Linux Users
1. First time setup:
   ```bash
   chmod +x linux.sh
   chmod +x linux.desktop
   ```
2. Double click `linux.desktop` to run the program
3. On first run, it will automatically:
   1. Create Python virtual environment (.venv)
   2. Install required packages
   3. Run the PEM generator

## Command Line Arguments

The tool supports the following command line arguments:

```
usage: pem_generator.py [-h] [-f FILENAME] [-p] [-s {1024,2048,4096}] [-v]

Generate RSA key in PEM format

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        output PEM filename (optional, will prompt if not provided)
  -p, --password        enable password protection (default: False)
  -s {1024,2048,4096}, --size {1024,2048,4096}
                        key size in bits, default is 2048
  -v, --version         show program version and exit

Example: python pem_generator.py --filename my_key.pem --password --size 4096
```

## Password Protection

To add password protection to your PEM key, you can:

1. **Use Command Line Arguments**:
   ```bash
   python pem_generator.py --password
   ```
   or
   ```bash
   python pem_generator.py -p
   ```

2. **Modify Scripts**:
   To enable password protection by default in click-to-run mode, edit the script files:
   - For Windows: Change `python pem_generator.py` to `python pem_generator.py --password` in windows.bat
   - For Mac/Linux: Make the same change in the corresponding scripts

## Features

- Generates 2048-bit RSA keys in PEM format
- Sets appropriate file permissions (600) for security
- Simple one-click execution for all major operating systems
- Password protection support
- Automatic virtual environment creation and management
- Automatic package installation
- Multiple key size options (1024, 2048, 4096 bits)
- Pure Python implementation, no system OpenSSL required

## Output

The program will:
1. Create Python virtual environment (if not exists)
2. Install required packages automatically
3. Ask for filename (if not specified via command line)
4. Generate PEM key file with specified name
5. Prompt for password if protection is enabled
6. Set appropriate file permissions
7. Save the file in the same directory

## Notes

1. Make sure Python 3.x is installed
2. All scripts will automatically create virtual environment and install dependencies
3. For security, it's recommended not to move the generated PEM key files
4. Password protection adds security, but make sure to remember your password!

## Contributing

Contributions are welcome! You can:
1. [Submit Issues](https://github.com/linuxjackie/pem-generator/issues)
2. Fork the repository and submit Pull Requests

## Changelog

### 1.0.0 (2024-02-14)
- Initial release
- Pure Python implementation using pyOpenSSL
- Added command line argument support
- Added password protection option
- Improved error handling
- Added multiple key size options
- Automatic virtual environment creation
- Automatic package installation

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/linuxjackie/pem-generator/blob/main/LICENSE) file for details. 