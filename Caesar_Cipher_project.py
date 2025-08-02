# Caesar Cipher - Encrypt and Decrypt Messages
# Created by: Saharsh Hegde

def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char  # keep spaces, numbers, symbols unchanged
    return encrypted_text


def decrypt(message, shift):
    return encrypt(message, -shift)


def start_cipher():
    print("\n---------------------------")
    print("  Caesar Cipher Tool ")
    print("  By: Saharsh Hegde")
    print("---------------------------\n")

    print("1. Encrypt Message")
    print("2. Decrypt Message")
    choice = input("\nEnter your choice (1/2): ").strip()

    if choice not in ['1', '2']:
        print(" Invalid option. Please choose 1 or 2.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value : "))
    except ValueError:
        print(" Shift must be a number.")
        return

    if choice == '1':
        result = encrypt(message, shift)
        print(f"\n Encrypted Message: {result}")
    else:
        result = decrypt(message, shift)
        print(f"\n Decrypted Message: {result}")


# Run the program
if __name__ == "__main__":
    start_cipher()