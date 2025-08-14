from .whisper import whisperer as say
from .echo import listener as listen
import sys

__all__ = ["listen", "say"]

def main():
    """Main entry point for the d-encryptor package."""
    if len(sys.argv) < 2:
        print("d-encryptor: A drift cipher encryption/decryption tool")
        print("Usage:")
        print("  python -m d_encryptor encrypt <message> <drift>")
        print("  python -m d_encryptor decrypt <encrypted_message> [drift]")
        print("  d-encryptor encrypt <message> <drift>")
        print("  d-encryptor decrypt <encrypted_message> [drift]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "encrypt":
        if len(sys.argv) != 4:
            print("Usage: encrypt <message> <drift>")
            sys.exit(1)
        message = sys.argv[2]
        drift = sys.argv[3]
        encrypted = say(message, drift)
        print(f"Your whisper is: {encrypted}")
        
    elif command == "decrypt":
        if len(sys.argv) < 3 or len(sys.argv) > 4:
            print("Usage: decrypt <encrypted_message> [drift]")
            sys.exit(1)
        encrypted_message = sys.argv[2]
        drift = sys.argv[3] if len(sys.argv) == 4 else None
        decrypted = listen(encrypted_message, drift)
        if decrypted:
            print(f"You received a whisper: {decrypted}")
    else:
        print(f"Unknown command: {command}")
        print("Available commands: encrypt, decrypt")
        sys.exit(1)

if __name__ == "__main__":
    main()