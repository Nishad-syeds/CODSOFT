from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key successfully generated and saved as 'secret.key'.")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(filename, "wb") as file:
        file.write(encrypted)
    print(f"🔒 File '{filename}' encrypted successfully!")

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = fernet.decrypt(data)
    with open(filename, "wb") as file:
        file.write(decrypted)
    print(f"🔓 File '{filename}' decrypted successfully!")

def main():
    print("\n🛡️ Welcome to SecureLock: File Encryptor & Decryptor Tool 🛡️")
    while True:
        print("\n📋 Menu")
        print("1️⃣ Generate Secret Key")
        print("2️⃣ Encrypt a File")
        print("3️⃣ Decrypt a File")
        print("4️⃣ Exit")
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            generate_key()
        elif choice == "2":
            filename = input("📂 Enter the filename to encrypt: ")
            if os.path.exists(filename):
                key = load_key()
                encrypt_file(filename, key)
            else:
                print("❌ File not found!")
        elif choice == "3":
            filename = input("📂 Enter the filename to decrypt: ")
            if os.path.exists(filename):
                key = load_key()
                decrypt_file(filename, key)
            else:
                print("❌ File not found!")
        elif choice == "4":
            print("👋 Thank you for using SecureLock. Stay safe!")
            break
        else:
            print("⚠️ Invalid input. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()
