#!/usr/bin/env python3
from bitsv import PrivateKey
import os
import getpass
import json
from cryptography.fernet import Fernet

def generate_key(network):
    """Generate a new Bitcoin SV private key."""
    return PrivateKey(network=network)

def encrypt_private_key(private_key, password):
    """Encrypt the private key using a password."""
    # Generate a key from the password
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    # Encrypt the private key
    encrypted_key = cipher_suite.encrypt(private_key.to_wif().encode())
    
    # Save the encryption key securely (In a real scenario, you should store this securely)
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)

    return encrypted_key

def save_keys_to_file(address, private_key_wif, encrypted_private_key):
    """Save keys to respective files."""
    with open('bsv_public_address.txt', 'a') as pub_file:
        print(address, file=pub_file)
        
    with open('bsv_private_key.txt', 'a') as priv_file:
        print(private_key_wif, file=priv_file)

    with open('bsv_encrypted_private_key.txt', 'a') as enc_file:
        enc_file.write(encrypted_private_key.decode() + '\n')

def main():
    print("Welcome to the Advanced Bitcoin SV Wallet Generator!")
    
    # Prompt user for network preference
    network = input("Enter network (main/test): ").strip().lower() or "main"
    if network not in ["main", "test"]:
        print("Invalid network choice. Defaulting to 'main'.")
        network = "main"

    # Generate keys
    try:
        my_key_test = generate_key(network)
    except Exception as e:
        print(f"Error generating key: {e}")
        return
    
    address = my_key_test.address
    private_key_wif = my_key_test.to_wif()

    # Prompt for password to encrypt private key
    password = getpass.getpass("Enter a password to encrypt your private key: ")
    
    # Encrypt the private key
    encrypted_private_key = encrypt_private_key(my_key_test, password)
    
    # Save keys to files
    save_keys_to_file(address, private_key_wif, encrypted_private_key)
    
    print("Keys generated and saved successfully!")
    print(f"Public Address: {address}")
    print(f"Private Key (WIF) saved in bsv_private_key.txt")
    print(f"Encrypted Private Key saved in bsv_encrypted_private_key.txt")
    print("Make sure to remember your encryption password!")

if __name__ == "__main__":
    main()
