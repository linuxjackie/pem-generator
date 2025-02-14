import os
import subprocess

def generate_pem_key():
    """
    Generates a PEM key with a single command.
    """

    # Ask the user for the PEM file name
    filename = input("Please enter the name of the PEM file (without extension):")
    filename = filename.strip() + ".pem"  # Ensure it has a .pem extension

    # Check if the file already exists
    if os.path.exists(filename):
        print(f"Error: File '{filename}' already exists. Please choose another name.")
        return

    try:
        # Use openssl command to generate the key
        #   - Generate an RSA key with a length of 2048 bits
        #   - Do not use password protection for the key (you can add `-passout pass:<password>` option if needed)
        #   - Output to the specified file
        subprocess.run(
            ["openssl", "genrsa", "-out", filename, "2048"],
            check=True,  # Check if the command executed successfully
            capture_output=True,  # Capture output for debugging
            text=True,  # Handle output in text mode
        )
        print(f"PEM key has been successfully generated and saved to '{filename}'")

        # (Optional) Set file permissions, only owner can read and write
        os.chmod(filename, 0o600)
        print(f"File permissions have been set to owner read/write only (600).")


    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the key:")
        print(f"  Command: {e.cmd}")
        print(f"  Standard Output: {e.stdout}")
        print(f"  Standard Error: {e.stderr}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

if __name__ == "__main__":
    generate_pem_key()
