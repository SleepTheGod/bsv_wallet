#!/usr/bin/env python3
from bitsv import PrivateKey
import time
import os
import json

def generate_keys(num_keys, network):
    """Generate a specified number of Bitcoin SV keys."""
    keys_info = []
    
    for _ in range(num_keys):
        try:
            my_key = PrivateKey(network=network)
            keys_info.append({
                'address': my_key.address,
                'private_key_hex': my_key.to_hex(),
                'private_key_wif': my_key.to_wif()
            })
            print(f"Address: {my_key.address}")
            print(f"Private Key (HEX): {my_key.to_hex()}")
            print(f"Private Key (WIF): {my_key.to_wif()}\n")
            time.sleep(3)  # Pause for 3 seconds between key generations
        except Exception as e:
            print(f"Error generating key: {e}")
    
    return keys_info

def save_keys_to_file(keys_info, file_path):
    """Save generated keys to a JSON file."""
    try:
        with open(file_path, 'w') as json_file:
            json.dump(keys_info, json_file, indent=4)
        print(f"Keys saved to {file_path}")
    except Exception as e:
        print(f"Error saving keys to file: {e}")

def main():
    print("Welcome to the Advanced Bitcoin SV Wallet Generator!")
    
    # Prompt user for network preference
    network = input("Enter network (main/test): ").strip().lower() or "test"
    if network not in ["main", "test"]:
        print("Invalid network choice. Defaulting to 'test'.")
        network = "test"
    
    # Prompt user for the number of keys to generate
    try:
        num_keys = int(input("Enter the number of keys to generate (default: 1000): ") or 1000)
    except ValueError:
        print("Invalid number entered. Defaulting to 1000.")
        num_keys = 1000
    
    # Generate keys
    keys_info = generate_keys(num_keys, network)
    
    # Save keys to a file
    save_keys_to_file(keys_info, 'bsv_keys.json')

if __name__ == "__main__":
    main()
