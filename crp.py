import os
from cryptography.fernet import Fernet

KEY_FILE = 'secret.key'
NOTES_FILE = 'notes.txt'


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key


def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()


def encrypt_message(message, key):
    return Fernet(key).encrypt(message.encode())


def decrypt_message(encrypted_message, key):
    return Fernet(key).decrypt(encrypted_message).decode()


def write_note():
    note = input("Enter your note:\n> ")
    key = load_key()
    encrypted = encrypt_message(note, key)
    with open(NOTES_FILE, 'ab') as f:
        f.write(encrypted + b'\n')
    print("✅ Note saved securely.")


def read_notes():
    if not os.path.exists(NOTES_FILE):
        print("⚠️ No notes found.")
        return
    key = load_key()
    print("\n📖 Your Notes:")
    with open(NOTES_FILE, 'rb') as f:
        for line in f:
            try:
                decrypted = decrypt_message(line.strip(), key)
                print(f"- {decrypted}")
            except Exception as e:
                print("❌ Failed to decrypt a note:", e)


def main():
    while True:
        print("\n--- Secure Notes App ---")
        print("1. Write a Note")
        print("2. Read Notes")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            write_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")


if __name__ == '__main__':
    main()
